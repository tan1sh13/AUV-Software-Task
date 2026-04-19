#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommanderNode(Node):

    def __init__(self):
        super().__init__('commander_node')
        self.publisher = self.create_publisher(String, '/cmd', 10)
        self.get_logger().info("Enter commands: forward, backward, turn left, turn right")

        self.send_commands()

    def send_commands(self):
        while True:
            cmd = input(">> ")

            msg = String()
            msg.data = cmd

            self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CommanderNode()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
