import os
from subprocess import Popen
from TestcaseRunner import *


class HomeWorkExecutioner:
    """
    This component is responsible for finding the student solutions and
    distinguishing them according to the ID number of each student, running any solution it finds to run a test set,
    once the test set is complete the component will kill the program and move on to the next program.

    Attributes
    ----------
    students_solution_folder_path
    results_report_path
    test_case_runner
    students_id
    report_headers

    Methods
    -------
    extract_student_ids()
    run(student_id)
    """
    def __init__(self, students_solution_folder_path, test_configurations_path):

        self.students_solution_folder_path = students_solution_folder_path
        self.test_case_runner = TestcaseRunner(test_configurations_path)
        self.students_id = self.extract_student_ids()

    def extract_student_ids(self):
        """
        extract_student_ids(...) Extraction of students' ID
        :return: students id's
        :rtype: list of strings
        """
        students_id = []
        for student_id in os.listdir(self.students_solution_folder_path):
            student_id_dir_path = os.path.join(self.students_solution_folder_path, student_id)
            if os.path.isdir(student_id_dir_path):
                students_id.append(student_id)
        return students_id

    def run(self):
        """
        run(...) iterate over each student solution, run it, and create test_case_runner
        To run the tests and transfer the data produced to report Generator
        :return: None
        """
        students_data = []
        for student_id in self.students_id:
            student_id_dir_path = os.path.join(self.students_solution_folder_path, student_id)
            student_exe_path = os.path.join(student_id_dir_path, student_id + '.py')
            print(student_exe_path)

            cmd = ['python.exe', student_exe_path]
            p = Popen(cmd)
            time.sleep(1)

            student_data = self.test_case_runner.run(student_id)
            students_data.append(student_data.generate_data())

            p.terminate()

        return students_data


