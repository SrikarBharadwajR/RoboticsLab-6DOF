import rclpy
from rclpy.node import Node
from sensor_msgs.msg import (
    LaserScan,
)  # Assuming proximity sensor data is in LaserScan format
from conveyorbelt_msgs.srv import ConveyorBeltControl  # Import the service message type
import subprocess


class ProximityMonitor(Node):
    def __init__(self):
        super().__init__("proximity_monitor_node")

        # Subscribe to the /prox topic
        self.subscription = self.create_subscription(
            LaserScan, "/prox", self.listener_callback, 10  # Topic to subscribe to
        )
        self.subscription  # prevent unused variable warning

        # Create a service client for /CONVEYORPOWER
        self.conveyor_power_client = self.create_client(
            ConveyorBeltControl, "/CONVEYORPOWER"
        )

        # Wait for the service to be available
        while not self.conveyor_power_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for /CONVEYORPOWER service...")

    def listener_callback(self, msg):
        distance = msg.ranges[0]  # Assuming a single beam sensor
        self.get_logger().info(f"Detected object at {distance:.2f} meters")

        # Call the conveyor power service
        self.control_conveyor(5)

        # Spawn the box
        self.spawn_box()

    def control_conveyor(self, power):
        # Create a request for the conveyor power service
        request = ConveyorBeltControl.Request()
        request.power = power

        # Call the service asynchronously
        self.get_logger().info(
            "Calling /CONVEYORPOWER service to turn on the conveyor..."
        )
        future = self.conveyor_power_client.call_async(request)

        # Wait for the service call to complete
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info(f"Conveyor powered with {power} units.")
        else:
            self.get_logger().error("Failed to call /CONVEYORPOWER service")

    def spawn_box(self):
        # Spawn a box using SpawnObject.py
        self.get_logger().info("Spawning a box...")
        try:
            subprocess.run(
                [
                    "ros2",
                    "run",
                    "ros2_conveyorbelt",
                    "SpawnObject.py",
                    "--package",
                    "conveyorbelt_gazebo",
                    "--urdf",
                    "box.urdf",
                    "--name",
                    "box",
                    "--x",
                    "-0.5",
                    "--y",
                    "0.0",
                    "--z",
                    "0.76",
                ],
                check=True,
            )
            self.get_logger().info("Box spawned successfully.")
        except subprocess.CalledProcessError as e:
            self.get_logger().error(f"Failed to spawn box: {e}")


def main(args=None):
    rclpy.init(args=args)

    node = ProximityMonitor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
