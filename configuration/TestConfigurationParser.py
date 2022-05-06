import json
from Operation import *
from Test import *
from Feature import *


def parse_features_headers(data):
    # TODO documentation
    """
    parse_features_headers(...) write function description here
    :param data: write parameter description here
    :type data: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    features_headers = ['student ids']

    json_features = data["features"]
    for feature_name, feature_tests in json_features.items():
        feature_name = feature_name.replace("_", " ")
        # features_headers.append(f'{feature_name} score')
        features_headers.append(f'{feature_name} review')

    features_headers.append('final score')
    return features_headers


def parse_features(data):
    # TODO documentation
    """
    parse_features(...) write function description here
    :param data: write parameter description here
    :type data: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    json_features = data["features"]
    num_features = len(json_features.keys())
    features = []
    print("***************START PARSE TEST CONFIGURATION********************")
    for feature_name, feature_tests in json_features.items():
        print(f"Parsing Feature:{feature_name}")

        tests = []
        for test_name, test_values in feature_tests.items():
            print(f"Parsing test:{test_name}")
            test = parse_test(test_name, test_values)
            tests.append(test)
            print(f"finish Test parsing: {test_name}")

        feature_score_percent = 1 / num_features
        feature = Feature(tests, feature_score_percent)
        features.append(feature)
        print(f"finish Feature parsing: {feature_name}")

    print("***************FINISH PARSE TEST CONFIGURATION********************")
    return features


def parse_test(test_name, test_values):
    # TODO documentation
    """
    parse_test(...) write function description here
    :param test_name: write parameter description here
    :type test_name: write the parameter's type here
    :param test_values: write parameter description here
    :type test_values: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    operations = extract_test_configuration_operations(test_values["operations"])
    result = test_values["result"]
    cropped_element_name = result["cropped_element_name"]
    cropped_area_img_path = RunTimeTestConfigurations.get_solution_screenshot_imgs_path()
    hw_path = RunTimeTestConfigurations.get_hw_path()
    string_test_name = test_name.replace("_", " ")
    expected_result = f"configuration/{hw_path}/lecturer_solution/templates/{string_test_name}.png"
    test = Test(operations, expected_result, cropped_element_name, cropped_area_img_path, test_name)
    return test


def extract_xy_from_operation(element_name_operation, gui_config):
    # TODO documentation
    """
    extract_xy_from_operation(...) write function description here
    :param element_name_operation: write parameter description here
    :type element_name_operation: write the parameter's type here
    :param gui_config: write parameter description here
    :type gui_config: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    element_name = element_name_operation.split("-input")[0]
    if "-input" in element_name_operation:
        x, y = gui_config.get_elements_input_xy(element_name)
    else:
        x, y = gui_config.get_elements_xy(element_name)
    return x, y


def extract_operation_value(element_name_operation):
    # TODO documentation
    """
    extract_operation_value(...) write function description here
    :param element_name_operation: write parameter description here
    :type element_name_operation: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    values_str = element_name_operation.split("-")[0]
    if len(values_str) == 3:
        return int(values_str[-1])

    return None


def parse_operation_value(operation_value_str):
    # TODO documentation
    """
    parse_operation_value(...) write function description here
    :param operation_value_str: write parameter description here
    :type operation_value_str: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    values_str = operation_value_str.split("-")
    element_name = values_str[0]
    use_input = False
    operation_value_number = None

    if len(values_str) == 2:
        if values_str[1] == "input":
            use_input = True
        else:
            operation_value_number = int(values_str[1])
    elif len(values_str) == 3:
        if values_str[1] != "input":
            print(f"Invalid Line value:{operation_value_str}, when having 3 arguments - the middle must be input")
            return None

        use_input = True
        operation_value_number = int(values_str[2])
    # else:
    #     print(f"Invalid Line value:{operation_value_str}, invalid number of arguments: {len(values_str)}")
    #     return None

    print(f"Parse {operation_value_str} into -> {element_name},{use_input},{operation_value_number}")
    return element_name, use_input, operation_value_number


def parse_generic_click_operation(gui_config, element_name, use_input, operation_value_number):
    # TODO documentation
    """
    parse_generic_click_operation(...) write function description here
    :param gui_config: write parameter description here
    :type gui_config: write the parameter's type here
    :param element_name: write parameter description here
    :type element_name: write the parameter's type here
    :param use_input: write parameter description here
    :type use_input: write the parameter's type here
    :param operation_value_number: write parameter description here
    :type operation_value_number: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    if operation_value_number is not None and use_input is False:
        print(f"Invalid Click operation trying to work on operation_value={operation_value_number}, use_input={use_input}")
        return None

    if use_input:
        x, y = gui_config.get_elements_input_xy(element_name, operation_value_number)
    else:
        x, y = gui_config.get_elements_xy(element_name)

    return x, y


def parse_click_operation(gui_config, element_name, use_input, operation_value_number):
    # TODO documentation
    """
    parse_click_operation(...) write function description here
    :param gui_config: write parameter description here
    :type gui_config: write the parameter's type here
    :param element_name: write parameter description here
    :type element_name: write the parameter's type here
    :param use_input: write parameter description here
    :type use_input: write the parameter's type here
    :param operation_value_number: write parameter description here
    :type operation_value_number: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    x, y = parse_generic_click_operation(gui_config, element_name, use_input, operation_value_number)
    return Click(x, y)


