import os
import xacro
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Paths to your DAE and URDF files
    dae_file = "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo/models/conveyor_belt/meshes/conveyor_belt.dae"
    urdf_file = "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/urdf/ur5_bot.urdf"

    # Node to spawn the DAE file at specified coordinates
    spawn_dae = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity",
            "dae_model",
            "-file",
            dae_file,
            "-x",
            "0.5",
            "-y",
            "0",
            "-z",
            "-0.25",
        ],
        output="screen",
    )
    doc = xacro.parse(open(urdf_file))
    xacro.process_doc(doc)
    params = {"robot_description": doc.toxml()}

    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[params],
    )

    # Node to spawn the URDF file at the origin
    spawn_urdf = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity",
            "ur5",
            "-file",
            urdf_file,
            "-x",
            "0",
            "-y",
            "0",
            "-z",
            "0",
        ],
        output="screen",
    )

    # Execute Gazebo with a default world (you can specify your own world file here)
    launch_gazebo = ExecuteProcess(
        cmd=["gazebo", "--verbose", "-s", "libgazebo_ros_factory.so"], output="screen"
    )

    return LaunchDescription(
        [
            launch_gazebo,
            node_robot_state_publisher,
            spawn_urdf,
            spawn_dae,
        ]
    )
