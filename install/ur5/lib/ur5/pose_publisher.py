#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose


class PosePublisher(Node):
    def __init__(self):
        super().__init__("pose_publisher")
        self.publisher_ = self.create_publisher(Pose, "/desired_pose", 10)
        timer_period = 2.0  # seconds
        self.timer = self.create_timer(timer_period, self.publish_pose)

    def publish_pose(self):
        msg = Pose()

        # Set the position
        msg.position.x = 0.11325
        msg.position.y = 0.48885
        msg.position.z = 0.50805

        # Set the orientation (quaternion)
        msg.orientation.x = -0.50022
        msg.orientation.y = -0.53391
        msg.orientation.z = 0.46324
        msg.orientation.w = 0.50013

        self.publisher_.publish(msg)
        self.get_logger().info(
            "Publishing desired pose: position (x: %f, y: %f, z: %f), orientation (x: %f, y: %f, z: %f, w: %f)"
            % (
                msg.position.x,
                msg.position.y,
                msg.position.z,
                msg.orientation.x,
                msg.orientation.y,
                msg.orientation.z,
                msg.orientation.w,
            )
        )


def main(args=None):
    rclpy.init(args=args)
    pose_publisher = PosePublisher()
    rclpy.spin(pose_publisher)
    pose_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
