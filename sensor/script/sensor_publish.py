#!/usr/bin/env python
import rospy
from common_msgs.msg import com
from common_msgs.srv import SelfService, SelfServiceRequest

rospy.init_node("sensor_publisher")
pub = rospy.Publisher("sensor_msg", com, queue_size=1)
rospy.wait_for_service("selfservice")
requester = rospy.ServiceProxy("selfservice", SelfService)
msg = com()
rate = rospy.Rate(1)

while not rospy.is_shutdown():
	msg.lidar_data += 0.72168
	msg.bool.data = msg.lidar_data % 2
	msg.vector.x += 0.05187
	msg.vector.y -= 0.02658
	msg.vector.z = 0
	req = SelfServiceRequest(vector_x=msg.vector.x, vector_y=msg.vector.y, vector_z=msg.vector.z)
	res = requester(req)
	print "request:", req.vector_x, req.vector_y, req.vector_z, "response:", res.sum

	pub.publish(msg)
	rospy.loginfo(msg)
	rate.sleep()
