#!/usr/bin/env python
import rospy
from original_test.msg import WheelState
from original_test.msg import SensorData
#######################################################################
#SensorDataメッセージを受け取るコールバック関数
def callback(data):
	print(data.sensor_value[0])
#######################################################################


rospy.init_node('wheel_state_pub')
rospy.Subscriber('sensor_data', SensorData, callback)

pub = rospy.Publisher('wheelState', WheelState , queue_size=1)

rate = rospy.Rate(10)
data=WheelState();

#######################################################################
#WheelStateメッセージを送るループ
while not rospy.is_shutdown():
    data.left_wheel_speed=100;

    pub.publish(data)
    rate.sleep()
#######################################################################
