cmake_minimum_required(VERSION 3.8)
project(ur5)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(rviz2 REQUIRED)
find_package(controller_manager REQUIRED)

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

ament_package()
