cmake_minimum_required(VERSION 3.8)
project(ur5)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(rviz2 REQUIRED)
find_package(controller_manager REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(moveit_core REQUIRED)
find_package(moveit_visual_tools REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)

# Install launch files
install(
  DIRECTORY
    launch
  DESTINATION
    share/${PROJECT_NAME}
)

# Install config files
install(
  DIRECTORY
    config
  DESTINATION
    share/${PROJECT_NAME}
)

# Install URDF files
install(
  DIRECTORY
    urdf
  DESTINATION
    share/${PROJECT_NAME}
)

# Install mesh files
install(
  DIRECTORY
    meshes
  DESTINATION
    share/${PROJECT_NAME}
)

# Add executable for motion_plan
add_executable(motion_plan src/motion_plan.cpp)

# Link against the required dependencies
ament_target_dependencies(motion_plan
  rclcpp
  geometry_msgs
  moveit_core
  moveit_visual_tools
  moveit_ros_planning_interface
)

# Install the executable
install(TARGETS
  motion_plan
  DESTINATION lib/${PROJECT_NAME})

# Install Python scripts
install(PROGRAMS
  ur5/controller_fk.py
  ur5/controller_ik.py
  ur5/controller_rviz.py
  ur5/controller_rviz_ik.py
  ur5/capture_image.py
  ur5/pose_publisher.py
  ur5/vacuum_gripper_controller.py
  ur5/proximity.py
  ur5/spawn_box_scheduler.py
  ur5/pick_and_place.py
  ur5/moveit2_control.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
