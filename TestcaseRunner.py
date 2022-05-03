from StudentData import StudentData
from TestConfigurationParser import *


class TestcaseRunner:
    def __init__(self, test_configurations_path=None):

        self.features = None
        self.final_score = ''
        self.features_scores = []
        self.features_reviews = []
        self.test_configurations_path = test_configurations_path

        # if test_configurations_path is not None:
        #     self.set_configurations(test_configurations_path)

    def set_configurations(self, test_configurations_path):
        self.features = TestConfigurationParser.extract_features(test_configurations_path)

    def run(self, student_id) -> StudentData:
        self.features_scores.clear()
        self.features_reviews.clear()
        self.final_score = "N/A"

        gui_config = GUIConfigurations.get_instance()
        if not gui_config.find_gui_elements():
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

    def print(self):
        for feature in self.features:
            feature.print()


