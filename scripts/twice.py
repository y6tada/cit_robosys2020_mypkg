#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0

def callback(message):
	global n
	n = message.data * 2

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, callback)
pub = rospy.Publisher('twice', Int32, queue_size = 1)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
	pub.publish(n)
	rate.sleep()

