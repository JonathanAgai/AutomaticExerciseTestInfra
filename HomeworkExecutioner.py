"""
iteratre over each solution, run it, and create test_case_runner
hand over all test case runner to report Generator

"""

import os
from subprocess import Popen
from ReportGenerator import *
from TestcaseRunner import *



class HomeWorkExecutioner:
    def __init__(self, students_solution_folder_path, results_report_path, test_configurations_path):
        self.students_solution_folder_path = students_solution_folder_path
        self.results_report_path = results_report_path
        self.test_case_runner = TestcaseRunner(test_configurations_path)

        self.students_id = self.extract_student_ids() # ['308418367']  # add homeworkexe extract students ids from students solution dir
        self.report_headers = TestConfigurationParser.extract_features_headers(test_configurations_path)

    def extract_student_ids(self):
        students_id = []
        for student_id in os.listdir(self.students_solution_folder_path):
            student_id_dir_path = os.path.join(self.students_solution_folder_path, student_id)
            if os.path.isdir(student_id_dir_path):
                students_id.append(student_id)
        return students_id

    def run(self):
        students_data = []
        for student_id in self.students_id:
            student_id_dir_path = os.path.join(self.students_solution_folder_path, student_id)
            student_exe_path = os.path.join(student_id_dir_path, student_id + '.py')
            print(student_exe_path)
            cmd = ['python.exe', student_exe_path]
            p = Popen(cmd)
            student_data = self.test_case_runner.run(student_id)
            students_data.append(student_data.generate_data())
            p.terminate()
        report_generator = ReportGenerator(self.results_report_path, students_data, self.report_headers)
        report_generator.generate_report()


