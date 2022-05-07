from StudentData import StudentData
from TestConfigurationParser import *
import time


class TestcaseRunner:
    # TODO documentation
    """
        write in one line class description here

        write long description of class here

        Attributes
        ----------
        features : write the parameter's type here
            write parameter description here
        final_score : write the parameter's type here
            write parameter description here
        features_scores : write the parameter's type here
            write parameter description here
        features_reviews : write the parameter's type here
            write parameter description here
        test_configurations_path : write the parameter's type here
            write parameter description here

        Methods
        -------
        set_configurations(test_configurations_path)
            write function description here
        run(student_id) -> StudentData
            write function description here
        calculate_final_score()
            write function description here
        print()
            write function description here
        """
    def __init__(self, test_configurations_path=None):
        # TODO documentation
        """
        __init__(...) write function description here
        :param test_configurations_path: write parameter description here
        :type test_configurations_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.features = None
        self.final_score = ''
        self.features_scores = []
        self.features_reviews = []
        self.test_configurations_path = test_configurations_path

    def set_configurations(self, test_configurations_path):
        # TODO documentation
        """
        set_configurations(...) write function description here
        :param test_configurations_path: write parameter description here
        :type test_configurations_path: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.features = TestConfigurationParser.extract_features(test_configurations_path)

    def run(self, student_id) -> StudentData:
        # TODO documentation
        """
        run(...) write function description here
        :param student_id: write parameter description here
        :type student_id: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.features_scores.clear()
        self.features_reviews.clear()
        self.final_score = "N/A"

        if not self.try_to_find_gui_elements(1, 10):

            if len(self.features) == 0:
                self.features_scores.append('0/0')
                self.features_reviews.append('score: 0/0, could not find tests features and gui elements')
            else:
                for _ in range(len(self.features)):
                    self.features_scores.append('0/0')
                    self.features_reviews.append('score: 0/0, could not find gui elements')
            self.final_score = '0.0/100.0'

            return StudentData(student_id, self.features_scores, self.features_reviews, self.final_score)

        self.set_configurations(self.test_configurations_path)

        for feature in self.features:
            feature.run_tests(student_id)
            # total score
            self.features_scores.append(feature.get_feature_score())
            # list of test reviews
            self.features_reviews.append(feature.get_feature_review())
        self.calculate_final_score()

        return StudentData(student_id, self.features_scores, self.features_reviews, self.final_score)

    def calculate_final_score(self):
        # TODO documentation
        """
        calculate_final_score(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        x, y = 0, 0
        flat_list = []
        for score in self.features_scores:
            flat_list.append(score)
        for score in flat_list:
            x_cur, y_cur = score.split("/")
            x += float(x_cur)
            y += float(y_cur)

        x = round(x, 2)
        y = round(y, 2)
        final_score = str(x) + "/" + str(y)
        self.final_score = final_score

    def try_to_find_gui_elements(self, sleep_interval_sec, num_retries):
        gui_config = GUIConfigurations.get_instance()
        for i in range(num_retries):
            found_gui_elements = gui_config.find_gui_elements()
            if found_gui_elements is True:
                print(f"Found Gui elements on {i} iteration")
                return True
            print(f"Failed to find Gui elements for {i} iteration, going to sleep for: {sleep_interval_sec}")
            time.sleep(sleep_interval_sec)

        print(f"Failed to find Gui elements after {num_retries} iteration")
        return False

    def print(self):
        # TODO documentation
        """
        print(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        for feature in self.features:
            feature.print()


