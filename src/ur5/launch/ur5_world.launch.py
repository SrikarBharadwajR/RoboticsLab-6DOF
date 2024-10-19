import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    urdf = "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/urdf/ur5_bot.urdf"
    world_file = "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/worlds/world_final.world"  # Path to your world file

    return LaunchDescription(
        [
            # Node to publish the robot state (robot_description) using the URDF
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                arguments=[urdf],
            ),
            # Joint State Publisher node
            Node(
                package="joint_state_publisher",
                executable="joint_state_publisher",
                name="joint_state_publisher",
                arguments=[urdf],
            ),
            # Launch Gazebo with the provided world file (UR5 is already inside the world file)
            ExecuteProcess(
                cmd=[
                    "gazebo",
                    "--verbose",
                    "-s",
                    "libgazebo_ros_factory.so",
                    "-world",
                    world_file,
                ],
                output="screen",
            ),
        ]
    )
