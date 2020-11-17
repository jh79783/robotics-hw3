#!/usr/bin/env python
import rospy
from common_msgs.msg import com

def callback(msg):
	if msg.bool.data:
		rospy.loginfo("route set success")
	else:
		msg.vector.x = 0
		msg.vector.y = 0
		msg.vector.z = 1.0
		msg.lidar_data += 50
		rospy.loginfo("route set fail")




rospy.init_node("process_sub")
sub = rospy.Subscriber("sensor_msg", com, callback)
rospy.spin()
