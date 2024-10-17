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

        # Create KDL chain
        self.chain = PyKDL.Chain()
        # Add segments to the chain (you may need to adjust these values for your UR5 model)
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
            self.chain,
            PyKDL.JntArray(self.num_joints),
            PyKDL.JntArray(self.num_joints),
            self.fk_solver,
            self.ik_v_solver,
            100,
            1e-6,
        )

        # Declare and get the joint_angles parameter
        self.declare_parameter(
            "joint_angles", [0.0, -np.pi / 2, 0.0, -np.pi / 2, 0.0, 0.0]
        )
        self.initial_joint_angles = self.get_parameter("joint_angles").value

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
            self.publish_joint_trajectory(solution)
            self.initial_joint_angles = (
                solution  # Update initial angles for next optimization
            )
        else:
            self.get_logger().warn("Failed to find inverse kinematics solution")

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
