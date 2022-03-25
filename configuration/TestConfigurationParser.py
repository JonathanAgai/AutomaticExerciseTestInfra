import json
from Operation import *
from Test import *
from Feature import *


def parse_features_headers(data):
    features_headers = ['student_ids']

    json_features = data["features"]
    for feature_name, feature_tests in json_features.items():
        features_headers.append(f'{feature_name}_score')
        features_headers.append(f'{feature_name}_review')

    features_headers.append('final_score')
    return features_headers


def parse_features(data):
    json_features = data["features"]
    num_features = len(json_features.keys())
    features = []
    for feature_name, feature_tests in json_features.items():
        print(feature_name)

        tests = []
        for test_name, test_values in feature_tests.items():
            print(test_name)
            test = parse_test(test_name, test_values)
            tests.append(test)

        feature_score_percent = 1 / num_features
        feature = Feature(tests, feature_score_percent)
        features.append(feature)
    return features


def parse_test(test_name, test_values):
    operations = extract_test_configuration_operations(test_values["operations"])
    result = test_values["result"]
    cropped_area = result["crop_area"]
    cropped_area_img_path = result["crop_area_img_path"]
    expected_result = result["expected_result"]
    test = Test(operations, expected_result, cropped_area, cropped_area_img_path, test_name)
    return test


def extract_test_configuration_operations(test_operations):
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


class TestConfigurationParser:
    # Private static member that holds inner configuration data
    _data = None

    @staticmethod
    def get_config_data(test_configuration_path):
        if TestConfigurationParser._data is not None:
            return TestConfigurationParser._data

        with open(test_configuration_path, "r") as f:
            TestConfigurationParser._data = json.load(f)

        return TestConfigurationParser._data

    @staticmethod
    def extract_features_headers(test_configuration_path):
        data = TestConfigurationParser.get_config_data(test_configuration_path)
        return parse_features_headers(data)

    @staticmethod
    def extract_features(test_configuration_path):
        data = TestConfigurationParser.get_config_data(test_configuration_path)
        return parse_features(data)

    @staticmethod
    def extract_features(test_configuration_path):
        data = TestConfigurationParser.get_config_data(test_configuration_path)
        return parse_features(data)

    @staticmethod
    def extract_gui_elements(test_configuration_path):
        data = TestConfigurationParser.get_config_data(test_configuration_path)
        return data["gui_elements"]
