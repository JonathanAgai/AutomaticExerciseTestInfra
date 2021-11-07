import pyautogui

from main import is_images_the_same


class Test:
    def __init__(self, operations, expected_img_path, crop_area):
        self.operations = operations

        self.expected_img_path = expected_img_path
        # TODO extract image from expected_img_path
        self.expected_img = None

        self.crop_area = crop_area
        self.success = False

    def run(self):
        for operation in self.operations:
            operation.execute()

        cropped_image = pyautogui.screenshot(region=self.crop_area)
        self.success = is_images_the_same(self.expected_img, cropped_image)

    def print(self):
        print(f"expected_image_path: {self.expected_img_path}, cropped_area: {self.crop_area}")
        for operation in self.operations:
            operation.print()