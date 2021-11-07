"""
class containing:
  string - student ID
  dict/list - amount of score recv for each feature
  dict/list - summery for each feature
  string - final score
"""


class StudentData:
    def __init__(self, student_id: str, features_scores: list, features_reviews: list):
        self.student_id = student_id
        self.features_scores = features_scores
        self.features_reviews = features_reviews

    def __init__(self, output_path):
        self.output_path = output_path

    # assume each feature score is "x/y"
    def calculate_final_score(self):
        x, y = 0, 0
        for score in self.features_scores:
            x_cur, y_cur = score.split("/")
            x += int(x_cur)
            y += int(y_cur)
        final_score = str(x) + "/" + str(y)
        return final_score

    def generate_data(self):
        data = [self.student_id]
        for score, review in zip(self.features_scores, self.features_reviews):
            data.append(score)
            data.append(review)
        data.append(self.calculate_final_score())
        return data

