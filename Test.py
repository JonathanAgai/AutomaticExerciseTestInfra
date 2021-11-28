import os
import time
from functools import reduce

import cv2
import pyautogui
from PIL import ImageChops, Image

from ImageSimilarity import ImageSimilarity


class Test:
    def __init__(self, operations, expected_img_path, crop_area, crop_area_img_path, test_name, state):
        self.operations = operations

        # expected_img_path: Solution image for a specific test
        self.expected_img_path = expected_img_path

        # crop_area: Screenshot area for comparison
        self.crop_area = crop_area
        self.crop_area_img_path = crop_area_img_path
        self.test_name = test_name
        self.state = state
        self.success = False
        # TODO ? self.test_review = []

    def run(self):
        time.sleep(5)
        for operation in self.operations:
            operation.execute()
            time.sleep(2)

        cropped_image = pyautogui.screenshot(region=self.crop_area)
        cropped_image_path = self.crop_area_img_path + f'\\{self.test_name}.png'
        cropped_image.save(cropped_image_path)

        if not self.state:
            img1 = cv2.imread(self.expected_img_path, 0)
            img2 = cv2.imread(cropped_image_path, 0)

            image_sim = ImageSimilarity(img1, img2)
            self.success = image_sim.compare_images()
            # os.remove(cropped_image_path)

            print(f"test success = {self.success}")
            # TODO ? self.test_review.append(self.test_name, self.success)

    def print(self):
        print(f"expected_image_path: {self.expected_img_path}, cropped_area: {self.crop_area}")
        for operation in self.operations:
            operation.print()

    def get_reviews(self):
        return self.test_review
