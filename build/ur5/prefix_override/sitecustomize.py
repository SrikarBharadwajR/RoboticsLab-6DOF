import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/Storage/Documents/MIT/Books/Robotics-2_Lab/Mini_Project/install/ur5'
