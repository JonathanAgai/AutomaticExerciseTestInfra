import time
import pyautogui
from TemplateMatcher import TemplateMatcher


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
        self.feature_review = []

    def run(self):
        time.sleep(5)
        for operation in self.operations:
            operation.execute()
            time.sleep(2)

        cropped_image = pyautogui.screenshot(region=self.crop_area)
        cropped_image_path = self.crop_area_img_path + f'\\{self.test_name}.png'
        cropped_image.save(cropped_image_path)

        if not self.state:
            # os.remove(cropped_image_path)
            tm = TemplateMatcher(self.expected_img_path, cropped_image_path, self.test_name)
            self.success = tm.template_matching()
            print(f"test success = {self.success}")
            self.feature_review.append(f'{self.test_name}: {self.success}')

    def print(self):
        print(f"expected_image_path: {self.expected_img_path}, cropped_area: {self.crop_area}")
        for operation in self.operations:
            operation.print()

    def get_reviews(self):
        return self.feature_review
