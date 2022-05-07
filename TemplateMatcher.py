import cv2
import numpy as np
import os


class TemplateMatcher:
    # TODO documentation
    """
        write in one line class description here

        write long description of class here

        Attributes
        ----------
        test_name : write the parameter's type here
            write parameter description here

        Methods
        -------
        draw_rectangle_around_target(loc, image, w, h)
            write function description here
        template_matching(source_image_cv, lecturer_img_path)
            write function description here
        find_location(source_image, template_path)
            write function description here
        """
    def __init__(self, test_name="-1"):
        # TODO documentation
        """
        __init__(...) write function description here
        :param test_name: write parameter description here
        :type test_name: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.test_name = test_name

    def draw_rectangle_around_target(self, loc, image, w, h):
        # TODO documentation
        """
        draw_rectangle_around_target(...) write function description here
        :param loc: write parameter description here
        :type loc: write the parameter's type here
        :param image: write parameter description here
        :type image: write the parameter's type here
        :param w: write parameter description here
        :type w: write the parameter's type here
        :param h: write parameter description here
        :type h: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        # for pt in zip(*loc[::-1]):
        # is for the points which have values greater than threshold.
        # zip is a container of all such points
        # and it will iterate to all such points
        # and draw rectangle around this closed entity.
        for pt in zip(*loc[::-1]):
            cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    def template_matching(self, source_image_cv, lecturer_img_path):
        # TODO documentation
        """
        template_matching(...) compare between given cv img and img inside file system
        :param source_image_cv: open cv img to be compered with
        :param lecturer_img_path: path(string) to lecturer(correct) img path
        :return: true if match found otherwise false
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
        # TODO documentation
        """
        template_matching(...) write function description here
        :param source_image: write parameter description here
        :type source_image: write the parameter's type here
        :param template_path: write parameter description here
        :type template_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        image = source_image
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_path, 0)
        w, h = template.shape[::-1]

        # cv2.imshow("app", image_gray)
        # cv2.waitKey(0)
        # cv2.imshow("template", template)
        # cv2.waitKey(0)

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
