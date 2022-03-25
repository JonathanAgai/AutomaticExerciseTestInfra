from HomeworkExecutioner import *
from RunTimeTestConfigurations import *

running_lecturer_solution = True


if __name__ == '__main__':

    if running_lecturer_solution:
        json_configuration_file_path = 'configuration/Lecturer_Solution.json'
    else:
        json_configuration_file_path = './configuration/Student_Solution.json'

    students_solution_folder_path = 'students_solution_execs'
    results_report_path = 'results_report'
    homework_exe = HomeWorkExecutioner(students_solution_folder_path,
                                       results_report_path,
                                       json_configuration_file_path)

    RunTimeTestConfigurations.set_is_lecturer_mode(running_lecturer_solution)

    homework_exe.run()

