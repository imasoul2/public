#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Move_BB8():
    
    def __init__(self, loop):
        print ("Constructor for class")
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
        self.rate = rospy.Rate(10) # 10Hz freq
        self.loop = loop
        self.ctrl_c = False #  This is an indicator whether user has terminated the program yet or not/
        self.vel = Twist() # the variable with the type Twist
        self.vel.linear.x = self.loop
        rospy.on_shutdown(self.shutdownhook) # this gets triggered on shutdown
    
    def run_bb8(self):
        
        while not self.ctrl_c:
            connections = self.pub.get_num_connections()
            if connections > 0:
                self.pub.publish(self.vel)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()
                
     
    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True       
        
    def move_bb8(self):
       
        rospy.loginfo("Moving BB8!")
        self.run_bb8()    
    
    
if __name__ == '__main__':
    rospy.init_node('bb8_move', anonymous=True)
    obj = Move_BB8(0.2)
    try:
        obj.run_bb8()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass    
        
        
        
        
    