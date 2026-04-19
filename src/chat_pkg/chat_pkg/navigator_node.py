#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from chat_pkg_interfaces.msg import BotPose

class NavigatorNode(Node):

    def __init__(self):
        super().__init__('navigator_node')

        self.subscription = self.create_subscription(
            String,
            '/cmd',
            self.callback,
            10
        )

        self.publisher = self.create_publisher(BotPose, '/bot_pose', 10)

        self.x = 0.0
        self.y = 0.0
        self.direction = "North"

    def callback(self, msg):
        cmd = msg.data.lower()

        # TURNING LOGIC
        if cmd == "turn right":
            self.direction = self.turn_right(self.direction)

        elif cmd == "turn left":
            self.direction = self.turn_left(self.direction)

        # MOVEMENT LOGIC
        elif cmd == "forward":
            if self.direction == "North":
                self.y += 1
            elif self.direction == "South":
                self.y -= 1
            elif self.direction == "East":
                self.x += 1
            elif self.direction == "West":
                self.x -= 1

        elif cmd == "backward":
            if self.direction == "North":
                self.y -= 1
            elif self.direction == "South":
                self.y += 1
            elif self.direction == "East":
                self.x -= 1
            elif self.direction == "West":
                self.x += 1

        # Publish result
        pose = BotPose()
        pose.x = self.x
        pose.y = self.y
        pose.facing_direction = self.direction

        self.publisher.publish(pose)

        self.get_logger().info(
            f"Position: ({self.x}, {self.y}) Facing: {self.direction}"
        )

    def turn_right(self, d):
        order = ["North", "East", "South", "West"]
        return order[(order.index(d) + 1) % 4]

    def turn_left(self, d):
        order = ["North", "West", "South", "East"]
        return order[(order.index(d) + 1) % 4]


def main(args=None):
    rclpy.init(args=args)
    node = NavigatorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
