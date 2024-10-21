#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from sensor_msgs.msg import JointState
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_srvs.srv import SetBool
import numpy as np
import time
import cv2
import cv2.aruco as aruco

# Define poses
HOME_POSE = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
ARUCO_SCAN_POSE = [-0.15, 0.1, -0.9, 0.4, -1.57, -0.25]
PICK_POSE = [-0.2, 0.2, -0.99, 0.38, -1.57, 0.0]
BOX_1_POSE = [0.3, -0.3, 1.5, 0.1, 1.57, 0.0]
BOX_2_POSE = [0.0, -0.7, 1.0, 0.1, 1.6, 0.0]
BOX_3_POSE = [-0.6, -0.7, 1.0, 0.1, 1.6, 0.0]
BOX_4_POSE = [-0.45, -1.0, 0.5, 0.3, 1.6, 0.0]


class TrajectoryPublisher(Node):

    def __init__(self):
        super().__init__("trajectory_node")
        self.joints = [
            "shoulder_pan_joint",
            "shoulder_lift_joint",
            "elbow_joint",
            "wrist_1_joint",
            "wrist_2_joint",
            "wrist_3_joint",
        ]
        self.goal_ = ARUCO_SCAN_POSE

        self.publisher_ = self.create_publisher(
            JointTrajectory, "/joint_trajectory_controller/joint_trajectory", 10
        )
        self.timer_ = self.create_timer(1, self.timer_callback)

        self.joint_state_subscriber_ = self.create_subscription(
            JointState, "/joint_states", self.joint_state_callback, 10
        )
        self.current_joint_angles_ = [0.0] * 6  # Initialize current joint angles

        self.gripper_client = self.create_client(SetBool, "/switch")
        while not self.gripper_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for the vacuum gripper service...")

        self.aruco_marker_id = None  # Store scanned marker ID

    def joint_state_callback(self, msg):
        joint_positions = []
        for joint_name in self.joints:
            if joint_name in msg.name:
                index = msg.name.index(joint_name)
                joint_positions.append(msg.position[index])

        if len(joint_positions) == 6:
            self.current_joint_angles_ = joint_positions

    def timer_callback(self):
        msg = JointTrajectory()
        msg.joint_names = self.joints
        point = JointTrajectoryPoint()
        point.positions = self.goal_
        point.time_from_start = Duration(sec=2)
        msg.points.append(point)
        self.publisher_.publish(msg)

        self.get_logger().info(f"Moving to pose: {self.goal_}")

        if self.reached_goal(self.current_joint_angles_, self.goal_):
            self.get_logger().info(f"Reached pose: {self.goal_}")

            if self.goal_ == ARUCO_SCAN_POSE:
                self.scan_aruco_marker()
            elif self.goal_ == PICK_POSE:
                self.toggle_gripper(True)
                self.move_to_box_pose()
            elif self.goal_ in [BOX_1_POSE, BOX_2_POSE, BOX_3_POSE, BOX_4_POSE]:
                self.toggle_gripper(False)
                self.goal_ = ARUCO_SCAN_POSE  # Return to scan position
                self.get_logger().info("Returning to ArUco scan pose.")

    def scan_aruco_marker(self):
        # Load the image with the ArUco marker
        # image = cv2.imread(
        #     "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/captures/shot.png"
        # )
        # if image is None:
        #     self.get_logger().error("Could not load shot.png")
        #     return

        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
        # parameters = aruco.DetectorParameters_create()
        # corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        # if ids is not None:
        #     self.aruco_marker_id = ids[0][0]
        #     self.get_logger().info(f"Detected ArUco marker ID: {self.aruco_marker_id}")
        self.goal_ = PICK_POSE
        # else:
        #     cv2.imshow("gray",gray)
        #     cv2.waitKey(1)
        #     cv2.destroyAllWindows()
        #     self.get_logger().error("No ArUco marker detected!")
        self.aruco_marker_id = 1

    def move_to_box_pose(self):
        if self.aruco_marker_id == 1:
            self.goal_ = BOX_1_POSE
        elif self.aruco_marker_id == 2:
            self.goal_ = BOX_2_POSE
        elif self.aruco_marker_id == 3:
            self.goal_ = BOX_3_POSE
        elif self.aruco_marker_id == 4:
            self.goal_ = BOX_4_POSE
        else:
            self.get_logger().error("Invalid ArUco marker ID or no marker detected!")

    def reached_goal(self, current_angles, goal_angles, tolerance=0.01):
        return np.allclose(current_angles, goal_angles, atol=tolerance)

    def toggle_gripper(self, engage):
        request = SetBool.Request()
        request.data = engage
        future = self.gripper_client.call_async(request)
        future.add_done_callback(self.gripper_response_callback)

    def gripper_response_callback(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info(
                    f"Gripper {'engaged' if response.data else 'released'}."
                )
            else:
                self.get_logger().warn(f"Gripper operation failed: {response.message}")
        except Exception as e:
            self.get_logger().error(f"Gripper service call failed: {str(e)}")


def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryPublisher()
    rclpy.spin(node)
    
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
