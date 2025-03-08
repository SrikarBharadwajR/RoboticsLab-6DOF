# Install script for directory: /mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/install/ur5")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5" TYPE DIRECTORY FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/launch")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5" TYPE DIRECTORY FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/config")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5" TYPE DIRECTORY FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/urdf")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5" TYPE DIRECTORY FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/meshes")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ur5/motion_plan" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ur5/motion_plan")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ur5/motion_plan"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ur5" TYPE EXECUTABLE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/motion_plan")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ur5/motion_plan" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ur5/motion_plan")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ur5/motion_plan"
         OLD_RPATH "/opt/ros/humble/lib/x86_64-linux-gnu:/opt/ros/humble/lib:/opt/ros/humble/opt/rviz_ogre_vendor/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ur5/motion_plan")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ur5" TYPE PROGRAM FILES
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/controller_fk.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/controller_ik.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/controller_rviz.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/controller_rviz_ik.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/capture_image.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/pose_publisher.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/vacuum_gripper_controller.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/proximity.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/spawn_box_scheduler.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/pick_and_place.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/moveit2_control.py"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/ur5/gazebo_comm.py"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/ur5")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/ur5")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5/environment" TYPE FILE FILES "/opt/ros/humble/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5/environment" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5/environment" TYPE FILE FILES "/opt/ros/humble/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5/environment" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_environment_hooks/path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_environment_hooks/local_setup.bash")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_environment_hooks/local_setup.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_environment_hooks/package.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_index/share/ament_index/resource_index/packages/ur5")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5/cmake" TYPE FILE FILES
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_core/ur5Config.cmake"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/ament_cmake_core/ur5Config-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ur5" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/ur5/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
