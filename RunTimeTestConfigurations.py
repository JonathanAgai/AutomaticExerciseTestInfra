

class RunTimeTestConfigurations:
    # public static member that holds whether tests are to be run in lecturer_mode
    _lecturer_mode = False

    @staticmethod
    def set_is_lecturer_mode(lecturer_mode: bool):
        RunTimeTestConfigurations._lecturer_mode = lecturer_mode

    @staticmethod
    def get_is_lecturer_mode():
        return RunTimeTestConfigurations._lecturer_mode
