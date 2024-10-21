from setuptools import find_packages, setup
import os
from glob import glob

package_name = "ur5"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name), glob("launch/*")),
        (os.path.join("share", package_name), glob("urdf/*")),
        (os.path.join("share", package_name), glob("config/*")),
        (os.path.join("share", package_name), glob("meshes/*")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="ps",
    maintainer_email="pragyasujitkumar922004@gmil.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    # tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "gz = ur5.controller_fk:main",
            "gz_ik = ur5.controller_ik:main",
            "rviz = ur5.controller_rviz:main",
            "rviz_ik = ur5.controller_rviz_ik:main",
            "cap = ur5.capture_image:main",
            "pose = ur5.pose_publisher:main",
            "grip = ur5.vacuum_gripper_controller:main",
            "prox = ur5.proximity:main",
            "scheduler = ur5.spawn_box_scheduler:main",
            "pnp = ur5.pick_and_place:main",
        ],
    },
)

"""
ros2 param set /trajectory_node joint_angles "[0.0,0.0,1.5,0.0,1.5,0.0]"

ros2 param set /trajectory_node joint_angles "[-0.2,0.2,-0.95,0.35,-1.57,0.0]"

ros2 service call /switch std_srvs/srv/SetBool "{data: true}"
"""
