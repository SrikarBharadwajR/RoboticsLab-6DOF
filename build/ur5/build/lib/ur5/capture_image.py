import rclpy
import cv2
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import time


class Capture(Node):
    def __init__(self):
        super().__init__("image_subscriber")
        self.subscriber = self.create_subscription(
            Image, "/camera1/image_raw", self.process_data, 10
        )
        self.bridge = CvBridge()
        self.image_count = 0  # Counter for captured images

    def process_data(self, data):
        try:
            # Convert ROS image message to OpenCV format
            frame = self.bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")

            # If it's a depth image, normalize for visualization (if needed)
            if len(frame.shape) == 2:  # Likely a depth image
                frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

            # Save the captured image with a unique filename
            image_filename = f"/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/captures/shot.png"
            cv2.imwrite(image_filename, frame)
            
            # self.get_logger().info(f"Image saved")

            # Display the image
            cv2.imshow("Captured Image", frame)
            cv2.waitKey(1)  # Use a short wait time to allow for window refresh

        except Exception as e:
            self.get_logger().error(f"Error processing image: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = Capture()
    rclpy.spin(node)


if __name__ == "__main__":
    main()
