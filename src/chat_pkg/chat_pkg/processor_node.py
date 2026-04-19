#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class ProcessorNode(Node):

    def __init__(self):
        super().__init__('processor_node')

        self.subscription = self.create_subscription(
            Int32,
            '/raw_signal',
            self.callback,
            10
        )

        self.publisher = self.create_publisher(Int32, '/processed_signal', 10)

    def callback(self, msg):
        new_value = msg.data * 5

        out_msg = Int32()
        out_msg.data = new_value

        self.publisher.publish(out_msg)

        self.get_logger().info(f"Processed: {new_value}")


def main(args=None):
    rclpy.init(args=args)
    node = ProcessorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
