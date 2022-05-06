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
        # TODO documentation
        """
        execute(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        raise NotImplementedError

    def print(self):
        # TODO documentation
        """
        print(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        raise NotImplementedError


class Click(Operation):
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
    def __init__(self, x, y):
        # TODO documentation
        """
        __init__(...) write function description here
        :param x: write parameter description here
        :type x: write the parameter's type here
        :param y: write parameter description here
        :type y: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.x = x
        self.y = y

    def execute(self):
        # TODO documentation
        """
        execute(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        pyautogui.click(self.x, self.y)

    def print(self):
        # TODO documentation
        """
        print(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        print(f"Click:  x [{type(self.x)}] = {self.x}, y [{type(self.y)}]= {self.y}")


class DoubleClick(Operation):
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
    def __init__(self, x, y):
        # TODO documentation
        """
        __init__(...) write function description here
        :param x: write parameter description here
        :type x: write the parameter's type here
        :param y: write parameter description here
        :type y: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.x = x
        self.y = y

    def execute(self):
        # TODO documentation
        """
        execute(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        pyautogui.click(self.x, self.y, clicks=2)

    def print(self):
        # TODO documentation
        """
        print(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        print(f"DobuleClick {self.x}, {self.y}")


class Keyboard(Operation):
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
    def __init__(self, string):
        # TODO documentation
        """
        __init__(...) write function description here
        :param string: write parameter description here
        :type string: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.string = string

    def execute(self):
        # TODO documentation
        """
        execute(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        pyautogui.write(self.string, interval=0.01)

    def print(self):
        # TODO documentation
        """
        print(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        print(f"Keyboard {self.string}")


class Delete(Operation):
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
        # TODO documentation
        """
        execute(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        pyautogui.press('backspace', interval=0.01)

    def print(self):
        # TODO documentation
        """
        print(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        print(f"delete")


class Scroll(Operation):
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
    def __init__(self, scroll_type, clicks, x, y):
        # TODO documentation
        """
        __init__(...) write function description here
        :param scroll_type: write parameter description here
        :type scroll_type: write the parameter's type here
        :param clicks: write parameter description here
        :type clicks: write the parameter's type here
        :param x: write parameter description here
        :type x: write the parameter's type here
        :param y: write parameter description here
        :type y: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.scroll_type = scroll_type
        self.clicks = clicks
        self.x = x
        self.y = y

    def execute(self):
        # TODO documentation
        """
        execute(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        pyautogui.click(self.x, self.y, clicks=self.clicks  )

    def print(self):
        # TODO documentation
        """
        print(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        print(f"{self.scroll_type} {self.clicks}, {self.x}, {self.y}")


class ScrollUp(Scroll):
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
    def __init__(self, clicks, x, y):
        # TODO documentation
        """
        __init__(...) write function description here
        :param clicks: write parameter description here
        :type clicks: write the parameter's type here
        :param x: write parameter description here
        :type x: write the parameter's type here
        :param y: write parameter description here
        :type y: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        super().__init__("ScrollUp", clicks, x, y)

    def execute(self):
        # TODO documentation
        """
        execute(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        super().execute()

    def print(self):
        # TODO documentation
        """
        print(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        super().execute()


class ScrollDown(Scroll):
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
    def __init__(self, clicks, x, y):
        # TODO documentation
        """
        __init__(...) write function description here
        :param clicks: write parameter description here
        :type clicks: write the parameter's type here
        :param x: write parameter description here
        :type x: write the parameter's type here
        :param y: write parameter description here
        :type y: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        super().__init__("ScrollDown", clicks, x, y)

    def execute(self):
        # TODO documentation
        """
        execute(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        super().execute()

    def print(self):
        # TODO documentation
        """
        print(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        super().execute()
