import os
import time
from functools import reduce

import cv2
import pyautogui
from PIL import ImageChops, Image

from ImageSimilarity import ImageSimilarity


def equal(im1, im2):
    print(f"{ImageChops.difference(im1, im2).getbbox()}")
    return ImageChops.difference(im1, im2).getbbox() is None


class Test:
    def __init__(self, operations, expected_img_path, crop_area):
        self.operations = operations

        # expected_img_path: Solution image for a specific test
        self.expected_img_path = expected_img_path

        # crop_area: Screenshot area for comparison
        self.crop_area = crop_area
        self.success = False

    def run(self):
        time.sleep(5)
        for operation in self.operations:
            operation.execute()
            time.sleep(2)

        cropped_image = pyautogui.screenshot(region=self.crop_area)
        cropped_image_path = r'C:\\Users\\Ben\\Desktop\\compare\\test.png'
        cropped_image.save(cropped_image_path)
        img1 = cv2.imread(self.expected_img_path, 0)
        img2 = cv2.imread(cropped_image_path, 0)

        image_sim = ImageSimilarity(img1, img2)
        print(f"orb_sim: {image_sim.orb_sim()}")
        print(f"structural_sim: {image_sim.structural_sim()}")

        self.success = equal(cropped_image, cropped_image)
        # os.remove(r'C:\\Users\\Ben\\Desktop\\compare\\test.png')
        print(f"test success = {self.success}")
        # TODO make sure to write reviews after each test

    def print(self):
        print(f"expected_image_path: {self.expected_img_path}, cropped_area: {self.crop_area}")
        for operation in self.operations:
            operation.print()
