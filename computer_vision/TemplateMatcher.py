import cv2
import numpy as np


class TemplateMatcher:
    """
        This component is responsible for comparing images and finding matches

        Attributes
        ----------
        test_name

        Methods
        -------
        draw_rectangle_around_target(loc, image, w, h)
        template_matching(source_image_cv, lecturer_img_path)
        find_location(source_image, template_path)
        """
    def __init__(self, test_name="-1"):

        self.test_name = test_name

    def draw_rectangle_around_target(self, loc, image, w, h):
        # for pt in zip(*loc[::-1]):
        # is for the points which have values greater than threshold.
        # zip is a container of all such points
        # and it will iterate to all such points
        # and draw rectangle around this closed entity.
        for pt in zip(*loc[::-1]):
            cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    def template_matching(self, source_image_cv, lecturer_img_path):
        """
        template_matching(...) compare between given cv img and img inside file system
        :param source_image_cv: img to be compered with
        :type source_image_cv: open cv img
        :param lecturer_img_path: path to lecturer(correct) img path
        :type lecturer_img_path: string
        :return: true if match found otherwise false
        :rtype: bool
        """
        image = source_image_cv
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(lecturer_img_path, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.99

        print(f"test name: {self.test_name}, res: {np.amax(res)}")
        if np.amax(res) >= threshold:
            return True

        return False

    @staticmethod
    def find_location(source_image, template_path):
        """
        find_location(...) Finding element location
        :param source_image: img to be compered with
        :type source_image: open cv img
        :param template_path: template img path
        :type template_path: string
        :return: x, y, width, height
        :rtype: list of ints
        """
        image = source_image
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_path, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.985
        print(f"match percentage: {np.amax(res)}")
        if np.amax(res) < threshold:
            print(f"Failed to find match, threshold = {threshold}")
            return []

        print("Match found")

        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]
            return [x, y, w, h]

        return []
