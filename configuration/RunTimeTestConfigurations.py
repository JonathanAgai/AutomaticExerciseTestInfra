

class RunTimeTestConfigurations:
    """
        This component is responsible for setting the relevant files and mode before running tests
        in order to be able to distinguish between creating a new exercise and testing a specific exercise

        Attributes
        ----------

        Methods
        -------
        get_solution_screenshot_imgs_path()
        set_hw_path(hw_path)
        get_hw_path()
        set_is_lecturer_mode(lecturer_mode: bool)
        get_is_lecturer_mode()
        """

    # public static member that holds whether tests are to be run in lecturer_mode
    _lecturer_mode = False
    _hw_path = None

    @staticmethod
    def get_solution_screenshot_imgs_path():

        hw_path = RunTimeTestConfigurations._hw_path
        if hw_path is None:
            raise Exception("hw path not set please set a path")

        if RunTimeTestConfigurations._lecturer_mode:
            return f"{hw_path}/lecturer_solution"
        else:
            return f"students_solution/{hw_path}"

    @staticmethod
    def set_hw_path(hw_path):
        RunTimeTestConfigurations._hw_path = hw_path

    @staticmethod
    def get_hw_path():
        return RunTimeTestConfigurations._hw_path

    @staticmethod
    def set_is_lecturer_mode(lecturer_mode: bool):
        RunTimeTestConfigurations._lecturer_mode = lecturer_mode

    @staticmethod
    def get_is_lecturer_mode():
        return RunTimeTestConfigurations._lecturer_mode
