# Install script for directory: /mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/install/conveyorbelt_gazebo")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo" TYPE DIRECTORY FILES
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo/launch"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo/models"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo/worlds"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo/urdf"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/conveyorbelt_gazebo")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/conveyorbelt_gazebo")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo/environment" TYPE FILE FILES "/opt/ros/humble/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo/environment" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo/environment" TYPE FILE FILES "/opt/ros/humble/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo/environment" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_environment_hooks/path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_environment_hooks/local_setup.bash")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_environment_hooks/local_setup.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_environment_hooks/package.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_index/share/ament_index/resource_index/packages/conveyorbelt_gazebo")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo/cmake" TYPE FILE FILES
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_core/conveyorbelt_gazeboConfig.cmake"
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/ament_cmake_core/conveyorbelt_gazeboConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/conveyorbelt_gazebo" TYPE FILE FILES "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/build/conveyorbelt_gazebo/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")