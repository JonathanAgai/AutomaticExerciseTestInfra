class Feature:
    def __init__(self, tests, score_percent):
        self.tests = tests
        self.score_percent = score_percent

    def get_score(self):
        success_tests = 0
        num_tests = len(self.tests)
        for test in self.tests:
            if test.success:
                success_tests += 1

        return self.score_percent * success_tests / num_tests

    def run_tests(self):
        #TODO clear keyboard after each test or add clear key board as an operation
        for test in self.tests:
            test.run()

    def print(self):
        print(f"score percent = {self.score_percent}")
        for test in self.tests:
            test.print()

