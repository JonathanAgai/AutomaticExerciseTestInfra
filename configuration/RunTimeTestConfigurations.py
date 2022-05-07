

class RunTimeTestConfigurations:
    # TODO documentation
    """
        write in one line class description here

        write long description of class here

        Attributes
        ----------

        Methods
        -------
        get_solution_screenshot_imgs_path()
            write function description here
        set_hw_path(hw_path)
            write function description here
        get_hw_path()
            write function description here
        set_is_lecturer_mode(lecturer_mode: bool)
            write function description here
        get_is_lecturer_mode()
            write function description here
        """

    # public static member that holds whether tests are to be run in lecturer_mode
    _lecturer_mode = False
    _hw_path = None

    @staticmethod
    def get_solution_screenshot_imgs_path():
        # TODO documentation
        """
        get_solution_screenshot_imgs_path(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        hw_path = RunTimeTestConfigurations._hw_path
        if hw_path is None:
            raise Exception("hw path not set please set a path")

        if RunTimeTestConfigurations._lecturer_mode:
            return f"{hw_path}/lecturer_solution"
        else:
            return f"students_solution/{hw_path}"

    @staticmethod
    def set_hw_path(hw_path):
        # TODO documentation
        """
        set_hw_path(...) write function description here
        :param hw_path: write parameter description here
        :type hw_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        RunTimeTestConfigurations._hw_path = hw_path

    @staticmethod
    def get_hw_path():
        # TODO documentation
        """
        get_hw_path(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        return RunTimeTestConfigurations._hw_path

    @staticmethod
    def set_is_lecturer_mode(lecturer_mode: bool):
        # TODO documentation
        """
        set_is_lecturer_mode(...) write function description here
        :param lecturer_mode: write parameter description here
        :type lecturer_mode: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        RunTimeTestConfigurations._lecturer_mode = lecturer_mode

    @staticmethod
    def get_is_lecturer_mode():
        # TODO documentation
        """
        get_is_lecturer_mode(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        return RunTimeTestConfigurations._lecturer_mode
