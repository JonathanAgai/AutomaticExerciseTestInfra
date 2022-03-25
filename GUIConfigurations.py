from TestConfigurationParser import *


def get_box_union(box1: list, box2: list):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    x_min = min(x1, x2)
    x_max = max(x1, x2)
    y_min = min(y1, y2)
    y_max = max(y1, y2)

    x = x_min
    y = y_min
    width = x_max - x_min
    height = y_max - y_min

    return [x, y, width, height]



def get_element_input_location(element_location: list, input_dimension: dict):
    orientation = input_dimension["orientation"]
    width = input_dimension["width"]
    height = input_dimension["height"]

    #assuming that element padding is already calculated in the img
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

    def __init__(self, test_config_path):
        self.gui_elements = TestConfigurationParser.extract_gui_elements(test_config_path)

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

        student_app_crop_area = [
            self.gui_elements["screen_width"],
            self.gui_elements["screen_height"],
            self.gui_elements["screen_offset_y"],
            self.gui_elements["screen_offset_x"]
        ]
        student_app_img = pyautogui.screenshot(region=student_app_crop_area)

        for e_key, e_val in self.gui_elements["elements"].items():
            element_img_path = e_val["image_path_location"]
            element_location = TemplateMatcher.find_location(student_app_img, element_img_path)

            if len(element_location) == 0:
                print(f"couldn't find element: {e_key}")
                return False
            if e_val.at("input") is None:
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
        if self.gui_elements["elements"].at(element_name) is None:
            return []
        return self.gui_elements["elements"][element_name]["location"]

    def get_element_input_location(self, element_name):
        if self.gui_elements["elements"].at(element_name) is None:
            print(f"Error Couldn't find {element_name}")
            return []

        if self.gui_elements["elements"][element_name]["input"] is None:
            print(f"Error Couldn't find {element_name} input")
            return []

        return self.gui_elements["elements"][element_name]["input"]["location"]

    def get_crop_area(self, element_name):
        return self.gui_elements[element_name]["crop_area"]


if __name__ == "__main__":
    pass
    # path = "json_fml.json"
    # gui_config = GUIConfigurations(path)
    # gui_config.find_gui_elements()
