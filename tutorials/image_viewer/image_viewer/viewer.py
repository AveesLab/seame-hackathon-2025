import rclpy
from rclpy.node import Node
import cv2
import os

class ImageViewer(Node):
    def __init__(self):
        super().__init__('image_viewer')
        
        # 이미지 경로 설정
        image_dir = '/home/seungwoo/workspace/src'
        image_path = os.path.join(image_dir, 'image_raw.jpg')

        # 이미지 읽기
        image = cv2.imread(image_path)
        if image is None:
            self.get_logger().error(f'이미지를 불러오지 못했습니다: {image_path}')
            return

        # print(image.shape)

        resized_image = cv2.resize(image, (1250, 750))
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)



        # 이미지 시각화
        cv2.imshow('Image Viewer', image)
        cv2.imshow('Resized Viewer', resized_image)
        cv2.imshow('Gray Viewer', gray_image)
        cv2.imshow('Binary Viewer', binary_image)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    node = ImageViewer()
    rclpy.shutdown()
