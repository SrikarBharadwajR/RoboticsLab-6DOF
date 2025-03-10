#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


class TrajectoryPublisher(Node):

    def __init__(self):
        super().__init__("trajectory_node")
        topic_ = "/joint_trajectory_controller/joint_trajectory"
        self.joints = [
            "shoulder_pan_joint",
            "shoulder_lift_joint",
            "elbow_joint",
            "wrist_1_joint",
            "wrist_2_joint",
            "wrist_3_joint",
        ]
        self.declare_parameter("joint_angles", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        self.publisher_ = self.create_publisher(JointTrajectory, topic_, 10)
        self.timer_ = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        # Dynamically get the latest joint angles
        self.goal_ = self.get_parameter("joint_angles").value

        msg = JointTrajectory()
        msg.joint_names = self.joints
        point = JointTrajectoryPoint()
        point.positions = self.goal_
        point.time_from_start = Duration(sec=2)  # Correct Duration initialization
        msg.points.append(point)
        self.publisher_.publish(msg)
        # self.get_logger().info("Published trajectory point: %s" % str(point))


def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
