import pyautogui

from Operation import Operation


class Click(Operation):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        pyautogui.click(self.x, self.y)

    def print(self):
        print(f"Click {self.x}, {self.y}")
