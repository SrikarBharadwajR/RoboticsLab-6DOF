#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from builtin_interfaces.msg import Duration


class TrajectoryActionClient(Node):

    def __init__(self):
        super().__init__("trajectory_action_client")

        # Create an action client for the FollowJointTrajectory action
        self._action_client = ActionClient(
            self, FollowJointTrajectory, "/ur5_arm_controller/follow_joint_trajectory"
        )

        # Wait for the action server to become available
        self._action_client.wait_for_server()

        # Send the goal once the action server is available
        self.send_goal()

    def send_goal(self):
        goal_msg = FollowJointTrajectory.Goal()

        # Fill in the trajectory (joint names and points)
        goal_msg.trajectory.joint_names = [
            "shoulder_pan_joint",
            "shoulder_lift_joint",
            "elbow_joint",
            "wrist_1_joint",
            "wrist_2_joint",
            "wrist_3_joint",
        ]

        point = JointTrajectoryPoint()
        point.positions = [0.0, -0.2, 1.7, 0.45, 1.6, 0.0]  # Example joint positions
        point.time_from_start = Duration(sec=5)  # 5 seconds duration

        goal_msg.trajectory.points.append(point)

        # Send the goal asynchronously and attach the result and feedback callbacks
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected :(")
            return

        self.get_logger().info("Goal accepted :)")

        # Wait for the result
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.goal_result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f"Feedback: {feedback_msg.feedback}")

    def goal_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Result: {result}")


def main(args=None):
    rclpy.init(args=args)

    action_client = TrajectoryActionClient()

    try:
        rclpy.spin(action_client)
    except KeyboardInterrupt:
        pass

    action_client.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
