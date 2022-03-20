from HomeworkExecutioner import *


running_lecturer_solution = False

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

    homework_exe.run(running_lecturer_solution)

