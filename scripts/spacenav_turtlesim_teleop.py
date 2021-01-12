#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rate_vel   = 5.0
rate_steer = 5.0
vel = 0.0
steer = 0.0

def spacenav_joy_callback(_joy):
	global vel, steer
	vel   = _joy.linear.x * rate_vel
	steer = _joy.angular.z * rate_steer

rospy.init_node('spacenav_teleop_node')
tw = Twist()
sub = rospy.Subscriber('spacenav/twist', Twist, spacenav_joy_callback)
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 1)
rate = rospy.Rate(30)

while not rospy.is_shutdown():
	tw.linear.x  = vel 
	tw.angular.z = steer 
	pub.publish(tw)
	rate.sleep()

