# piracer_demo/control_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from piracer.vehicles import PiRacerPro


class ControlNode(Node):
    def __init__(self):
        super().__init__('control_node')
        self.piracer = PiRacerPro()
        self.throttle = 0
        self.steering = 0
        
        self.subscription = self.create_subscription(
            Float32,
            '/throttle',
            self.throttle_callback,
            10
        )
        self.subscription = self.create_subscription(
            Float32,
            '/steering',
            self.steering_callback,
            10
        )
        self.timer = self.create_timer(0.2, self.timer_callback)  # 10Hz

    def timer_callback(self):
        self.piracer.set_steering_percent(self.steering)
        self.piracer.set_throttle_percent(self.throttle)

    def throttle_callback(self, throttle_msg: Float32):
        self.throttle = throttle_msg.data

    def steering_callback(self, steering_msg: Float32):
        self.steering = steering_msg.data

def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("KeyboardInterrupt. Shutting down.")
    finally:
        node.piracer.set_throttle_percent(0.0)
        node.piracer.set_steering_percent(0.0)
        node.destroy_node()
        rclpy.shutdown()
