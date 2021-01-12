#! /usr/bin/env python  
import rospy
from std_msgs.msg import Int32, Float32
from math import *

import math
import time
import serial
import struct

def printing(data)
    print("steer:", data.data)

if __name__=='__main__':
    rospy.init_node('sub_steer')
    sub_steer = rospy.Subscriber('ERP42_steer', Float32, printing ,queue_size=10)
    