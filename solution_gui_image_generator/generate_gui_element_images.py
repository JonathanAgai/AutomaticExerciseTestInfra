import json
from subprocess import Popen
from time import sleep
import pyautogui

DEFAULT_PATH = "../configuration/Lecturer_GUI_Elements_Location.json"
DEFAULT_LECTURER_PATH = "../students_solution_execs/308418367/308418367.py"


def load_data(path: str= DEFAULT_PATH):
    with open(path, "r") as f:
        return json.load(f)


def create_elements_images():
    data = load_data()
    for e_name, e_crop_area in data.items():
        gui_element_img = pyautogui.screenshot(region=e_crop_area)
        cropped_image_path = f"../configuration/hw1/{e_name}.png"
        gui_element_img.save(cropped_image_path)


def execute_lecturer_exec(exec_path: str = DEFAULT_LECTURER_PATH):
    cmd = ['python.exe', exec_path]
    p = Popen(cmd)
    sleep(5)
    create_elements_images()
    # TODO add lecturer solution somehow and generate the solution images
    p.terminate()



