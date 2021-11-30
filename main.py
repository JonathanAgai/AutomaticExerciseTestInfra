import HomeworkExecutioner


state = False

if __name__ == '__main__':
    if state:
        json_configuration_file_path = 'C:\\Users\\Ben\\PycharmProjects\\pythonProject\\Solutions.json'
    else:
        json_configuration_file_path = 'C:\\Users\\Ben\\PycharmProjects\\pythonProject\\ShayExam.json'

    students_solution_folder_path = []
    student_solution = 'C:\\Users\\Ben\\PycharmProjects\\pythonProject\\testing.py'
    students_solution_folder_path.append(student_solution)
    results_report_path = 'C:\\Users\\Ben\\Desktop\\results_report'
    homework_exe = HomeworkExecutioner.HomeWorkExecutioner(students_solution_folder_path,
                                                           results_report_path, json_configuration_file_path, state)

    homework_exe.run()

