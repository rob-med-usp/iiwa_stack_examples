#!/usr/bin/env python

import time
from math import pi
import rospy

from iiwa_msgs.msg import CartesianPose
from geometry_msgs.msg import PoseStamped

curr_pos = 0

class listener:
    def __init__(self):
        self.current_pos = None

    def pose_cb(self, data):
        self.current_pos = data
        # print(data)
        # print(data.pose.position)
        # print(type(data))
        # print("\n\n\n")


def pose_subscriber(states):
    pose_sub = rospy.Subscriber('/iiwa/state/CartesianPose', PoseStamped, states.pose_cb)
    # rospy.spin()

def pose_publisher():
    x_0 = PoseStamped()
    x_1 = PoseStamped()
    x_2 = PoseStamped()

    x_0.pose.position.z = 1.3

    x_1.pose.position.x = 0.2
    x_1.pose.position.z = 1.0

    x_2.pose.position.x = -0.2
    x_2.pose.position.z = 1.0

    rate = rospy.Rate(.25) # 0.25 Hz => 4 s

    states = listener()
    pose_subscriber(states)

    while not rospy.is_shutdown():
        rospy.loginfo("Publishing pos x_0: \n{}".format(x_0.pose.position))
        pose_pub.publish(x_0)
        rate.sleep()

        rospy.loginfo("Publishing pos x_1: \n{}".format(x_1.pose.position))
        pose_pub.publish(x_1)
        rate.sleep()

        rospy.loginfo("Publishing pos x_2: \n{}".format(x_2.pose.position))
        pose_pub.publish(x_2)
        rate.sleep()

        rospy.loginfo("Publishing pos x_1: \n{}".format(x_1.pose.position))
        pose_pub.publish(x_1)
        rate.sleep()
        # print("\n\n\n\n x_0: \n", x_0)
        # print("\n\n\n\n x_1: \n", x_1)
        print("\n\n\n\n curr_pos: \n", states.current_pos)

if __name__ == "__main__":

    pose_pub = rospy.Publisher('/iiwa/command/CartesianPose', PoseStamped, queue_size = 10)
    rospy.init_node('joint_pos_ctrl', anonymous=True)

    # pos_init =

    try:
        pose_publisher()
    except KeyboardInterrupt:
        print("Stopping controller...")