from report.StudentData import StudentData
from TestConfigurationParser import *
import time


class TestcaseRunner:
    """
        A component that contains the features and configurations required to run the tests

        Attributes
        ----------
        features
        final_score
        features_scores
        features_reviews
        test_configurations_path

        Methods
        -------
        set_configurations(test_configurations_path)
        run(student_id) -> StudentData
        calculate_final_score()
        print()
        """
    def __init__(self, test_configurations_path=None):

        self.features = None
        self.final_score = ''
        self.features_scores = []
        self.features_reviews = []
        self.test_configurations_path = test_configurations_path

    def set_configurations(self, test_configurations_path):
        """
        set_configurations(...) extract features from configuration file
        :param test_configurations_path: configuration path file
        :type test_configurations_path: string
        :return: None
        """
        self.features = TestConfigurationParser.extract_features(test_configurations_path)

    def run(self, student_id) -> StudentData:
        """
        run(...) Extract the required features, and run a set of tests on each feature
        :param student_id: student id
        :type student_id: string
        :return: student data
        :rtype: Class StudentData
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
        """
        calculate_final_score(...) student's final score calculation
        :return: None
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
        """
        try_to_find_gui_elements(...) Attempts to locate the GUI elements
        :param sleep_interval_sec: amount of seconds for sleep
        :type sleep_interval_sec: time
        :param num_retries: number of tries
        :type num_retries: int
        :return: True if the elements has been found, False otherwise
        :rtype: bool
        """
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
        for feature in self.features:
            feature.print()


