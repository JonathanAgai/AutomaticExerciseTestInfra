class Feature:
    # TODO documentation
    """
        write in one line class description here

        write long description of class here

        Attributes
        ----------
        tests : write the parameter's type here
            write parameter description here
        score_percent : write the parameter's type here
            write parameter description here
        feature_reviews : write the parameter's type here
            write parameter description here
        feature_score : write the parameter's type here
            write parameter description here

        Methods
        -------
        calculate_score()
            write function description here
        run_tests(student_id)
            write function description here
        get_feature_review()
            write function description here
        get_feature_score()
            write function description here
        print()
            write function description here
        """
    def __init__(self, tests, score_percent):
        # TODO documentation
        """
        __init__(...) write function description here
        :param tests: write parameter description here
        :type tests: write the parameter's type here
        :param score_percent: write parameter description here
        :type score_percent: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.tests = tests
        self.score_percent = score_percent
        self.feature_reviews = []
        self.feature_score = -1

    def calculate_score(self):
        # TODO documentation
        """
        calculate_score(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
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
        # TODO documentation
        """
        run_tests(...) write function description here
        :param student_id: write parameter description here
        :type student_id: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.feature_score = "-1"
        self.feature_reviews.clear()
        for test in self.tests:
            test.run(student_id)
            if not test.success:
                self.feature_reviews.append(test.get_review())
        self.calculate_score()

    def get_feature_review(self):
        # TODO documentation
        """
        get_feature_review(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        return self.feature_reviews

    def get_feature_score(self):
        # TODO documentation
        """
        get_feature_score(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        return self.feature_score

    def print(self):
        # TODO documentation
        """
        print(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        print(f"score percent = {self.score_percent}")
        for test in self.tests:
            test.print()

