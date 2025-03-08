#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/pose.hpp>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <trajectory_msgs/msg/joint_trajectory.hpp>
#include <vector>
#include <cstdlib>

int main(int argc, char **argv)
{
    // Initialize ROS2 node
    rclcpp::init(argc, argv);
    auto node = rclcpp::Node::make_shared("motion_plan");

    // Ensure 6 joint angles are passed as arguments
    if (argc != 7)
    {
        RCLCPP_ERROR(node->get_logger(), "Usage: motion_plan angle1 angle2 angle3 angle4 angle5 angle6");
        rclcpp::shutdown();
        return 1;
    }

    // Parse the joint angles from the command line arguments
    std::vector<double> joint_angles;
    for (int i = 1; i <= 6; ++i)
    {
        joint_angles.push_back(std::atof(argv[i]));
    }

    // Start the MoveIt2 interface for the manipulator group
    moveit::planning_interface::MoveGroupInterface move_group(node, "ur5_arm");

    // Publisher to send the planned trajectory
    auto trajectory_pub = node->create_publisher<trajectory_msgs::msg::JointTrajectory>("/planned_trajectory", 10);

    // Set the joint target for the MoveIt group
    move_group.setJointValueTarget(joint_angles);

    // Plan the motion
    moveit::planning_interface::MoveGroupInterface::Plan my_plan;
    bool success = (move_group.plan(my_plan) == moveit::core::MoveItErrorCode::SUCCESS);

    // Execute the plan if it was successful
    if (success)
    {
        RCLCPP_INFO(node->get_logger(), "Plan found. Executing...");

        // Publish the planned trajectory
        trajectory_pub->publish(my_plan.trajectory_.joint_trajectory);

        // Execute the trajectory locally (in RViz)
        move_group.execute(my_plan);
    }
    else
    {
        RCLCPP_ERROR(node->get_logger(), "Planning failed.");
    }

    // Stop any residual motion
    move_group.stop();

    // Shutdown the node
    rclcpp::shutdown();
    return 0;
}
