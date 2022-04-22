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

            print(f"Going to find element: {e_key}")
            element_img_name = e_val["image_name"]
            element_img_path = f"{self.images_dir_path}/{element_img_name}"

            element_location = TemplateMatcher.find_location(app_image, element_img_path)

            element_location[0] += self.gui_elements["screen_offset_x"]
            element_location[1] += self.gui_elements["screen_offset_y"]

            if len(element_location) == 0:
                print(f"couldn't find element: {e_key}")
                return False

            e_val["location"] = element_location

            if "input" not in e_val:
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

    def get_element_input_location(self, element_name, input_index=None):
        if element_name not in self.gui_elements["elements"]:
            print(f"Error Couldn't find {element_name}")
            return []

        gui_element = self.gui_elements["elements"][element_name]

        if "input" not in gui_element:
            print(f"Error Couldn't find {element_name} input")
            return []

        gui_element_input = gui_element["input"]

        """
            input index is None, meaning the input is something like text box
            meaning, no index
        """
        if input_index is None:
            return gui_element_input["location"]

        """
        if input_index is a number this means the input is some sort of list
        and the input is an entry
        TODO support in future for other orientations beside down
        """
        if  gui_element_input["orientation"] == "down":
            x = gui_element["location"][0]
            y = gui_element["location"][1] + gui_element_input["height"] * input_index
            w = gui_element_input["width"]
            h = gui_element_input["height"]
            return [x, y, w, h]

        print("Invalid orientation, not supported")
        return []

    def get_elements_xy_scroll(self, element_name):
        """
        1) check that element exist
        2) check that element has vertical scroll input
        """
        if element_name not in self.gui_elements["elements"]:
            print(f"Error Couldn't find {element_name}")
            return []

        gui_element = self.gui_elements["elements"][element_name]

        if "input-vertical-scrollbar" not in gui_element:
            print(f"Error Couldn't find {element_name} input-vertical-scrollbar")
            return []

        gui_element_vertical_scroll_input = gui_element["input-vertical-scrollbar"]

        element_location = self.get_element_location(element_name)
        if len(element_location) == 0:
            return []
        e_x,e_y,e_w,e_h = element_location
        vs_w = gui_element_vertical_scroll_input["width"]
        vs_h = gui_element_vertical_scroll_input["height"]

        return [e_x,e_y,e_w,e_h,vs_w,vs_h]

    def get_location_xy_center(self, location):
        x, y, w, h = location
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        return [cx, cy]

    def get_elements_xy_scroll_up(self, element_name):
        """
        calculate center of up-arrow of the scrollbar
            breakdown: (assuming orientation right direction)
            x = (element_x + element_w) + (vertical_scrollbar_w / 2)
            y = element_y + (vertical_scrollbar_h / 2)
        """
        e_x, e_y, e_w, e_h, vs_w, vs_h = self.get_elements_xy_scroll(element_name)

        scroll_up_x = e_x + e_w
        scroll_up_y = e_y
        scroll_up_w = vs_w
        scroll_up_h = vs_h

        location = [scroll_up_x, scroll_up_y, scroll_up_w, scroll_up_h]
        return self.get_location_xy_center(location)

    def get_elements_xy_scroll_down(self, element_name):
        """
        calculate center of up-arrow of the scrollbar
            breakdown: (assuming orientation right direction)
            x = (element_x + element_w) + (vertical_scrollbar_w / 2)
            y = (element_y + element_h) - (vertical_scrollbar_h / 2)
        """
        e_x, e_y, e_w, e_h, vs_w, vs_h = self.get_elements_xy_scroll(element_name)

        scroll_down_x = e_x + e_w
        scroll_down_y = e_y + e_h - vs_h
        scroll_down_w = vs_w
        scroll_down_h = vs_h

        location = [scroll_down_x, scroll_down_y, scroll_down_w, scroll_down_h]
        return self.get_location_xy_center(location)

    def get_elements_xy(self, element_name):
        location = self.get_element_location(element_name)
        if len(location) == 0:
            return []

        return self.get_location_xy_center(location)

    def get_elements_input_xy(self, element_name, input_index=None):
        location = self.get_element_input_location(element_name, input_index)
        if len(location) == 0:
            return []

        return self.get_location_xy_center(location)

    def get_crop_area(self, element_name):
        return self.gui_elements["elements"][element_name]["crop_area"]


if __name__ == "__main__":
    pass
    # path = "json_fml.json"
    # gui_config = GUIConfigurations(path)
    # gui_config.find_gui_elements()
