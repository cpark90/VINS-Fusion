#!/usr/bin/env python

import rospy
import tf
from sensor_msgs.msg import Imu

def imu_callback(data):

    data.orientation.x = 0 #data.orientation.x
    data.orientation.y = 0 #data.orientation.x
    data.orientation.z = 0 #data.orientation.x
    data.orientation.w = 1 #data.orientation.x

    # angular velocity
    # data.angular_velocity.x = -data.angular_velocity.x
    # data.angular_velocity.y = -data.angular_velocity.y
    # data.angular_velocity.z = -data.angular_velocity.z

    # Negate Y-axis for linear acceleration
    data.linear_acceleration.x = -data.linear_acceleration.x
    data.linear_acceleration.y = -data.linear_acceleration.y
    data.linear_acceleration.z = -data.linear_acceleration.z

    # Publish the transformed IMU data
    imu_transformed_pub.publish(data)


rospy.init_node('imu_frame_changer')
imu_sub = rospy.Subscriber('/mavros/imu/data', Imu, imu_callback)
imu_transformed_pub = rospy.Publisher('/imu/data_transformed', Imu, queue_size=10)

rospy.spin()
