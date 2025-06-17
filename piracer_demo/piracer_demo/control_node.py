# piracer_demo/control_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_msgs.msg import Joy
from piracer.vehicles import PiRacerPro


class ControlNode(Node):
    def __init__(self):
        super().__init__('control_node')
        self.is_auto = False
        self.steer = 0
        self.throttle = 0

        self.auto_steer = 0
        self.auto_throttle = 0
        self.manual_steer = 0
        self.manual_throttle = 0
        
        self.piracer = PiRacerPro()

        self.subscription = self.create_subscription(
            Float32,
            '/steering_angle',
            self.steering_callback,
            10
        )

        self.pad = self.create_subscription(
            Joy,
            '/joy',
            self.pad_callback,
            10
        )

        self.timer = self.create_timer(0.2, self.timer_callback)  # 10Hz

    def timer_callback(self):
        if self.is_auto:
            self.steer = self.auto_steer
            self.throttle = self.auto_throttle

        else:
            self.steer = self.manual_steer
            self.throttle = self.manual_throttle

        self.piracer.set_steering_percent(self.steer)
        self.piracer.set_throttle_percent(self.throttle)
        # self.get_logger().info(f"steer is {self.steer}")
        # self.get_logger().info(f"throttle is {self.throttle}")

    def pad_callback(self, joy_msg):
        ex_mode = self.is_auto
        if joy_msg.buttons[0] == 1:
            self.is_auto = False
        elif joy_msg.buttons[3] == 1:
            self.is_auto = True

        self.get_logger().info(f"mode is {self.is_auto}")

        if self.is_auto != ex_mode:
            self.get_logger().info(f"mode changed to {self.is_auto}")

        self.manual_steer = -joy_msg.axes[0]
        self.manual_throttle = joy_msg.axes[3]*0.5
        # self.get_logger().info(f"manual_steer is {self.manual_steer}")
        # self.get_logger().info(f"manual_throttle is {self.manual_throttle}")

    def steering_callback(self, steer_msg: Float32):
        # self.auto_throttle = steer_msg.data*0.5   알아서 작성하기
        self.auto_steer = max(-1.0, min(1.0, steer_msg.data / 15.0))
        self.get_logger().info(f"auto_steer is {self.auto_steer}")



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
