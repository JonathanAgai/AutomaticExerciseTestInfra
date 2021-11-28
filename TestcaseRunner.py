import time
import json

from Feature import Feature
from Operation import Click, Keyboard, DoubleClick, Delete
from StudentData import StudentData
from Test import Test


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


#TODO extract all features: json configuration - move it to homeworkexecutioner

class TestcaseRunner:

    def __init__(self, student_id, json_configuration_file_path, state):
        self.student_id = student_id
        self.json_configuration_file_path = json_configuration_file_path
        self.state = state
        self.features = self.extract_features()
        self.final_score = 0
        self.features_scores = []
        self.features_headers = []

    def extract_features(self):
        with open(self.json_configuration_file_path, "r") as f:
            data = json.load(f)
        num_features = len(data.keys())

        features = []
        for feature_name, feature_tests in data.items():
            print(feature_name)
            # TODO GET THIS LINE THE FUCK OUT OF HERE
            # self.features_headers.append((feature_name, f'{feature_name}_review'))
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

        for feature in self.features:
            feature.run_tests()
        self.calculate_scores()

    def calculate_scores(self):
        for feature in self.features:
            self.features_scores.append(feature.get_score())
        self.final_score = round(sum(self.features_scores))

    def get_results(self):
        student_data = StudentData(self.student_id, self.features_scores, self.features_reviews)
        return student_data

    def print(self):
        for feature in self.features:
            feature.print()


