import cv2
import numpy as np
from matplotlib import pyplot as plt


class TemplateMatcher:
    def __init__(self, source_image, crop_image, test_name):
        self.source_image = source_image
        self.crop_image = crop_image
        self.test_name = test_name

    def template_matching(self):
        image = cv2.imread(self.source_image)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(self.crop_image,0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.99
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        result_path = 'C:\\Users\\Ben\\Desktop\\template_results' + f'\\{self.test_name}.png'
        match_found = cv2.imwrite(result_path, image)
        cv2.waitKey(0)

        return match_found
