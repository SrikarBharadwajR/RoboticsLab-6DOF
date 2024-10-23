#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/pose.hpp>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <vector>

int main(int argc, char **argv)
{
    // Initialize ROS2 node
    rclcpp::init(argc, argv);
    auto node = rclcpp::Node::make_shared("motion_plan");

    // Start the MoveIt2 interface for the manipulator group
    moveit::planning_interface::MoveGroupInterface move_group(node, "ur5_arm");

    // Define the joint angles directly in the code
    std::vector<double> joint_angles = { -0.15, 0.1, -0.9, 0.4, -1.57, -0.25 }; // Example joint angles

    // Set the joint target for the MoveIt group
    move_group.setJointValueTarget(joint_angles);

    // Plan the motion
    moveit::planning_interface::MoveGroupInterface::Plan my_plan;
    bool success = (move_group.plan(my_plan) == moveit::core::MoveItErrorCode::SUCCESS); // Updated here

    // Execute the plan if it was successful
    if (success)
    {
        RCLCPP_INFO(node->get_logger(), "Plan found. Executing...");
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
