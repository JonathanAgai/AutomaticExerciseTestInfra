import time
import json


def extract_operations(test_operations):
    operations = []
    for operation in test_operations:
        for operation_name, values in operation.items():
            print(f"{operation_name}: {operation}")
            if operation_name == "click":
                operation = Click(values[0], values[1])
            elif operation_name == "keyboard":
                operation = Keyboard(values)

            operations.append(operation)
    return operations


#TODO extract all features: json configuration - move it to homeworkexecutioner

class TestcaseRunner:

    def __init__(self, student_id, json_configuration_file_path):
        self.student_id = student_id
        self.json_configuration_file_path = json_configuration_file_path
        self.features = extract_features()
        self.final_score = 0
        self.features_scores = []
        self.features_reviews = []

    def extract_features(self):
        with open(self.json_configuration_file_path, "r") as f:
            data = json.load(f)
        num_features = len(data.keys())

        features = []
        for feature_name, feature_tests in data.items():
            print(feature_name)
            tests = []
            for test_name, test_values in feature_tests.items():
                print(test_name)
                operations = extract_operations(test_values["operations"])
                result = test_values["result"]
                cropped_area = result["crop_area"]
                expected_result = result["expected_result"]
                test = Test(operations, expected_result, cropped_area)
                tests.append(test)

            feature = Feature(tests, 100 / num_features)
            features.append(feature)
        return features

    def run(self):
        for feature in self.features:
            feature.run_tests()
        calculate_scores()

    def calculate_scores(self):
        for feature in self.features:
            self.feature_scores.append(feature.get_score())
        self.final_score = round(sum(feature_scores))

    def get_results(self):
        student_data = StudentData(self.student_id, self.features_scores, self.features_reviews)
        return student_data

    def print(self):
        for feature in self.features:
            feature.print()


