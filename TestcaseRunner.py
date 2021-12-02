from StudentData import StudentData


class TestcaseRunner:

    def __init__(self, student_id, features, json_configuration_file_path):
        self.student_id = student_id
        self.json_configuration_file_path = json_configuration_file_path
        self.features = features
        self.final_score = ''
        self.features_scores = []
        self.features_reviews = []

    def run(self):
        for feature in self.features:
            feature.run_tests()
            self.features_scores.append(feature.get_feature_score())
            self.features_reviews.append(feature.get_feature_review())
        self.calculate_final_score()

    def get_results(self):
        sd = StudentData(self.student_id, self.features_scores, self.features_reviews, self.final_score)
        return sd.generate_data()

    def calculate_final_score(self):
        x, y = 0, 0
        flat_list = []
        for score in self.features_scores:
            flat_list += score
        for score in flat_list:
            x_cur, y_cur = score.split("/")
            x += float(x_cur)
            y += float(y_cur)
        final_score = str(x) + "/" + str(y)
        self.final_score = final_score

    def print(self):
        for feature in self.features:
            feature.print()


