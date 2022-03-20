import cv2
import numpy as np
import os


class TemplateMatcher:
    def __init__(self, student_id, source_image, crop_image, test_name):
        self.student_id = student_id
        self.source_image = source_image
        self.crop_image = crop_image
        self.test_name = test_name
        self.match_found = False

    def draw_rectangle_around_target(self, loc, image, w, h):
        # for pt in zip(*loc[::-1]):
        # is for the points which have values greater than threshold.
        # zip is a container of all such points
        # and it will iterate to all such points
        # and draw rectangle around this closed entity.
        for pt in zip(*loc[::-1]):
            cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    def save_result_image(self, image):
        result_dir = f'template_results/{self.student_id}'
        result_path = f'{result_dir}/{self.test_name}.png'
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
        result_image = cv2.imwrite(result_path, image)

    def template_matching(self):
        image = cv2.imread(self.source_image)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(self.crop_image, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.99

        if np.amax(res) >= threshold:
            self.match_found = True

        loc = np.where(res >= threshold)

        #self.draw_rectangle_around_target(loc, image, w, h)

        if not self.match_found:
            self.save_result_image(template)

        return self.match_found
