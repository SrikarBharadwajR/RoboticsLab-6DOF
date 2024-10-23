from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os


def generate_launch_description():

    return LaunchDescription(
        [
            Node(
                package="ur5",  # Replace with your package name
                executable="motion_plan",  # C++ executable name
                name="motion_plan",
                output="screen",
            ),
        ]
    )
