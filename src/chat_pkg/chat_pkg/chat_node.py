#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import threading

class ChatNode(Node):

    def __init__(self, username):
        super().__init__('chat_node')
        self.username = username
        self.publisher = self.create_publisher(String, '/chat', 10)
        self.subscription = self.create_subscription(
            String,
            '/chat',
            self.listener_callback,
            10
        )
        self.get_logger().info(f"{self.username} started chatting...")
        thread = threading.Thread(target=self.send_messages)
        thread.daemon = True
        thread.start()

    def listener_callback(self, msg):
        print(msg.data)

    def send_messages(self):
        while True:
            message = input()
            full_msg = f"[{self.username}]: {message}"
            msg = String()
            msg.data = full_msg
            self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    if len(sys.argv) < 2:
        print("Usage: ros2 run chat_pkg chat_node <username>")
        return
    username = sys.argv[1]
    node = ChatNode(username)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
