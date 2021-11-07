

class TestCaseRunner:
    def __init__(self, student_id):
        self.student_id = student_id
        self.final_score = 0
        self.features_scores = []

    def run(self, exercise):
        self.final_score, self.features_scores = exercise.calculate_scores()