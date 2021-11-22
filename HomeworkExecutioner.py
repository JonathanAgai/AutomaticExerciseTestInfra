"""
iteratre over each solution, run it, and create test_case_runner
hand over all test case runner to report Generator

"""

import os
import importlib
import ReportGenerator
import TestcaseRunner


class HomeWorkExecutioner:
    def __init__(self, student_solution_folder_path, result_path, exercise_json_operation_path):
        self.student_solution_folder_path = student_solution_folder_path
        self.result_path = result_path
        self.exercise_json_operation_path = exercise_json_operation_path

        # Assuming all students gives their IDs as names
        students = os.listdir(student_solution_folder_path)  # Gives a list of all files in a directory
        self.students_ids = {student.replace('.py', '') for student in students}  # Remove the .py suffix

        # Create test case runners
        self.test_case_runners = []
        # TODO add test case runner extract all features here
        for student in self.students_ids:
            self.test_case_runners.append(TestcaseRunner(student, self.exercise_json_operation_path))

        # Create report generator
        self.report_generator = ReportGenerator(self.result_path)

        # Create list of solution paths
        self.student_solution_paths = "%%%" % (self.student_solution_folder_path, '.', students)

    def run(self):
        students_data = []
        for student_solution_path, test_case_runner, student_id \
                in self.student_solution_paths, self.test_case_runners, self.students_ids:
            run_student_solution(student_solution_path, student_id)
            test_case_runner.run()
            students_data.append(test_case_runner.get_results())
            # kill(student_solution_path)  # ??? #TODO add terminate solution
        self.report_generator.generate_report(student_solution_path)


def run_student_solution(student_solution_path, student_id):
    spec = importlib.util.spec_from_file_location(student_id, student_solution_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
