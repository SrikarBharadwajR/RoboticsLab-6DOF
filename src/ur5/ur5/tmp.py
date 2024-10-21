import cv2
import numpy as np
import cv2.aruco as aruco

# Load the image
image = cv2.imread(
    "/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/src/ur5/captures/shot.png"
)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to create a black and white (binary) mask
_, bw_mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Define ArUco dictionary and detector parameters
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
parameters = aruco.DetectorParameters_create()

# Detect markers on the grayscale image (not the black and white one)
corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

# Show the black and white image
cv2.imshow("Black and White Image", bw_mask)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()

# Check if any ArUco markers were detected
if ids is not None:
    aruco_marker_id = ids[0][0]  # ids is a list of arrays, so use [0][0]
    print(f"Detected ArUco marker ID: {aruco_marker_id}")
else:
    print("No ArUco markers detected.")