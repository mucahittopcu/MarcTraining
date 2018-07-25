#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import random

def talker():
    pub = rospy.Publisher('chatter', String , queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        random_sayi = random.randint(0, 9)
        random_str = "Rastgele Uretilen Sayi : %s" % random_sayi
        rospy.loginfo(random_str)
        pub.publish(str(random_sayi))
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
