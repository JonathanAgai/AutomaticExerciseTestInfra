class Feature:
    def __init__(self, tests, score_percent):
        self.tests = tests
        self.score_percent = score_percent
        self.feature_reviews = []
        self.feature_score = []

    def calculate_score(self):
        success_tests = 0
        num_tests = len(self.tests)
        for test in self.tests:
            if test.success:
                success_tests += 1
                # TODO fix /100
        self.feature_score.append(f'{self.score_percent * success_tests / num_tests}/100')

    def run_tests(self, running_lecturer_solution):
        for test in self.tests:
            test.run(running_lecturer_solution)
            self.feature_reviews.append(test.get_review())
        self.calculate_score()

    def get_feature_review(self):
        return self.feature_reviews

    def get_feature_score(self):
        return self.feature_score

    def print(self):
        print(f"score percent = {self.score_percent}")
        for test in self.tests:
            test.print()

