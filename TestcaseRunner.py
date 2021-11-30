from StudentData import StudentData


class TestcaseRunner:

    def __init__(self, student_id, features, json_configuration_file_path):
        self.student_id = student_id
        self.json_configuration_file_path = json_configuration_file_path
        self.features = features
        self.final_score = 0
        self.features_scores = []
        self.features_headers = []

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


