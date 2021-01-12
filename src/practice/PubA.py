#!/usr/bin/env python

import rospy

from std_msgs.msg import String

rospy.init_node('node_A')

pub0 = rospy.Publisher('good',String,queue_size=10)
rate = rospy.Rate(2)

word = "number"
while not rospy.is_shutdown():
    pub0.publish(word)
    rate.sleep()
