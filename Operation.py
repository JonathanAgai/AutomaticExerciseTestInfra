import abc
import pyautogui


class Operation(abc.ABC):
    # TODO documentation
    """
        write in one line class description here

        write long description of class here

        Attributes
        ----------

        Methods
        -------
        execute()
            write function description here
        print(student_id)
            write function description here
        """
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


class Scroll(Operation):
    def __init__(self, scroll_type, clicks, x, y):
        self.scroll_type = scroll_type
        self.clicks = clicks
        self.x = x
        self.y = y

    def execute(self):
        pyautogui.click(self.x, self.y, clicks=self.clicks  )

    def print(self):
        print(f"{self.scroll_type} {self.clicks}, {self.x}, {self.y}")


class ScrollUp(Scroll):
    def __init__(self, clicks, x, y):
        super().__init__("ScrollUp", clicks, x, y)

    def execute(self):
        super().execute()

    def print(self):
        super().execute()


class ScrollDown(Scroll):
    def __init__(self, clicks, x, y):
        super().__init__("ScrollDown", clicks, x, y)

    def execute(self):
        super().execute()

    def print(self):
        super().execute()
