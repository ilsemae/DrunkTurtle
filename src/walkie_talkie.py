#!/usr/bin/env python

import rospy
import numpy as np
from turtlesim.msg import Pose

def callback(data):
    rospy.set_param('x',data.x)
    rospy.set_param('y',data.y)
    rospy.set_param('theta',data.theta)

def listener():
    rospy.init_node('walkie_talkie',anonymous=True)
    rospy.Subscriber('turtle1/pose',Pose,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
