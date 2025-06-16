# piracer_demo/control_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

from piracer.vehicles import PiRacerPro
from piracer.gamepads import ShanWanGamepad


class ControlNode(Node):
    def __init__(self):
        super().__init__('control_node')

        self.piracer = PiRacerPro()
        self.shanwan_gamepad = ShanWanGamepad()
        self.manual_mode = True  # 기본은 manual

        self.subscription = self.create_subscription(
            Float32,
            '/steering_angle',
            self.steering_callback,
            10
        )

        self.timer = self.create_timer(0.05, self.timer_callback)  # 10Hz
        # self.get_logger().info("control_node started. Waiting for gamepad and steering_angle...")

    def timer_callback(self):
        gamepad_input = self.shanwan_gamepad.read_data()

        if gamepad_input.button_a:
            self.manual_mode = True
            self.get_logger().info("Manual mode (joystick control) activated.")
        elif gamepad_input.button_x:
            self.manual_mode = False
            self.get_logger().info("Auto mode (topic control) activated.")

        if self.manual_mode:
            # 조이스틱 입력값에 따라 조향/속도 제어
            steering = gamepad_input.analog_stick_left.x
            throttle = gamepad_input.analog_stick_right.y * 0.5

            self.piracer.set_steering_percent(steering)
            self.piracer.set_throttle_percent(throttle)

            # self.get_logger().info(f"[MANUAL] Steering: {steering:.2f}, Throttle: {throttle:.2f}")

    def steering_callback(self, msg: Float32):
        if self.manual_mode:
            # manual 모드일 땐 callback 무시
            return

        angle_deg = msg.data
        steering_percent = max(-1.0, min(1.0, angle_deg / 30.0))  # 예: -30도 ~ 30도 → -1.0 ~ 1.0

        self.piracer.set_steering_percent(steering_percent)
        # self.get_logger().info(f"[AUTO] Steering set to: {steering_percent:.2f}")

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
