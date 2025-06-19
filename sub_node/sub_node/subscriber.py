import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SubscriberObject(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.create_subscription(Float32, 'steer', self.steer_callback, 10)
        self.create_subscription(Float32, 'throttle', self.throttle_callback, 10)

    def steer_callback(self, steer_msg):
        self.get_logger().info(f'Received steer: {steer_msg.data}')

    def throttle_callback(self, throttle_msg):
        self.get_logger().info(f'Received throttle: {throttle_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberObject()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
