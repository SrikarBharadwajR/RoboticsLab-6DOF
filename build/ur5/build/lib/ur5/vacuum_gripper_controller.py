#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
from std_msgs.msg import Bool


class MultiVacuumGripperController(Node):

    def __init__(self):
        super().__init__("multi_vacuum_gripper_controller")

        # Publishers for the four vacuum grippers
        self.gripper_publishers = [
            self.create_publisher(Bool, "/grasping1", 10),
            # self.create_publisher(Bool, "/grasping2", 10),
            # self.create_publisher(Bool, "/grasping3", 10),
            # self.create_publisher(Bool, "/grasping4", 10),
        ]

        # Create a service to control all vacuum grippers
        self.srv = self.create_service(SetBool, "/switch", self.switch_callback)

        # Log that the service is ready
        self.get_logger().info("Multi Vacuum Gripper Switch Service is ready.")

    def switch_callback(self, request, response):
        # Create the message to publish (True for engage, False for release)
        msg = Bool()
        msg.data = request.data

        # Publish the state to all four grippers
        # self.gripper_publishers.publish(msg)
        self.get_logger().info(
            f"Gripper 1 {'engaged' if request.data else 'released'}."
        )

        # Respond to the service request
        response.success = True
        response.message = "All vacuum grippers have been " + (
            "engaged." if request.data else "released."
        )

        return response


def main(args=None):
    rclpy.init(args=args)

    # Create the node and spin
    vacuum_gripper_controller = MultiVacuumGripperController()
    rclpy.spin(vacuum_gripper_controller)

    # Shutdown after node is done
    vacuum_gripper_controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
