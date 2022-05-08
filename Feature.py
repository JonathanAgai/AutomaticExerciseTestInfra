class Feature:
    """
    A feature that contains tests, reviews and a scores

    Attributes
    ----------
    tests
    score_percent
    feature_reviews
    feature_score

    Methods
    -------
    calculate_score()
    run_tests(student_id)
    get_feature_review()
    get_feature_score()
    print()
    """
    def __init__(self, tests, score_percent):

        self.tests = tests
        self.score_percent = score_percent
        self.feature_reviews = []
        self.feature_score = -1

    def calculate_score(self):
        """
        calculate_score(...) Calculation of the score according to the number of tests passed successfully
        :return: None
        """
        success_tests = 0
        num_tests = len(self.tests)
        for test in self.tests:
            if test.success:
                success_tests += 1

        feature_total_score = self.score_percent * 100

        feature_score = success_tests / num_tests * feature_total_score
        feature_score = round(feature_score, 2)

        self.feature_score = f"{feature_score} / {feature_total_score}"

    def run_tests(self, student_id):
        """
        run_tests(...) Running tests for each feature according to the student's ID and calculating score
        :param student_id:
        :type student_id: string
        :return: None
        """
        self.feature_score = "-1"
        self.feature_reviews.clear()
        for test in self.tests:
            test.run(student_id)
            if not test.success:
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

