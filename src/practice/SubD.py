#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32

def callback(msg):
    print msg.data

rospy.init_node('node_D')
sub = rospy.Subscriber('Liam',Int32, callback)
rospy.spin()