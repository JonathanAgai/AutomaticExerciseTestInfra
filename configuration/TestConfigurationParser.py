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
    cropped_element_name = result["cropped_element_name"]
    cropped_area_img_path = RunTimeTestConfigurations.get_solution_screenshot_imgs_path()
    hw_path = RunTimeTestConfigurations.get_hw_path()
    expected_result = f"configuration/{hw_path}/lecturer_solution/{test_name}.png"
    test = Test(operations, expected_result, cropped_element_name, cropped_area_img_path, test_name)
    return test


def extract_xy_from_operation(element_name_operation, gui_config):
    element_name = element_name_operation.split("-input")[0]
    if "-input" in element_name_operation:
        x, y = gui_config.get_elements_input_xy(element_name)
    else:
        x, y = gui_config.get_elements_xy(element_name)
    return x, y


def extract_test_configuration_operations(test_operations):
    gui_config = GUIConfigurations.get_instance()

    operations = []
    for operation in test_operations:
        for operation_name, values in operation.items():
            print(f"{operation_name}: {operation}")
            if operation_name == "click":
                # values of click operation is the element name to be clicked
                gui_element_name = values
                x, y = extract_xy_from_operation(gui_element_name, gui_config)
                operation = Click(x, y)
            elif operation_name == "keyboard":
                operation = Keyboard(values)
            elif operation_name == "double_click":
                gui_element_name = values
                x, y = extract_xy_from_operation(gui_element_name, gui_config)
                operation = DoubleClick(x, y)
            elif operation_name == "delete":
                operation = Delete()

            operations.append(operation)
    return operations


class TestConfigurationParser:
    # Private static member that holds inner configuration data
    _data = None

    @staticmethod
    def initialize(test_configuration_path, images_dir_path):
        data = TestConfigurationParser.get_config_data(test_configuration_path)
        gui_elements = data["gui_elements"]
        GUIConfigurations.initialize(gui_elements, images_dir_path)

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
