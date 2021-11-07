import pyautogui
from Operation import Operation


class Keyboard(Operation):
    def __init__(self, string):
        self.string = string

    def execute(self):
        pyautogui.write(self.string, interval=0.01)

    def print(self):
        print(f"Keyboard {self.string}")
