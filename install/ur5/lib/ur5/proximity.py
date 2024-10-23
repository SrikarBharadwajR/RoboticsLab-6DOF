#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from time import sleep

class ProximitySensorNode(Node):
    def __init__(self):
        super().__init__("proximity_sensor_node")
        # Subscribe to the sensor topic
        self.subscription = self.create_subscription(
            LaserScan,
            "/prox",  # This is the topic where the sensor data is published
            self.listener_callback,
            10,
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # LaserScan contains a list of range readings; since our sensor has one beam, we take the first value
        distance = msg.ranges[0]
        if distance < msg.range_max:
            self.get_logger().info(f"Object detected at {distance:.3f} meters")
        # else:
        #     self.get_logger().info("No object detected")
        sleep(0.5)


def main(args=None):
    rclpy.init(args=args)
    node = ProximitySensorNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
