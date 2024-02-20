#!/usr/bin/env python3
from tkinter import *
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from turtlesim.srv import SetPen
from std_srvs.srv import Empty


def publish(cmd):
    pub.publish(cmd)

def MotionLog_callback(msg):
    rospy.loginfo(msg.data)

def Forward():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z = 0.0
    publish(cmd)
    MotionLog_pub.publish(String("Forward"))

def Backward():
    cmd = Twist()
    cmd.linear.x = -LinearVel.get()
    cmd.angular.z = 0.0
    publish(cmd)
    MotionLog_pub.publish(String("Backward"))

def TurnLeft():
    cmd = Twist()
    cmd.angular.z = AngularVel.get()
    publish(cmd)
    MotionLog_pub.publish(String("TurnLeft"))

def TurnRight():
    cmd = Twist()
    cmd.angular.z = -AngularVel.get()
    publish(cmd)
    MotionLog_pub.publish(String("TurnRight")) 

def PenOn():
    rospy.wait_for_service('turtle1/set_pen')
    set_pen = rospy.ServiceProxy('turtle1/set_pen', SetPen)
    set_pen(255, 255, 255, 3, 0)
    MotionLog_pub.publish(String("PenOn")) 
  

def PenOff():
    rospy.wait_for_service('turtle1/set_pen')
    set_pen = rospy.ServiceProxy('turtle1/set_pen', SetPen)
    set_pen(255, 0, 0, 5, 1)
    MotionLog_pub.publish(String("PenOff")) 

rospy.init_node("Turtle_Control")
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)
MotionLog_pub = rospy.Publisher("MotionLog_topic", String, queue_size=10)
rospy.Subscriber("MotionLog_topic", String, MotionLog_callback)

frame = Tk()
frame.title("Turtle_Control")
frame.geometry("300x400")

LinearVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
LinearVel.set(1)

AngularVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
AngularVel.set(1)


B1 = Button(text="Forward", command=Forward)
B1.place(x=100, y=120)

B2 = Button(text="Backward", command=Backward)
B2.place(x=100, y=230)

B3 = Button(text="Turn Left", command=TurnLeft)
B3.place(x=20, y=180)

B4 = Button(text="Turn Right", command=TurnRight)
B4.place(x=200, y=180)

B5 = Button(text="PenOn", command=PenOn)
B5.place(x=20, y=300)

B6 = Button(text="PenOff", command=PenOff)
B6.place(x=180, y=300)
frame.mainloop()

