#!/usr/bin/env python3

import argparse
import os
import xacro
import rclpy
from gazebo_msgs.srv import SpawnEntity

# Function to spawn object into Gazebo
def spawn_object(urdf_file, name, x, y, z, node, client):
    request = SpawnEntity.Request()
    request.name = name

    # Process the URDF file using xacro
    xacro_file = xacro.process_file(urdf_file)
    request.xml = xacro_file.toxml()

    # Set the position for the object
    request.initial_pose.position.x = x
    request.initial_pose.position.y = y
    request.initial_pose.position.z = z

    # Call the service to spawn the object
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
        node.get_logger().info(f'Object "{name}" spawned successfully!')
    else:
        node.get_logger().error(f"Failed to spawn object: {future.exception()}")


def main():
    # Command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Spawn an object into the Gazebo world."
    )
    parser.add_argument(
        "--urdf", type=str, required=True, help="Path to the URDF file."
    )
    parser.add_argument(
        "--name", type=str, default="object", help="Name of the object to spawn."
    )
    parser.add_argument(
        "--x", type=float, default=0.0, help="X position of the object."
    )
    parser.add_argument(
        "--y", type=float, default=0.0, help="Y position of the object."
    )
    parser.add_argument(
        "--z", type=float, default=0.0, help="Z position of the object."
    )

    args = parser.parse_args()

    # Initialize ROS 2 client
    rclpy.init()
    node = rclpy.create_node("entity_spawner")
    client = node.create_client(SpawnEntity, "/spawn_entity")

    # Wait until the spawn_entity service is available
    node.get_logger().info("Waiting for /spawn_entity service...")
    client.wait_for_service()

    # Log information about the spawning process
    node.get_logger().info(
        f'Spawning "{args.name}" at position: ({args.x}, {args.y}, {args.z})'
    )

    # Call the function to spawn the object
    try:
        spawn_object(args.urdf, args.name, args.x, args.y, args.z, node, client)
    except Exception as e:
        node.get_logger().error(f"Error spawning object: {str(e)}")

    # Shutdown the node
    node.get_logger().info("Shutting down spawn_object node.")
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
