import numpy as np
import pyautogui
from TemplateMatcher import *


def get_box_union(box1: list, box2: list):
    x1_left, y1_top, w1, h1 = box1
    x1_right = x1_left + w1
    y1_down = y1_top + h1

    x2_left, y2_top, w2, h2 = box2
    x2_right = x2_left + w2
    y2_down = y2_top + h2

    x_min = min(x1_left, x1_right, x2_left, x2_right)
    x_max = max(x1_left, x1_right, x2_left, x2_right)
    y_min = min(y1_top, y1_down, y2_top, y2_down)
    y_max = max(y1_top, y1_down, y2_top, y2_down)

    x = x_min
    y = y_min
    width = x_max - x_min
    height = y_max - y_min

    return [x, y, width, height]


def get_element_input_location(element_location: list, input_dimension: dict):
    orientation = input_dimension["orientation"]
    width = input_dimension["width"]
    height = input_dimension["height"]

    # assuming that element padding is already calculated in the img
    e_x, e_y, e_w, e_h = element_location
    if orientation == "right":
        return [e_x+e_w, e_y, width, height]
    if orientation == "top":
        return [e_x, e_y-height, width, height]
    if orientation == "left":
        return [e_x-width, e_y, width, height]
    if orientation == "down":
        return [e_x, e_y+ e_h, width, height]
    return []


class GUIConfigurations:
    _gui_config = None

    @staticmethod
    def initialize(gui_elements, images_dir_path):
        GUIConfigurations._gui_config = GUIConfigurations(gui_elements, images_dir_path)

    @staticmethod
    def get_instance():
        return GUIConfigurations._gui_config

    def __init__(self, gui_elements, images_dir_path):
        self.images_dir_path = images_dir_path
        self.gui_elements = gui_elements

    def find_gui_elements(self):
        """
        steps:
        1)  open app screen image
        2)  iterate over each element in elements
        3)  open element image from image_path_location
        4)  use template matching to find element(x=left,y = top)
            on app screen image
        5)  save element location [x, y, w, h]
        6)  if value exist generate location for value as well
        """

        app_crop_area = [
            self.gui_elements["screen_offset_x"],
            self.gui_elements["screen_offset_y"],
            self.gui_elements["screen_width"],
            self.gui_elements["screen_height"]
        ]
        app_image = pyautogui.screenshot(region=app_crop_area)
        # convert into numpy in order to work with cv library
        app_image = np.array(app_image)

        for e_key, e_val in self.gui_elements["elements"].items():
            if e_key == "display_full_name":
                a =5


            element_img_name = e_val["image_name"]
            element_img_path = f"{self.images_dir_path}/{element_img_name}"
            element_location = TemplateMatcher.find_location(app_image, element_img_path)

            element_location[0] += self.gui_elements["screen_offset_x"]
            element_location[1] += self.gui_elements["screen_offset_y"]

            if len(element_location) == 0:
                print(f"couldn't find element: {e_key}")
                return False
            if "input" not in e_val:
                e_val["location"] = element_location
                continue

            input_dimension = e_val["input"]
            element_input_location = get_element_input_location(element_location, input_dimension)

            if len(element_input_location) == 0:
                print(f"couldn't find element: {e_key} input location")
                return False
            input_dimension["location"] = element_input_location

            crop_area = get_box_union(element_location, element_input_location)
            e_val["crop_area"] = crop_area

        return True

    def get_element_location(self, element_name):
        if element_name not in self.gui_elements["elements"]:
            return []
        return self.gui_elements["elements"][element_name]["location"]

    def get_element_input_location(self, element_name):
        if element_name not in self.gui_elements["elements"]:
            print(f"Error Couldn't find {element_name}")
            return []

        if "input" not in self.gui_elements["elements"][element_name]:
            print(f"Error Couldn't find {element_name} input")
            return []

        return self.gui_elements["elements"][element_name]["input"]["location"]

    def get_elements_xy(self, element_name):
        location = self.get_element_location(element_name)
        if len(location) == 0:
            return []

        x, y, w, h = location
        cx = int(x + w/2)
        cy = int(y + h/2)
        return [cx, cy]

    def get_elements_input_xy(self, element_name):
        location = self.get_element_input_location(element_name)
        if len(location) == 0:
            return []

        x, y, w, h = location
        cx = int(x + w/2)
        cy = int(y + h/2)
        return [cx, cy]

    def get_crop_area(self, element_name):
        return self.gui_elements["elements"][element_name]["crop_area"]


if __name__ == "__main__":
    pass
    # path = "json_fml.json"
    # gui_config = GUIConfigurations(path)
    # gui_config.find_gui_elements()
