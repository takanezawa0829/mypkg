#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

is_prime_num = 0

def cb(message):
    global n
    global is_prime_num
    for num in range(message.data):
        if message.data == 2:
            break
        if (num + 1) == int(message.data / 2):
            n = message.data
            rospy.loginfo(message.data)
            is_prime_num = 1
            break
        if message.data % (num + 2) == 0:
            break





if __name__ == '__main__':
    rospy.init_node('prime_num')
    sub = rospy.Subscriber('count_up', Int32, cb)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()