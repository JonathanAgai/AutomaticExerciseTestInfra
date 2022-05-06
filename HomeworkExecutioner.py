"""
iteratre over each solution, run it, and create test_case_runner
hand over all test case runner to report Generator

"""

import os
import time
from subprocess import Popen
from ReportGenerator import *
from TestcaseRunner import *


class HomeWorkExecutioner:
    # TODO documentation
    """
        write in one line class description here

        write long description of class here

        Attributes
        ----------
        students_solution_folder_path : write the parameter's type here
            write parameter description here
        results_report_path : write the parameter's type here
            write parameter description here
        test_case_runner : write the parameter's type here
            write parameter description here
        students_id : write the parameter's type here
            write parameter description here
        report_headers : write the parameter's type here
            write parameter description here

        Methods
        -------
        extract_student_ids()
            write function description here
        run(student_id)
            write function description here
        """
    def __init__(self, students_solution_folder_path, results_report_path, test_configurations_path):
        # TODO documentation
        """
        __init__(...) write function description here
        :param students_solution_folder_path: write parameter description here
        :type students_solution_folder_path: write the parameter's type here
        :param results_report_path: write parameter description here
        :type results_report_path: write the parameter's type here
        :param test_configurations_path: write parameter description here
        :type test_configurations_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.students_solution_folder_path = students_solution_folder_path
        self.results_report_path = results_report_path
        self.test_case_runner = TestcaseRunner(test_configurations_path)

        self.students_id = self.extract_student_ids() # ['308418367']  # add homeworkexe extract students ids from students solution dir
        self.report_headers = TestConfigurationParser.extract_features_headers(test_configurations_path)

    def extract_student_ids(self):
        # TODO documentation
        """
        extract_student_ids(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        students_id = []
        for student_id in os.listdir(self.students_solution_folder_path):
            student_id_dir_path = os.path.join(self.students_solution_folder_path, student_id)
            if os.path.isdir(student_id_dir_path):
                students_id.append(student_id)
        return students_id

    def run(self):
        # TODO documentation
        """
        run(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        students_data = []
        for student_id in self.students_id:
            student_id_dir_path = os.path.join(self.students_solution_folder_path, student_id)
            student_exe_path = os.path.join(student_id_dir_path, student_id + '.py')
            print(student_exe_path)

            cmd = ['python.exe', student_exe_path]
            p = Popen(cmd)
            time.sleep(5)

            student_data = self.test_case_runner.run(student_id)
            students_data.append(student_data.generate_data())

            p.terminate()

        report_generator = ReportGenerator(self.results_report_path, students_data, self.report_headers)
        report_generator.generate_report()


