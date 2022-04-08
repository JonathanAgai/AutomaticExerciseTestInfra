import abc
import pyautogui


class Operation(abc.ABC):
    def execute(self):
        raise NotImplementedError

    def print(self):
        raise NotImplementedError


class Click(Operation):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        pyautogui.click(self.x, self.y)

    def print(self):
        print(f"Click:  x [{type(self.x)}] = {self.x}, y [{type(self.y)}]= {self.y}")


class DoubleClick(Operation):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        pyautogui.click(self.x, self.y, clicks=2)

    def print(self):
        print(f"DobuleClick {self.x}, {self.y}")


class Keyboard(Operation):
    def __init__(self, string):
        self.string = string

    def execute(self):
        pyautogui.write(self.string, interval=0.01)

    def print(self):
        print(f"Keyboard {self.string}")


class Delete(Operation):
    def execute(self):
        pyautogui.press('backspace', interval=0.01)

    def print(self):
        print(f"delete")



