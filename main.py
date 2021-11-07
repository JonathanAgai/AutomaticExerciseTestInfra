import time
import json


def is_images_the_same(img1, img2) -> bool:
    return False


def extract_operations_from_test_json(test_operations):
    operations = []
    for operation in test_operations:
        for operation_name, values in operation.items():
            print(f"{operation_name}: {operation}")
            if operation_name == "click":
                operation = Click(values[0], values[1])
            elif operation_name == "keyboard":
                operation = Keyboard(values)

            operations.append(operation)

    time.sleep(5)
    for operation in operations:
        operation.execute()
        time.sleep(2)

    return operations


if __name__ == '__main__':
    with open("ShayExam.json", "r") as f:
        data = json.load(f)

    num_features = len(data.keys())

    features = []
    for feature_name, feature_tests in data.items():
        print(feature_name)
        tests = []
        for test_name, test_values in feature_tests.items():
            print(test_name)
            operations = extract_operations_from_test_json(test_values["operations"])
            json_result = test_values["result"]
            cropped_area = json_result["crop_area"]
            expected_result = json_result["expected_result"]
            test = Test(operations, expected_result, cropped_area)
            tests.append(test)

        feature = Feature(tests, 100 / num_features)
        features.append(feature)

    exercise = Exercise(features)
    exercise.print()


    # Code of Homework Executioner
    students_ids = ["2394234", "2394232", "23423434"]
    runners = []
    for sid in students_ids:
        # create data for student
        runner = TestCaseRunner(sid)
        # calculate score
        runner.run(exercise)
        # add to list of data saved
        runners.append(runner)



