import json
from subprocess import Popen
from time import sleep
import pyautogui
with open("../configuration/Lecturer_GUI_Elements_Location.json", "r") as f:
    data = json.load(f)

lecturer_id_dir_path = "../students_solution_execs/308418367/308418367.py"
print(lecturer_id_dir_path)
cmd = ['python.exe', lecturer_id_dir_path]
p = Popen(cmd)
sleep(5)
for e_name, e_crop_area in data.items():
    gui_element_img = pyautogui.screenshot(region=e_crop_area)
    cropped_image_path = f"../configuration/hw1/{e_name}.png"
    gui_element_img.save(cropped_image_path)
p.terminate()
