import time
import pyautogui
from TemplateMatcher import TemplateMatcher
from RunTimeTestConfigurations import *


class Test:
    def __init__(self, operations, expected_result_img_path, crop_area, crop_area_img_path, test_name):
        self.operations = operations

        # expected_img_path: Solution image for a specific test
        self.expected_result_img_path = expected_result_img_path

        # crop_area: Screenshot area for comparison
        self.crop_area = crop_area
        self.crop_area_img_path = crop_area_img_path
        self.test_name = test_name
        self.success = False
        self.review_str = ''

    def run(self, student_id):
        time.sleep(0.5)
        for operation in self.operations:
            operation.execute()
            time.sleep(0.5)

        cropped_image_path = self.crop_area_img_path + f'\\{self.test_name}.png'

        if RunTimeTestConfigurations.get_is_lecturer_mode():
            cropped_image = pyautogui.screenshot(region=self.crop_area)
            cropped_image.save(cropped_image_path)
            return


        # os.remove(cropped_image_path)
        tm = TemplateMatcher(self.expected_result_img_path, cropped_image_path, self.test_name, student_id)
        self.success = tm.template_matching()
        print(f"test success = {self.success}")

        if self.success:
            self.review_str = f'{self.test_name}: succeeded'
        else:
            self.review_str = f'{self.test_name}: failed'

    def print(self):
        print(f"expected_image_path: {self.expected_result_img_path}, cropped_image: {self.crop_area}")
        for operation in self.operations:
            operation.print()

    def get_review(self):
        return self.review_str
