#!/usr/bin/env python
import rospy
from common_msgs.msg import com

rospy.init_node("sensor_publisher")
pub = rospy.Publisher("sensor_msg", com, queue_size=1)
msg = com()
rate = rospy.Rate(1)

while not rospy.is_shutdown():
	msg.lidar_data += 0.72168
	msg.bool.data = msg.lidar_data % 2
	msg.vector.x += 0.05187
	msg.vector.y -= 0.02658
	msg.vector.z = 0

	pub.publish(msg)
	rospy.loginfo(msg)
	rate.sleep()
