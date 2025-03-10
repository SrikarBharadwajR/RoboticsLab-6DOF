#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from conveyorbelt_msgs.srv import ConveyorBeltControl
import subprocess
import time


box_counter = 0
box_spawned = False

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
        while not self.conveyor_power_client.wait_for_service(timeout_sec=100.0):
            self.get_logger().info("Waiting for /CONVEYORPOWER service...")

        ProximityMonitor.spawn_box(self)
        self.start_time = time.time()


    def listener_callback(self, msg):
        global box_spawned
        current_time = time.time()
        distance = msg.ranges[0]  # Assuming a single beam sensor
        elapsed_time = current_time - self.start_time            
        # self.get_logger().info(f"Elapsed Time: {elapsed_time}")

        if distance < 0.4 :
            self.control_conveyor(0.0)

            # self.get_logger().info(f"Detected object at {distance:.2f} meters")
            if(not box_spawned and elapsed_time >= 25.0):
                self.spawn_box()            
                self.start_time = time.time()

            box_spawned = True


        else:
            box_spawned = False
            self.control_conveyor(10.0)

    def control_conveyor(self, power):
        # Create a request for the conveyor power service
        request = ConveyorBeltControl.Request()
        request.power = float(power)

        self.conveyor_power_client.call_async(request)
        # self.get_logger().info(f"Conveyor powered with {power} units.")

    def spawn_box(self):
        global box_counter
        # Spawn a box using SpawnObject.py
        self.get_logger().info("Spawning a box...")
        try:
            subprocess.run(
                [
                    "ros2",
                    "run",
                    "ros2_conveyorbelt",
                    "SpawnObject.py",
                    "--urdf",
                    f"/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/conveyorbelt_gazebo/urdf/box_{(box_counter%4)+1}.urdf",
                    "--name",
                    f"box_{box_counter+1}",
                    "--x",
                    "-0.5",
                    "--y",
                    "0.55",
                    "--z",
                    "0.76",
                ],
            )
            self.get_logger().info(f"Box_{box_counter+1} spawned successfully.")
            box_counter += 1
        except subprocess.CalledProcessError as e:
            self.get_logger().error(f"Failed to spawn box: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = ProximityMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    time.sleep(1)
    main()
