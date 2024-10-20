import rospy
from geometry_msgs.msg import Pose, PoseStamped
from urdf_parser_py import Robot
from kdl import Chain, ChainJntToCart, ChainIkSolverVel_pinv, ChainIkSolverPos_LMA


def ik_solver(urdf_file, target_pose):
    # Load the URDF model
    robot = Robot.from_xml_file(urdf_file)

    # Get the KDL tree and chain
    tree = robot.to_kdl()
    chain = tree.getChain(
        "base_link", "wrist_3_link"
    )  # Replace with your end-effector link

    # Create KDL solvers
    jnt_to_cart = ChainJntToCart(chain)
    ik_vel = ChainIkSolverVel_pinv(chain)
    ik_pos = ChainIkSolverPos_LMA(chain, 1e-6)  # Adjust tolerance as needed

    # Initialize joint positions
    q_init = [0.0] * chain.getNrOfJoints()

    # Convert target pose to KDL frame
    kdl_target = KDL.Frame()
    kdl_target.p = KDL.Vector(
        target_pose.pose.position.x,
        target_pose.pose.position.y,
        target_pose.pose.position.z,
    )
    kdl_target.M = KDL.Rotation.Quaternion(
        target_pose.pose.orientation.x,
        target_pose.pose.orientation.y,
        target_pose.pose.orientation.z,
        target_pose.pose.orientation.w,
    )

    # Solve IK
    q_out = KDL.JntArray(chain.getNrOfJoints())
    res = ik_pos.solve(kdl_target, q_init, q_out)

    if res >= 0:
        return q_out
    else:
        rospy.logerr("IK solution not found")
        return None


def callback(pose_msg):
    # Get the target pose from the message
    target_pose = pose_msg

    # Solve IK
    joint_positions = ik_solver(urdf_file, target_pose)

    if joint_positions is not None:
        # Publish joint positions to a topic (e.g., /joint_commands)
        joint_positions_msg = JointState()
        joint_positions_msg.header.stamp = rospy.Time.now()
        joint_positions_msg.name = [
            "shoulder_pan_joint",
            "shoulder_lift_joint",
            "elbow_joint",
            "wrist_1_joint",
            "wrist_2_joint",
            "wrist_3_joint",
        ]  # Replace with your joint names
        joint_positions_msg.position = joint_positions
        joint_positions_pub.publish(joint_positions_msg)


if __name__ == "__main__":
    rospy.init_node("ur5_ik_controller")

    # Replace with your URDF file path
    urdf_file = "/path/to/your/urdf/file.urdf"

    # Create a publisher for joint commands
    joint_positions_pub = rospy.Publisher("/joint_commands", JointState, queue_size=10)

    # Create a subscriber for the target pose topic
    rospy.Subscriber("/target_pose", PoseStamped, callback)

    rospy.spin()
