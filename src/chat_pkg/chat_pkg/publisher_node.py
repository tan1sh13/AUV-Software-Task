#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.publisher = self.create_publisher(Int32, '/raw_signal', 10)
        self.timer = self.create_timer(1.0, self.publish_data)
        self.count = 1

    def publish_data(self):
        msg = Int32()
        msg.data = self.count * 2
        self.publisher.publish(msg)

        self.get_logger().info(f"Published: {msg.data}")
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
