#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from rclpy.clock import Clock
import sys
import numpy as np
import atexit

class TrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('trajectory_node')

        topic_ = "/joint_states"
        self.joints = [
            'shoulder_pan_joint', 'shoulder_lift_joint', 
            'elbow_joint', 'wrist_1_joint', 
            'wrist_2_joint', 'wrist_3_joint'
        ]

        # Handle command-line arguments
        if len(sys.argv) < 7:
            self.get_logger().error("Not enough arguments provided. Using default values.")
            self.goal_ = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # Default values
        else:
            try:
                self.goal_ = [float(sys.argv[i]) for i in range(1, 7)]
            except ValueError:
                self.get_logger().error("Invalid argument(s) provided. Using default values.")
                self.goal_ = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # Default values

        self.publisher_ = self.create_publisher(JointState, topic_, 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)

        # For interpolation
        self.current_position = [0.0] * len(self.joints)
        self.step_size = 0.01
        self.total_steps = int(1 / self.step_size)
        self.goal_reached = False

        # Register exit handler
        atexit.register(self.hold_final_position)

    def dh_transform(self, theta, d, a, alpha):
        """
        Create the transformation matrix using DH parameters.
        """
        return np.array([
            [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
            [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
            [0, np.sin(alpha), np.cos(alpha), d],
            [0, 0, 0, 1]
        ])

    def forward_kinematics(self, joint_angles):
        """
        Calculate the end-effector pose using the forward kinematics equations.
        """
        # DH parameters for UR5
        d = [0.089159, 0.13585, 0.1197, 0.11665, 0.0922, 0.05715]
        a = [0.425, 0.39225, 0.10915, 0, 0, 0]
        alpha = [-np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2, 0]

        T = np.eye(4)  # Initialize the transformation matrix as identity matrix
        for i in range(6):
            T_i = self.dh_transform(joint_angles[i], d[i], a[i], alpha[i])
            T = np.dot(T, T_i)
        
        return T

    def timer_callback(self):
        msg = JointState()
        current_time = Clock().now().to_msg()

        msg.header.stamp.sec = current_time.sec
        msg.header.stamp.nanosec = current_time.nanosec
        msg.name = self.joints

        if not self.goal_reached:
            # Interpolate each joint position towards the goal
            for i in range(len(self.joints)):
                self.current_position[i] += (self.goal_[i] - self.current_position[i]) * self.step_size

            # Check if the goal is reached
            if all(abs(self.goal_[i] - self.current_position[i]) < 0.01 for i in range(len(self.joints))):
                self.goal_reached = True
                self.get_logger().info("Goal reached. Holding position...")

        msg.position = self.current_position
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing position: {}".format(self.current_position))
        
        # Calculate and log end-effector position using forward kinematics
        end_effector_pose = self.forward_kinematics(self.current_position)
        self.get_logger().info(f"End-effector pose:\n{end_effector_pose}")

    def hold_final_position(self):
        msg = JointState()
        current_time = Clock().now().to_msg()

        msg.header.stamp.sec = current_time.sec
        msg.header.stamp.nanosec = current_time.nanosec
        msg.name = self.joints
        msg.position = self.current_position

        # Publish the final position one more time to ensure it's held
        self.publisher_.publish(msg)
        self.get_logger().info("Final position held: {}".format(self.current_position))

def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
