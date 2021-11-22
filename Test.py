import time

import pyautogui
import glob
from PIL import Image


def is_images_the_same(img1, img2) -> bool:
    return False


def extract_image_from_path(expected_img_path):
    #filename = glob.glob(expected_img_path)
    return Image.open(expected_img_path)


class Test:
    def __init__(self, operations, expected_img_path, crop_area):
        self.operations = operations

        # expected_img_path: Solution image for a specific test
        self.expected_img_path = expected_img_path
        self.expected_img = extract_image_from_path(self.expected_img_path)

        # crop_area: Screenshot area for comparison
        self.crop_area = crop_area
        self.success = False

    def run(self):
        time.sleep(5)
        for operation in self.operations:
            operation.execute()
            time.sleep(2)

        cropped_image = pyautogui.screenshot(region=self.crop_area)
        self.success = is_images_the_same(self.expected_img, cropped_image)
        # TODO make sure to write reviews after each test

    def print(self):
        print(f"expected_image_path: {self.expected_img_path}, cropped_area: {self.crop_area}")
        for operation in self.operations:
            operation.print()
