import os
from launch import LaunchDescription
from launch.actions import (
    ExecuteProcess,
    IncludeLaunchDescription,
    RegisterEventHandler,
)
from launch_ros.actions import Node
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    urdf_file_path = "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/urdf/ur5_bot.urdf"
    controller_file_path = "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/config/ur5_control.yaml"

    # Load URDF file
    with open(urdf_file_path, "r") as infp:
        robot_description_content = infp.read()

    # Set robot_description parameter with the URDF content
    robot_description = {"robot_description": robot_description_content}

    # Include the Gazebo launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/launch/ur5_world.launch.py"
        ),
    )

    # Node for robot_state_publisher
    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    # Node for spawning the robot in Gazebo
    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-entity", "ur5", "-file", urdf_file_path],
        output="screen",
    )

    # ExecuteProcess to load the joint_state_broadcaster controller
    load_joint_state_controller = ExecuteProcess(
        cmd=[
            "ros2",
            "control",
            "load_controller",
            "--set-state",
            "active",
            "joint_state_broadcaster",
        ],
        output="screen",
    )

    # ExecuteProcess to load the joint_trajectory_controller controller
    load_joint_trajectory_controller = ExecuteProcess(
        cmd=[
            "ros2",
            "control",
            "load_controller",
            "--set-state",
            "active",
            "joint_trajectory_controller",
        ],
        output="screen",
    )

    # Controller Manager Node (without the robot_description parameter)
    controller_manager_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[controller_file_path],
        output="screen",
    )

    load_forward_kinematics_solver = ExecuteProcess(
        cmd=[
            "ros2",
            "run",
            "ur5",
            "gz",
        ],
        output="screen",
    )

    load_camera_capture = ExecuteProcess(
        cmd=[
            "ros2",
            "run",
            "ur5",
            "cap",
        ],
        output="screen",
    )

    # Register event handlers to load controllers after the robot is spawned
    return LaunchDescription(
        [
            gazebo,
            node_robot_state_publisher,
            spawn_entity,
            RegisterEventHandler(
                event_handler=OnProcessExit(
                    target_action=spawn_entity,
                    on_exit=[load_joint_state_controller],
                )
            ),
            RegisterEventHandler(
                event_handler=OnProcessExit(
                    target_action=load_joint_state_controller,
                    on_exit=[load_joint_trajectory_controller],
                )
            ),
            controller_manager_node,
            load_forward_kinematics_solver,
            load_camera_capture,
        ]
    )
