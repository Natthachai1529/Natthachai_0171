#!/usr/bin/env python3
from tkinter import *
import rospy
from std_msgs.msg import String
from std_srvs.srv import Empty  # เพิ่ม import

root = Tk()
root.geometry("300x300")
root.title("MotionLog")

def clearToTextInput():
    ActOut.delete("1.0", "end")
    run(String(data="clear"))

def run(val):
    ActOut.insert(END, val.data + "\n")

def reset():
    clearToTextInput()
    try:
        rospy.wait_for_service("reset", timeout=5)  # รอบริการเป็นเวลาสูงสุด 5 วินาที
        clear_bg = rospy.ServiceProxy("reset", Empty)
        clear_bg()
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", str(e))

def motion_callback(msg):
    run(msg)

if __name__ == "__main__":
    # Initial ROS node and determine Publish or Subscribe action
    rospy.init_node("show_action_node")

    ActLabel = Label(text="MotionLog", font=("", 18))
    ActLabel.place(x=113, y=10)

    ActOut = Text(root, height=7, width=10, bg="light cyan", font=("", 16))
    ActOut.place(x=83, y=50)

    ClearResetBtn = Button(root, height=1, width=10, text="Clear", command=lambda: [reset()])
    ClearResetBtn.place(x=103, y=250)

    rospy.Subscriber("MotionLog_topic", String, motion_callback)

    mainloop()
    rospy.spin()

