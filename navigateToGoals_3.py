#!/usr/bin/env python

import rospy
import actionlib

#move_base_msgs
from move_base_msgs.msg import *
from geometry_msgs.msg import *

def simple_move(x,y,w,z):


    sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )

    #create goal
    goal = MoveBaseGoal()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = w
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()

    #start listner
    sac.wait_for_server()
    #send goal
    sac.send_goal(goal)
    print "Sending goal:",x,y,w,z
    #finish
    sac.wait_for_result()
    #print result
    print sac.get_result()

def talker(coordinates):
    #publishing as PoseArray, as a reference for user
    f = open('file.csv','r')
    array = PoseArray()
    array.header.frame_id = 'map'
    array.header.stamp = rospy.Time.now()

    for goal in f:
        coordinates = goal.split(",")
        pose = Pose()
        pose.position.x = float(coordinates[0])
        pose.position.y = float(coordinates[1])
        pose.orientation.w = float(coordinates[2])
        pose.orientation.z = float(coordinates[3])
        array.poses.append(pose)

        pub = rospy.Publisher('simpleNavPoses', PoseArray, queue_size=100)
        rate = rospy.Rate(1) # 1hz

        #To not have to deal with threading, Im gonna publish just a couple times in the begging, and then continue with telling the robot to go to the points
    count = 0
    while count<1:
		rate.sleep()	
		pub.publish(array)
		count +=1


if __name__ == '__main__':
    try:
        rospy.init_node('simple_move')

        #actually sending commands for the robot to travel
        f = open('file.csv','r')
        for goal in f:
			coordinates = goal.split(",")
			simple_move(float(coordinates[0]),float(coordinates[1]),float(coordinates[2]),float(coordinates[3]))
			talker(coordinates)
    except rospy.ROSInterruptException:
        print "Keyboard Interrupt"





