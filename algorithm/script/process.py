#!/usr/bin/env python
import rospy
from common_msgs.msg import com
from common_msgs.srv import SelfService, SelfServiceResponse

def service_callback(request):
	response = SelfServiceResponse(sum=request.vector_x + request.vector_y + request.vector_z)
	print "request:", request.vector_x, request.vector_y, request.vector_z, "response:", response.sum
	return response

def callback(msg):
	if msg.bool.data:
		print "route set success"
	else:
		msg.vector.x = 0
		msg.vector.y = 0
		msg.vector.z = 1.0
		msg.lidar_data += 50
		print "route set fail"




rospy.init_node("process_sub")
sub = rospy.Subscriber("sensor_msg", com, callback)
service = rospy.Service("selfservice", SelfService, service_callback)
rospy.spin()
