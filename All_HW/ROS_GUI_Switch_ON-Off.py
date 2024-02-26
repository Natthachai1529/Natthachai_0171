#!/usr/bin/env python3

from tkinter import*
import rospy
from std_msgs.msg import Int16

frame = Tk()
frame.geometry("200x200")

rospy.init_node('GUI_LED_Control')
rate = rospy.Rate(10)
rate.sleep()

pub = rospy.Publisher("Topic_LED_13",Int16,queue_size = 10)

def Talker(val):
 cmd_val = Int16(val)
 rospy.loginfo(cmd_val)
 pub.publish(cmd_val)

B1 = Button(frame, text = "ON",command = lambda: Talker(1))
B1.pack()
B2 = Button(frame, text = "Off",command = lambda: Talker(0))
B2.pack()


frame.mainloop()
