import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import cv2
import numpy as np

class LaneDetectionNode(Node):
    def __init__(self):
        super().__init__('lane_detection_node')

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        if not self.cap.isOpened():
            self.get_logger().error("카메라 열기 실패: /dev/video0")
            raise RuntimeError("카메라 열 수 없음")

        self.publisher_ = self.create_publisher(Float32, '/steering_angle', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  #Hz

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn("카메라 프레임 읽기 실패")
            return

        frame = cv2.resize(frame, (640, 480))
        roi = frame[240:, :]

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
   
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 255, 50])
        mask_black = cv2.inRange(hsv, lower_black, upper_black)

      
        histogram = np.sum(mask_black, axis=0)

        midpoint = histogram.shape[0] // 2
        left_x = np.argmax(histogram[:midpoint])
        right_x = np.argmax(histogram[midpoint:]) + midpoint

        lane_center = (left_x + right_x) // 2
        frame_center = mask_black.shape[1] // 2
        center_offset = lane_center - frame_center

        #조향각 계산 (-15 ~ 30도)
        steering_angle = - (center_offset / frame_center) * 30.0
        self.publisher_.publish(Float32(data=float(steering_angle)))

        mask_colored = cv2.cvtColor(mask_black, cv2.COLOR_GRAY2BGR)
        overlay = cv2.addWeighted(roi, 1.0, mask_colored, 0.3, 0.0)
        output_frame = frame.copy()
        output_frame[240:, :] = overlay

        cv2.putText(output_frame, f"Steering Angle: {steering_angle:.2f} deg",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

        cv2.imshow("Lane Tracking", output_frame)
        cv2.waitKey(1)

    def destroy_node(self):
        self.cap.release()
        cv2.destroyAllWindows()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = LaneDetectionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
