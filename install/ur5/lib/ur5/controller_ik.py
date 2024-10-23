#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import numpy as np
import tf_transformations as tf


class UR5IKSolver(Node):
    def __init__(self):
        super().__init__("ur5_ik_solver")

        # Define UR5 DH parameters (a, alpha, d, theta)
        self.dh_params = [
            [0, np.pi / 2, 0.08916, 0],  # base_link to shoulder_link
            [-0.425, 0, 0, 0],  # shoulder_link to upper_arm_link
            [-0.3922, 0, 0, 0],  # upper_arm_link to forearm_link
            [0, np.pi / 2, 0.10915, 0],  # forearm_link to wrist_1_link
            [0, -np.pi / 2, 0.09465, 0],  # wrist_1_link to wrist_2_link
            [0, 0, 0.0823, 0],  # wrist_2_link to wrist_3_link
        ]

    def dh_transformation(self, a, alpha, d, theta):
        """
        Compute individual transformation matrix based on DH parameters.
        """
        return np.array(
            [
                [
                    np.cos(theta),
                    -np.sin(theta) * np.cos(alpha),
                    np.sin(theta) * np.sin(alpha),
                    a * np.cos(theta),
                ],
                [
                    np.sin(theta),
                    np.cos(theta) * np.cos(alpha),
                    -np.cos(theta) * np.sin(alpha),
                    a * np.sin(theta),
                ],
                [0, np.sin(alpha), np.cos(alpha), d],
                [0, 0, 0, 1],
            ]
        )

    def forward_kinematics(self, joint_angles):
        """
        Compute the forward kinematics for the UR5 arm based on joint angles.
        Returns the transformation matrix of the end effector.
        """
        T = np.eye(4)
        
        if len(joint_angles) !=3:
            raise ValueError("Expected 3 joint angles, got {}".format(len(joint_angles)))

        for i in range(3):
            a, alpha, d, _ = self.dh_params[i]
            theta = joint_angles[i]
            T_i = self.dh_transformation(a, alpha, d, theta)
            T = np.dot(T, T_i)  # Multiply transformations

        return T

    def inverse_kinematics(self, target_pose):
        """
        Inverse Kinematics Solver using geometric approach.
        target_pose: [x, y, z, roll, pitch, yaw]
        """
        # Extract position and orientation from target pose
        px, py, pz = target_pose[:3]
        r, p, y = target_pose[3:]

        # Solving for joint 1: base rotation (theta1)
        d1 = self.dh_params[0][2]  # offset from base to shoulder_link
        theta1 = np.arctan2(py, px)

        # Solve for wrist center position (Px, Py, Pz)
        wrist_z_offset = self.dh_params[5][2]  # wrist_3_link offset
        wrist_center_x = px - wrist_z_offset * np.cos(theta1)
        wrist_center_y = py - wrist_z_offset * np.sin(theta1)
        wrist_center_z = pz - d1

        # Distance from shoulder to wrist center (r)
        r = np.sqrt(wrist_center_x**2 + wrist_center_y**2)

        # Solving for joint 2 and 3: shoulder and elbow angles (theta2, theta3)
        a2 = -self.dh_params[1][0]  # length of upper_arm_link
        a3 = -self.dh_params[2][0]  # length of forearm_link

        cos_theta3 = (r**2 + wrist_center_z**2 - a2**2 - a3**2) / (2 * a2 * a3)
        theta3 = np.arccos(np.clip(cos_theta3, -1.0, 1.0))  # Elbow joint

        s3 = np.sin(theta3)
        k1 = a2 + a3 * np.cos(theta3)
        k2 = a3 * s3
        theta2 = np.arctan2(wrist_center_z, r) - np.arctan2(k2, k1)  # Shoulder joint

        # Solve for wrist joints (theta4, theta5, theta6) based on orientation
        R03 = self.forward_kinematics([theta1, theta2, theta3])[:3, :3]
        R36 = np.dot(np.linalg.inv(R03), tf.euler_matrix(r, p, y)[:3, :3])

        theta4 = np.arctan2(R36[2, 1], R36[2, 2])
        theta5 = np.arctan2(np.sqrt(R36[2, 1] ** 2 + R36[2, 2] ** 2), R36[2, 0])
        theta6 = np.arctan2(R36[1, 0], -R36[0, 0])

        return [theta1, theta2, theta3, theta4, theta5, theta6]

    def compute_ik(self, target_pose):
        joint_angles = self.inverse_kinematics(target_pose)

        if joint_angles is not None:
            return joint_angles
        else:
            self.get_logger().error("IK Solver failed")
            return None


def main(args=None):
    rclpy.init(args=args)
    ik_solver = UR5IKSolver()

    # Example target pose (X, Y, Z, Roll, Pitch, Yaw)
    target_pose = [0.11325, 0.48885, 0.50805, 0.0, 0.0, 0.0]

    joint_angles = ik_solver.compute_ik(target_pose)
    if joint_angles is not None:
        print("Solved joint angles:", joint_angles)

    rclpy.spin(ik_solver)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
