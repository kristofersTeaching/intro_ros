import rclpy
import json
import time
from handlers_msgs.msg import CubeState

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('send_goal')

    publisher = node.create_publisher(CubeState, '/goal', 10)
    msg = CubeState()
    msg.pos1 = 'blue_cube'
    msg.pos2 = 'green_cube'
    msg.pos3 = 'red_cube'


    time.sleep(0.2)
    publisher.publish(msg)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()