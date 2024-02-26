#!/usr/bin/env python3

from tkinter import *
import rospy
from std_msgs.msg import Int16

frame = Tk()
frame.geometry("200x200")

L = Label(frame, font = ('Arial', 60), text = "0")
L.pack()

rospy.init_node('GUI_READ_Sensor')
rate = rospy.Rate(10)
rate.sleep()


def read(num):
 sensor_read = num.data
 L.config(text = str(sensor_read))
 
sub = rospy.Subscriber("Topic_Sensor", Int16, callback = read)


frame.mainloop()
