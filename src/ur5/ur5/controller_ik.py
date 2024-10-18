#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from geometry_msgs.msg import Pose
import PyKDL
import numpy as np


class UR5InverseKinematicsController(Node):
    def __init__(self):
        super().__init__("ur5_inverse_kinematics_controller")

        # Define UR5 parameters
        self.num_joints = 6
        self.joints = [
            "shoulder_pan_joint",
            "shoulder_lift_joint",
            "elbow_joint",
            "wrist_1_joint",
            "wrist_2_joint",
            "wrist_3_joint",
        ]

        # Joint limits for UR5 (min and max in radians)
        joint_limits_min = np.array([-2 * np.pi] * self.num_joints)  # Example values
        joint_limits_max = np.array([2 * np.pi] * self.num_joints)  # Example values

        # Convert NumPy arrays to PyKDL JntArray
        self.joint_limits_min = PyKDL.JntArray(self.num_joints)
        self.joint_limits_max = PyKDL.JntArray(self.num_joints)

        # Assign joint limits to JntArray
        for i in range(self.num_joints):
            self.joint_limits_min[i] = joint_limits_min[i]
            self.joint_limits_max[i] = joint_limits_max[i]

        # Create KDL chain (adjust DH parameters as needed for UR5)
        self.chain = PyKDL.Chain()
        self.chain.addSegment(
            PyKDL.Segment(
                PyKDL.Joint(PyKDL.Joint.RotZ), PyKDL.Frame.DH(0, 0.089159, 0, np.pi / 2)
            )
        )
        self.chain.addSegment(
            PyKDL.Segment(
                PyKDL.Joint(PyKDL.Joint.RotY), PyKDL.Frame.DH(0, 0, -0.425, 0)
            )
        )
        self.chain.addSegment(
            PyKDL.Segment(
                PyKDL.Joint(PyKDL.Joint.RotY), PyKDL.Frame.DH(0, 0, -0.39225, 0)
            )
        )
        self.chain.addSegment(
            PyKDL.Segment(
                PyKDL.Joint(PyKDL.Joint.RotY), PyKDL.Frame.DH(0, 0.10915, 0, np.pi / 2)
            )
        )
        self.chain.addSegment(
            PyKDL.Segment(
                PyKDL.Joint(PyKDL.Joint.RotZ), PyKDL.Frame.DH(0, 0.09465, 0, -np.pi / 2)
            )
        )
        self.chain.addSegment(
            PyKDL.Segment(
                PyKDL.Joint(PyKDL.Joint.RotY), PyKDL.Frame.DH(0, 0.0823, 0, 0)
            )
        )

        # Create solvers
        self.fk_solver = PyKDL.ChainFkSolverPos_recursive(self.chain)
        self.ik_v_solver = PyKDL.ChainIkSolverVel_pinv(self.chain)
        self.ik_solver = PyKDL.ChainIkSolverPos_NR_JL(
            self.chain,  # KDL chain
            self.joint_limits_min,  # Joint limits minimum (JntArray)
            self.joint_limits_max,  # Joint limits maximum (JntArray)
            self.fk_solver,  # Forward kinematics solver
            self.ik_v_solver,  # Inverse velocity solver
            100,  # Maximum iterations
            1e-6,  # Tolerance
        )

        # PID controller parameters for each joint
        self.kp = [0.5] * self.num_joints  # Proportional gain
        self.ki = [0.0] * self.num_joints  # Integral gain
        self.kd = [0.1] * self.num_joints  # Derivative gain

        # Variables to track previous errors for derivative control and integrals for integral control
        self.previous_errors = [0.0] * self.num_joints
        self.integral_errors = [0.0] * self.num_joints

        # Initial joint angles
        self.declare_parameter(
            "joint_angles", [0.0, -np.pi / 2, 0.0, -np.pi / 2, 0.0, 0.0]
        )
        self.initial_joint_angles = self.get_parameter("joint_angles").value

        # Create publisher and subscriber
        self.publisher_ = self.create_publisher(
            JointTrajectory, "/joint_trajectory_controller/joint_trajectory", 10
        )
        self.subscription = self.create_subscription(
            Pose, "/desired_pose", self.pose_callback, 10
        )

        # Publish initial joint angles
        self.publish_joint_trajectory(self.initial_joint_angles)

    def pose_callback(self, msg):
        # Convert ROS Pose to PyKDL Frame
        frame = PyKDL.Frame(
            PyKDL.Rotation.Quaternion(
                msg.orientation.x,
                msg.orientation.y,
                msg.orientation.z,
                msg.orientation.w,
            ),
            PyKDL.Vector(msg.position.x, msg.position.y, msg.position.z),
        )

        # Solve inverse kinematics
        result_angles = PyKDL.JntArray(self.num_joints)
        seed = PyKDL.JntArray(self.num_joints)
        for i in range(self.num_joints):
            seed[i] = self.initial_joint_angles[i]

        if self.ik_solver.CartToJnt(seed, frame, result_angles) >= 0:
            # IK solution found
            solution = [result_angles[i] for i in range(self.num_joints)]
            pid_output = self.apply_pid_control(solution)
            self.publish_joint_trajectory(pid_output)
            self.initial_joint_angles = pid_output  # Update for next step
        else:
            self.get_logger().warn("Failed to find inverse kinematics solution")

    def apply_pid_control(self, target_angles):
        # PID control to minimize the error between current and target joint angles
        pid_output = []
        dt = 0.1  # Assuming a time step of 0.1 seconds (this can be adjusted)

        for i in range(self.num_joints):
            error = target_angles[i] - self.initial_joint_angles[i]
            self.integral_errors[i] += error * dt
            derivative_error = (error - self.previous_errors[i]) / dt

            # PID control law: u(t) = Kp * e(t) + Ki * ∫e(t) dt + Kd * de(t)/dt
            pid_output.append(
                self.initial_joint_angles[i]
                + self.kp[i] * error
                + self.ki[i] * self.integral_errors[i]
                + self.kd[i] * derivative_error
            )

            # Update the previous error for the next iteration
            self.previous_errors[i] = error

        return pid_output

    def publish_joint_trajectory(self, joint_angles):
        msg = JointTrajectory()
        msg.joint_names = self.joints
        point = JointTrajectoryPoint()
        point.positions = (
            joint_angles
            if isinstance(joint_angles, list)
            else [joint_angles[i] for i in range(self.num_joints)]
        )
        point.time_from_start = Duration(sec=2)
        msg.points.append(point)
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = UR5InverseKinematicsController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
