from HomeworkExecutioner import *
from RunTimeTestConfigurations import *


if __name__ == '__main__':
    hw_path = "hw1"
    RunTimeTestConfigurations.set_hw_path(hw_path)
    RunTimeTestConfigurations.set_is_lecturer_mode(False)

    json_configuration_file_path = f'./configuration/{hw_path}/tests_configurations.json'

    gui_elements_images_path = f"configuration/{hw_path}/gui_elements_images"
    TestConfigurationParser.initialize(json_configuration_file_path, gui_elements_images_path)

    students_solution_folder_path = 'students_solution_execs'
    results_report_path = 'results_report'
    homework_exe = HomeWorkExecutioner(students_solution_folder_path,
                                       results_report_path,
                                       json_configuration_file_path)

    homework_exe.run()

