#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/pose.hpp>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>

int main(int argc, char **argv)
{
    // Initialize ROS2 node
    rclcpp::init(argc, argv);
    auto node = rclcpp::Node::make_shared("motion_plan");

    // Start the MoveIt2 interface for the manipulator group
    moveit::planning_interface::MoveGroupInterface move_group(node, "manipulator");

    // Create a target pose
    geometry_msgs::msg::Pose target_pose;
    target_pose.position.x = 0.4;
    target_pose.position.y = 0.2;
    target_pose.position.z = 0.6;
    target_pose.orientation.x = 0.0;
    target_pose.orientation.y = 0.0;
    target_pose.orientation.z = 0.0;
    target_pose.orientation.w = 1.0;

    // Set the target pose for the MoveIt group
    move_group.setPoseTarget(target_pose);

    // Plan the motion
    moveit::planning_interface::MoveGroupInterface::Plan my_plan;
    bool success = (move_group.plan(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);

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

    // Clear the pose targets to reset MoveIt
    move_group.clearPoseTargets();

    // Shutdown the node
    rclcpp::shutdown();
    return 0;
}
