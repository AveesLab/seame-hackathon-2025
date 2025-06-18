import rclpy
from rclpy.node import Node
import cv2
import os

class ImageViewer(Node):
    def __init__(self):
        super().__init__('image_viewer')
        
        # 이미지 경로 설정
        image_dir = '/home/seungwoo/workspace'
        image_path = os.path.join(image_dir, 'image_raw.jpg')

        # 이미지 읽기
        image = cv2.imread(image_path)
        if image is None:
            self.get_logger().error(f'이미지를 불러오지 못했습니다: {image_path}')
            return

        # 이미지 시각화
        cv2.imshow('Image Viewer', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    node = ImageViewer()
    rclpy.shutdown()
