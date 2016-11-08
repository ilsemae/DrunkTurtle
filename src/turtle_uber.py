#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3


def talker():

    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtle_uber', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():

	t = rospy.Time.now().secs

	if rospy.get_param('stumble_style')=="sway":
	    
	    if rospy.get_param('x')>=11 or rospy.get_param('x')==0 or rospy.get_param('y')>=11 or rospy.get_param('y')==0:

		if rospy.get_param('x')>=11:
		    desired_theta = np.pi

		elif rospy.get_param('x')==0:
		    desired_theta = 0

		elif rospy.get_param('y')>=11:
		    desired_theta = 3*np.pi/2

		elif rospy.get_param('y')==0:
		    desired_theta = np.pi/2
		while rospy.get_param('theta') < desired_theta - np.pi/6 or rospy.get_param('theta') > desired_theta + np.pi/6:
		    ang = Vector3(0,0,1)
		    lin = Vector3(0,0,0)
		    stumble = Twist(lin,ang)
        	    pub.publish(stumble)
		    rate.sleep()
		ang = Vector3(0,0,0)
		lin = Vector3(.5,0,0)
		stumble = Twist(lin,ang)
        	pub.publish(stumble)
		rate.sleep()
		
	    else:
	        lin = Vector3(1,0,0)
	        ang = Vector3(0,0,np.pi*np.sin(2*t))
		stumble = Twist(lin,ang)
            	pub.publish(stumble)
            	rate.sleep()

	else:
	    lin = Vector3(np.random.rand(1,1)[0][0],0,0)
	    ang = Vector3(0,0,(np.random.choice([-1,1],1)[0])*3*np.random.rand(1,1)[0][0])
            stumble = Twist(lin,ang)
            pub.publish(stumble)
            rate.sleep()



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
