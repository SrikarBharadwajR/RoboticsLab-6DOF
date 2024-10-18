#!/usr/bin/env python3

import subprocess
import time


def run_command(command, shell=False):
    """Helper function to run a command as a subprocess."""
    return subprocess.Popen(command, shell=shell)


def main():
    # Terminal 1: Launch UR5 control
    t1 = run_command(["ros2", "launch", "ur5", "ur5_control.launch.py"])

    # Sleep to give time for the first command to initialize
    time.sleep(5)

    # Terminal 2: Run Gazebo
    t2 = run_command(["ros2", "run", "ur5", "gz"])

    # Terminal 3: Run gripper control
    t3 = run_command(["ros2", "run", "ur5", "grip"])

    # Terminal 4: Set initial joint angles
    t4 = run_command(
        [
            "ros2",
            "param",
            "set",
            "/trajectory_node",
            "joint_angles",
            "[-0.2, 0.2, -0.95, 0.35, -1.57, 0.0]",
        ]
    )

    # Wait for a short period before activating the gripper
    time.sleep(15)

    # Terminal 4: Activate the vacuum gripper via service call
    t5 = run_command(
        [
            "ros2",
            "service",
            "call",
            "/switch",
            "std_srvs/srv/SetBool",
            '{"data": true}',
        ],
    )

    # Sleep for 2 seconds before moving the arm
    time.sleep(15)

    # Terminal 4: Move arm to new joint positions
    t6 = run_command(
        [
            "ros2",
            "param",
            "set",
            "/trajectory_node",
            "joint_angles",
            "[0.0, 0.0, 1.5, 0.0, 1.5, 0.0]",
        ]
    )

    # Wait for 10 seconds (gripper holding the box)
    time.sleep(30)

    # Terminal 4: Deactivate the vacuum gripper
    t7 = run_command(
        [
            "ros2",
            "service",
            "call",
            "/switch",
            "std_srvs/srv/SetBool",
            '{"data": false}',
        ],
    )


if __name__ == "__main__":
    main()
