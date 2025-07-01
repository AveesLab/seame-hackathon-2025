import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class PublisherObject(Node):
    def __init__(self):
        super().__init__('publisher')
        self.steer_pub = self.create_publisher(Float32, 'steer', 10)
        self.throttle_pub = self.create_publisher(Float32, 'throttle', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        steer_msg = Float32()
        throttle_msg = Float32()

        steer_msg.data = 0.2
        throttle_msg.data = -0.4

        self.get_logger().info(f'Publishing steer: {steer_msg.data}, throttle: {throttle_msg.data}')
        self.steer_pub.publish(steer_msg)
        self.throttle_pub.publish(throttle_msg)

def main(args=None):
    rclpy.init(args=args)
    node = PublisherObject()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
