#!/usr/bin/env python

import rospy

from std_msgs.msg import String
from std_msgs.msg import Int32

def callback(msg):
    print msg.data

rospy.init_node('node_C')

sub = rospy.Subscriber('good',String, callback)
sub = rospy.Subscriber('luck1',Int32, callback)  
sub = rospy.Subscriber('luck2',Int32, callback)
pub3 = rospy.Publisher('Liam',Int32,queue_size=10)
rate = rospy.Rate(4)
count3 = 3
while not rospy.is_shutdown():
    pub3.publish(count3)
    rate.sleep()