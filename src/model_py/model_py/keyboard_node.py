#!/usr/bin/env python3
import rospy
from std_srvs.srv import Trigger, TriggerRequest
import sys, select, termios, tty

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main():
    rospy.init_node('keyboard_listener')

    rospy.wait_for_service('/toggle_rviz')
    toggle_rviz = rospy.ServiceProxy('/toggle_rviz', Trigger)

    print("Press the space bar to toggle RViz")

    while not rospy.is_shutdown():
        key = getKey()
        if key == ' ':
            try:
                response = toggle_rviz(TriggerRequest())
                rospy.loginfo("RViz toggled: %s", response.message)
            except rospy.ServiceException as e:
                rospy.logerr("Service call failed: %s", e)

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    main()
