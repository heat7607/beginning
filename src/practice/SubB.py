#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32
from std_msgs.msg import Float32


def callback(msg):
    print msg.data

rospy.init_node('node_B')

sub = rospy.Subscriber('good',Int32, callback)

rospy.spin()