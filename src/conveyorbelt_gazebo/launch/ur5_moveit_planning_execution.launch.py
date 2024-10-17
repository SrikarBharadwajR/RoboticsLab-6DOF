from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
    # Launch arguments
    use_sim_time = LaunchConfiguration("use_sim_time", default="false")
    robot_description_file = LaunchConfiguration(
        "robot_description_file",
        default="/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo/urdf/box.urdf",
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_sim_time",
                default_value="false",
                description="Use simulation time if true",
            ),
            DeclareLaunchArgument(
                "robot_description_file",
                default_value="/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo/urdf/box.urdf",
                description="Full path to the URDF file",
            ),
            # Robot state publisher for UR5 URDF model
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                output="screen",
                parameters=[
                    {
                        "use_sim_time": use_sim_time,
                        "robot_description": LaunchConfiguration(
                            "robot_description_file"
                        ),
                    }
                ],
            ),
            # MoveIt2 Planning Scene Node
            Node(
                package="moveit_ros_planning",
                executable="planning_scene_monitor",
                output="screen",
                parameters=[
                    {
                        "robot_description": LaunchConfiguration(
                            "robot_description_file"
                        ),
                        "use_sim_time": use_sim_time,
                    }
                ],
            ),
            # MoveIt2 Move Group node
            Node(
                package="moveit_ros_move_group",
                executable="move_group",
                output="screen",
                parameters=[
                    {
                        "robot_description": LaunchConfiguration(
                            "robot_description_file"
                        ),
                        "robot_description_semantic": LaunchConfiguration(
                            "robot_description_semantic_file"
                        ),
                        "use_sim_time": use_sim_time,
                    }
                ],
            ),
            # RViz2 with MoveIt2 Motion Planning
            Node(
                package="rviz2",
                executable="rviz2",
                output="screen",
                arguments=[
                    "-d",
                    "<path_to_moveit_rviz_config>.rviz",
                ],  # Replace with the path to your RViz config file
                parameters=[
                    {
                        "use_sim_time": use_sim_time,
                        "robot_description": LaunchConfiguration(
                            "robot_description_file"
                        ),
                        "robot_description_semantic": LaunchConfiguration(
                            "robot_description_semantic_file"
                        ),
                    }
                ],
            ),
        ]
    )
