#!/usr/bin/env python
import rospy
import tf2_ros
import tf_conversions
from sensor_msgs.msg import Imu

def imu_callback(imu_msg):
    # Get the quaternion from the IMU message
    quat = imu_msg.orientation

    # Create a TransformStamped message
    tf_msg = tf2_ros.TransformStamped()
    tf_msg.header.stamp = rospy.Time.now()
    tf_msg.header.frame_id = 'imu_base_link' # Parent frame, change if needed
    tf_msg.child_frame_id = 'imu_frame' # Child frame, change if needed

    # Copy the quaternion to the TransformStamped message
    tf_msg.transform.rotation.x = quat.x
    tf_msg.transform.rotation.y = quat.y
    tf_msg.transform.rotation.z = quat.z
    tf_msg.transform.rotation.w = quat.w

    # Broadcast the transform
    tf_broadcaster.sendTransform(tf_msg)

if __name__ == '__main__':
    rospy.init_node('imu_to_tf_broadcaster')
    tf_broadcaster = tf2_ros.TransformBroadcaster()

    # Subscribe to the IMU data topic
    rospy.Subscriber('/mavros/imu/data', Imu, imu_callback)

    rospy.spin()
