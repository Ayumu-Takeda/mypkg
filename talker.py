import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub=node.create_publisher(Int16,"countup",10)
n = 1


def cd():
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    n += 1

node.create_timer(0.1,cd)
rclpy.spin(node)
