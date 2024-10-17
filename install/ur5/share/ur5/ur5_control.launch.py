import os
import xacro

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
    urdf_file = "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/urdf/ur5_bot.urdf"
    controller_file = "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/config/ur5_control.yaml"
    robot_description = {"robot_description": urdf_file}
    dae_file = "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo/models/conveyor_belt/meshes/conveyor_belt.dae"

    # world_file = "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/worlds/ur5_conveyor.world"  # Update this path to your world file

    # Include Gazebo launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/launch/ur5_gazebo.launch.py"
        ),
    )

    # Process the URDF file with Xacro
    doc = xacro.parse(open(urdf_file))
    xacro.process_doc(doc)
    params = {"robot_description": doc.toxml()}

    # Create Node for robot_state_publisher
    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[params],
    )

    # Create Node for spawning the entity in Gazebo
    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-entity", "ur5", "-b", "-file", urdf_file],
        output="screen",
    )

    # Create ExecuteProcess actions to load controllers
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

    # Add the ExecuteProcess action to launch Gazebo with the specified world file
    # launch_gazebo = ExecuteProcess(
    #     cmd=[
    #         "gazebo",
    #         "--verbose",
    #         "-s",
    #         "libgazebo_ros_factory.so",
    #         "-world",
    #         world_file,
    #     ],
    #     output="screen",
    # )
    launch_gazebo = ExecuteProcess(
        cmd=["gazebo", "--verbose", "-s", "libgazebo_ros_factory.so"], output="screen"
    )

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

    return LaunchDescription(
        [
            # Register event handlers to load controllers sequentially
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
            # Launch Gazebo with the world file
            launch_gazebo,
            gazebo,
            node_robot_state_publisher,
            spawn_dae,
            spawn_entity,
            Node(
                package="controller_manager",
                executable="ros2_control_node",
                parameters=[robot_description, controller_file],
                output="screen",
            ),
        ]
    )
