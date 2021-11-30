"""
iteratre over each solution, run it, and create test_case_runner
hand over all test case runner to report Generator

"""
import json
import os
import importlib
from multiprocessing import Process

import TestcaseRunner
# import ReportGenerator
from Feature import Feature
from Operation import Click, Keyboard, DoubleClick, Delete
from Test import Test


class HomeWorkExecutioner:
    def __init__(self, students_solution_folder_path, results_report_path, json_configuration_file_path, state):
        self.json_configuration_file_path = json_configuration_file_path
        self.students_solution_folder_path = students_solution_folder_path
        self.state = state
        self.students_ids = ['308418367']
        self.test_case_runners = self.init_test_case_runners() # Create test case runners
        # TODO self.report_generator = ReportGenerator(results_report_path)
        self.features_headers = []

        # TODO :
        #  Assuming all students gives their IDs as names
        # students = os.listdir(students_solution_folder_path)  # Gives a list of all files in a directory
        # self.students_ids = {student.replace('.py', '') for student in students}  # Remove the .py suffix
        # Create list of solution paths
        # self.student_solution_paths = "%%%" % (self.student_solution_folder_path, '.', students)

    def init_test_case_runners(self):
        test_case_runners = []
        features = self.extract_features()
        for student in self.students_ids:
            test_case_runners.append(TestcaseRunner.TestcaseRunner(student,
                                                                   features, self.json_configuration_file_path))
        return test_case_runners

    def extract_features(self):
        with open(self.json_configuration_file_path, "r") as f:
            data = json.load(f)
        num_features = len(data.keys())

        features = []
        for feature_name, feature_tests in data.items():
            # TODO add feature_name self.features_headers.append(feature_name)
            print(feature_name)

            tests = []
            for test_name, test_values in feature_tests.items():
                print(test_name)
                operations = extract_operations(test_values["operations"])
                result = test_values["result"]
                cropped_area = result["crop_area"]
                cropped_area_img_path = result["crop_area_img_path"]
                expected_result = result["expected_result"]
                test = Test(operations, expected_result, cropped_area, cropped_area_img_path, test_name, self.state)
                tests.append(test)

            feature = Feature(tests, 100 / num_features)
            features.append(feature)
        return features

    def run(self):
        students_data = []
        for student_solution in self.students_solution_folder_path:
            for test_case_runner in self.test_case_runners:
                for student_id in self.students_ids:
                    p = Process(target=run_student_solution, args=(student_solution, student_id))
                    p.start()
                    test_case_runner.run()
                    # TODO students_data.append(test_case_runner.get_results())
                    p.terminate()
        # TODO self.report_generator.generate_report(self.results_report_path)


def run_student_solution(student_solution_path, student_id):
    spec = importlib.util.spec_from_file_location(student_id, student_solution_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)


def extract_operations(test_operations):
    operations = []
    for operation in test_operations:
        for operation_name, values in operation.items():
            print(f"{operation_name}: {operation}")
            if operation_name == "click":
                operation = Click(values[0], values[1])
            elif operation_name == "keyboard":
                operation = Keyboard(values)
            elif operation_name == "double_click":
                operation = DoubleClick(values[0], values[1])
            elif operation_name == "delete":
                operation = Delete()

            operations.append(operation)
    return operations
