#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_srvs.srv import SetBool
import numpy as np
import time


class TrajectoryFollower(Node):

    def __init__(self):
        super().__init__("trajectory_follower_node")
        self.joints = [
            "shoulder_pan_joint",
            "shoulder_lift_joint",
            "elbow_joint",
            "wrist_1_joint",
            "wrist_2_joint",
            "wrist_3_joint",
        ]

        # Publisher for sending the trajectory to the UR5 controller in Gazebo
        self.publisher_ = self.create_publisher(
            JointTrajectory, "/joint_trajectory_controller/joint_trajectory", 10
        )

        # Subscriber to the planned trajectory from the MoveIt2 node
        self.create_subscription(
            JointTrajectory, "/planned_trajectory", self.trajectory_callback, 10
        )

        self.current_joint_angles_ = [0.0] * 6  # Initialize current joint angles
        self.joint_state_subscriber_ = self.create_subscription(
            JointState, "/joint_states", self.joint_state_callback, 10
        )

    def trajectory_callback(self, msg):
        """Callback to handle received planned trajectory and send it to Gazebo"""
        self.get_logger().info(
            f"Received trajectory with {len(msg.points)} points. Executing in Gazebo..."
        )
        self.publisher_.publish(msg)

    def joint_state_callback(self, msg):
        """Callback to update current joint angles"""
        joint_positions = []
        for joint_name in self.joints:
            if joint_name in msg.name:
                index = msg.name.index(joint_name)
                joint_positions.append(msg.position[index])

        if len(joint_positions) == 6:
            self.current_joint_angles_ = joint_positions

    def reached_goal(self, current_angles, goal_angles, tolerance=0.01):
        return np.allclose(current_angles, goal_angles, atol=tolerance)


def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
