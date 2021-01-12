#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32

rospy.init_node('node_B')

pub1 = rospy.Publisher('luck1',Int32,queue_size=10)
pub2 = rospy.Publisher('luck2',Int32,queue_size=10)
rate = rospy.Rate(2)

count1 = 1
count2 = 2
while not rospy.is_shutdown():
    pub1.publish(count1)
    pub2.publish(count2)
    rate.sleep()
