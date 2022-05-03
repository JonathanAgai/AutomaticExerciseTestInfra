import os.path
import time

import numpy

from RunTimeTestConfigurations import *
from GUIConfigurations import *


class Test:
    def __init__(self, operations, expected_result_img_path, crop_element_name, crop_area_img_path, test_name):
        self.operations = operations

        # expected_img_path: Solution image for a specific test
        self.lecturer_img_path = expected_result_img_path

        # crop_area: Screenshot area for comparison
        self.crop_element_name = crop_element_name
        self.crop_area_img_path = crop_area_img_path
        self.test_name = test_name
        self.success = False
        self.review_str = ''

    def save_application_img(self, string_test_name, student_id):
        save_path = self.get_app_img_path(string_test_name, student_id)
        gui_config = GUIConfigurations.get_instance()
        app_crop_area = gui_config.get_app_crop_area()
        cropped_image = pyautogui.screenshot(region=app_crop_area)
        cropped_image.save(save_path)

    def get_app_img_path(self, string_test_name, student_id):
        if RunTimeTestConfigurations.get_is_lecturer_mode():
            cropped_image_path = f"{self.crop_area_img_path}/application/{string_test_name}.png"
        else:
            cropped_image_base_path = f"{self.crop_area_img_path}/{student_id}"
            if not os.path.exists(cropped_image_base_path):
                os.mkdir(cropped_image_base_path)
            cropped_image_path = f"{cropped_image_base_path}/{string_test_name}.png"

        return cropped_image_path

    def get_lecturer_cropped_img_path(self, string_test_name):
        cropped_image_path = f"{self.crop_area_img_path}/templates/{string_test_name}.png"
        return cropped_image_path

    def run(self, student_id):
        time.sleep(0.5)
        string_test_name = self.test_name.replace("_", " ")
        for operation in self.operations:
            operation.execute()
            time.sleep(0.5)

        gui_config = GUIConfigurations.get_instance()
        crop_area = gui_config.get_crop_area(self.crop_element_name)
        cropped_image = pyautogui.screenshot(region=crop_area)

        self.save_application_img(string_test_name, student_id)

        if RunTimeTestConfigurations.get_is_lecturer_mode():
            cropped_image_path = self.get_lecturer_cropped_img_path(string_test_name)
            cropped_image.save(cropped_image_path)
            return

        # create cv img for template matcher
        cropped_image_cv = cv2.cvtColor(numpy.array(cropped_image), cv2.COLOR_RGB2BGR)

        # os.remove(cropped_image_path)
        tm = TemplateMatcher(self.test_name)
        self.success = tm.template_matching(cropped_image_cv, self.lecturer_img_path)
        print(f"test success = {self.success}")

        if self.success:
            self.review_str = f'{self.test_name}: succeeded'
        else:
            self.review_str = f'{self.test_name}: failed'

    def print(self):
        print(f"expected_image_path: {self.lecturer_img_path}, cropped_image: {self.crop_area}")
        for operation in self.operations:
            operation.print()

    def get_review(self):
        return self.review_str
