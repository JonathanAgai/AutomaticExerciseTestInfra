import json
import os.path
from subprocess import Popen
from time import sleep
import pyautogui
import sys
from TestConfigurationParser import *

pyautogui.FAILSAFE = False


GUI_ELEMENT_LOCATION_NAME = "gui_elements_locations.json"
LECTURER_SOLUTION_NAME = "lecturer_solution/lecturer_solution.py"


def load_data(hw_path: str):
    path = f"{hw_path}/{GUI_ELEMENT_LOCATION_NAME}"
    with open(path, "r") as f:
        return json.load(f)


def generate_hw_configuration_tree(hw_path:str):
    directories = [
        f"{hw_path}",
        f"{hw_path}/gui_elements_images",
        f"{hw_path}/lecturer_solution"
    ]

    for d in directories:
        if not os.path.exists(d):
            os.mkdir(d)


def create_elements_images(hw_path: str):
    data = load_data(hw_path)
    for e_name, e_crop_area in data.items():
        string_e_name = e_name.replace("_", " ")
        gui_element_img = pyautogui.screenshot(region=e_crop_area)
        cropped_image_path = f"{hw_path}/gui_elements_images/{string_e_name}.png"
        gui_element_img.save(cropped_image_path)


def execute_lecturer_exec(hw_path: str):
    RunTimeTestConfigurations.set_is_lecturer_mode(True)
    RunTimeTestConfigurations.set_hw_path(hw_path)
    test_config_path = f"{hw_path}/tests_configurations.json"
    gui_elements_images_path = f"{hw_path}/gui_elements_images"
    TestConfigurationParser.initialize(test_config_path, gui_elements_images_path)

    exec_path = f"{hw_path}/{LECTURER_SOLUTION_NAME}"
    cmd = ['python.exe', exec_path]
    p = Popen(cmd)
    sleep(2)

    create_elements_images(hw_path)

    gui_config = GUIConfigurations.get_instance()
    gui_config.find_gui_elements()

    features = TestConfigurationParser.extract_features(test_config_path)
    for feature in features:
        feature.run_tests("-1")

    p.terminate()


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc != 2:
        print("Error expected hw configuration name\nexample:<hw1>")
        sys.exit(-1)

    hw_name = sys.argv[1]
    generate_hw_configuration_tree(hw_name)
    execute_lecturer_exec(hw_name)