def parse_double_click_operation(gui_config, element_name, use_input, operation_value_number):
    # TODO documentation
    """
    parse_double_click_operation(...) write function description here
    :param gui_config: write parameter description here
    :type gui_config: write the parameter's type here
    :param element_name: write parameter description here
    :type element_name: write the parameter's type here
    :param use_input: write parameter description here
    :type use_input: write the parameter's type here
    :param operation_value_number: write parameter description here
    :type operation_value_number: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    x, y = parse_generic_click_operation(gui_config, element_name, use_input, operation_value_number)
    return DoubleClick(x, y)


def parse_scroll_up_operation(gui_config, element_name, operation_value_number):
    # TODO documentation
    """
    parse_scroll_up_operation(...) write function description here
    :param gui_config: write parameter description here
    :type gui_config: write the parameter's type here
    :param element_name: write parameter description here
    :type element_name: write the parameter's type here
    :param operation_value_number: write parameter description here
    :type operation_value_number: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    if operation_value_number is None:
        return None
    x, y = gui_config.get_elements_xy_scroll_up(element_name)
    num_clicks = operation_value_number
    return ScrollUp(num_clicks, x, y)


def parse_scroll_down_operation(gui_config, element_name, operation_value_number):
    # TODO documentation
    """
    parse_scroll_down_operation(...) write function description here
    :param gui_config: write parameter description here
    :type gui_config: write the parameter's type here
    :param element_name: write parameter description here
    :type element_name: write the parameter's type here
    :param operation_value_number: write parameter description here
    :type operation_value_number: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    if operation_value_number is None:
        return None
    x, y = gui_config.get_elements_xy_scroll_down(element_name)
    num_clicks = operation_value_number
    return ScrollDown(num_clicks, x, y)


def extract_test_configuration_operations(test_operations):
    # TODO documentation
    """
    extract_test_configuration_operations(...) write function description here
    :param test_operations: write parameter description here
    :type test_operations: write the parameter's type here
    :return: write return value and description here or write None if it doesn't have return value.
    :rtype: write the type of the return parameter here
    """
    gui_config = GUIConfigurations.get_instance()

    operations = []
    for operation in test_operations:
        for operation_name, operation_value_str in operation.items():
            operation = None
            print(f"Parsing Operation: {operation_name}")
            if operation_name == "click":
                element_name, use_input, operation_value_number = parse_operation_value(operation_value_str)
                operation = parse_click_operation(gui_config, element_name, use_input, operation_value_number)

            elif operation_name == "double_click":
                element_name, use_input, operation_value_number = parse_operation_value(operation_value_str)
                operation = parse_double_click_operation(gui_config, element_name, use_input, operation_value_number)

            elif operation_name == "keyboard":
                operation = Keyboard(operation_value_str)

            elif operation_name == "delete":
                operation = Delete()

            elif operation_name == "scroll_up":
                element_name, _, operation_value_number = parse_operation_value(operation_value_str)
                operation = parse_scroll_up_operation(gui_config, element_name, operation_value_number)

            elif operation_name == "scroll_down":
                element_name, _, operation_value_number = parse_operation_value(operation_value_str)
                operation = parse_scroll_down_operation(gui_config, element_name, operation_value_number)

            if operation is None:
                print("Invalid None Operation: Exit")
                return None

            operations.append(operation)
    return operations


class TestConfigurationParser:
    # TODO documentation
    """
        write in one line class description here

        write long description of class here

        Attributes
        ----------


        Methods
        -------
        calculate_score()
            write function description here
        initialize(test_configuration_path, images_dir_path)
            write function description here
        get_config_data(test_configuration_path)
            write function description here
        extract_features_headers(test_configuration_path)
            write function description here
        extract_features(test_configuration_path)
            write function description here
        extract_features(test_configuration_path)
            write function description here
        extract_gui_elements(test_configuration_path)
            write function description here

        """
    # Private static member that holds inner configuration data
    _data = None

    @staticmethod
    def initialize(test_configuration_path, images_dir_path):
        # TODO documentation
        """
        initialize(...) write function description here
        :param test_configuration_path: write parameter description here
        :type test_configuration_path: write the parameter's type here
        :param images_dir_path: write parameter description here
        :type images_dir_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        data = TestConfigurationParser.get_config_data(test_configuration_path)
        gui_elements = data["gui_elements"]
        GUIConfigurations.initialize(gui_elements, images_dir_path)

    @staticmethod
    def get_config_data(test_configuration_path):
        # TODO documentation
        """
        get_config_data(...) write function description here
        :param test_configuration_path: write parameter description here
        :type test_configuration_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        if TestConfigurationParser._data is not None:
            return TestConfigurationParser._data

        with open(test_configuration_path, "r") as f:
            TestConfigurationParser._data = json.load(f)

        return TestConfigurationParser._data

    @staticmethod
    def extract_features_headers(test_configuration_path):
        # TODO documentation
        """
        extract_features_headers(...) write function description here
        :param test_configuration_path: write parameter description here
        :type test_configuration_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        data = TestConfigurationParser.get_config_data(test_configuration_path)
        return parse_features_headers(data)

    @staticmethod
    def extract_features(test_configuration_path):
        # TODO documentation
        """
        extract_features(...) write function description here
        :param test_configuration_path: write parameter description here
        :type test_configuration_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        data = TestConfigurationParser.get_config_data(test_configuration_path)
        return parse_features(data)

    @staticmethod
    def extract_features(test_configuration_path):
        # TODO documentation
        """
        extract_features(...) write function description here
        :param test_configuration_path: write parameter description here
        :type test_configuration_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        data = TestConfigurationParser.get_config_data(test_configuration_path)
        return parse_features(data)

    @staticmethod
    def extract_gui_elements(test_configuration_path):
        # TODO documentation
        """
        extract_gui_elements(...) write function description here
        :param test_configuration_path: write parameter description here
        :type test_configuration_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        data = TestConfigurationParser.get_config_data(test_configuration_path)
        return data["gui_elements"]
