#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import cv2
import numpy as np

class VisionNode(Node):

    def __init__(self):
        super().__init__('vision_node')
        self.cap = cv2.VideoCapture(0)

        self.get_logger().info("Vision node started")

        self.run()

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            height, width, _ = frame.shape

            # Convert to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Detect BLUE object (you can change this)
            lower = np.array([100, 150, 0])
            upper = np.array([140, 255, 255])

            mask = cv2.inRange(hsv, lower, upper)

            # Find contours
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            state = "SEARCHING"

            if len(contours) > 0:
                largest = max(contours, key=cv2.contourArea)

                x, y, w, h = cv2.boundingRect(largest)
                center_x = x + w // 2

                # Draw rectangle
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

                # Decide state
                if center_x < width / 3:
                    state = "LEFT"
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                elif center_x < 2 * width / 3:
                    state = "CENTER"

                else:
                    state = "RIGHT"
                    frame = cv2.Canny(frame, 100, 200)

            else:
                state = "SEARCHING"
                frame = cv2.bitwise_not(frame)

            # Show state
            cv2.putText(frame, state, (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            self.get_logger().info(f"State: {state}")

            cv2.imshow("Vision", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
