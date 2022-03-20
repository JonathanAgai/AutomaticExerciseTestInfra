"""
class containing:
  string - student ID
  dict/list - amount of score recv for each feature
  dict/list - summery for each feature
  string - final score
"""


class StudentData:
    def __init__(self, student_id: str, features_scores: list, features_reviews: list, final_score: str):
        self.student_id = student_id
        self.features_scores = features_scores
        self.features_reviews = features_reviews
        self.final_score = final_score

    # assume each feature score is "x/y"
    # def calculate_final_score(self):
    #     x, y = 0, 0
    #     for score in self.features_scores:
    #         x_cur, y_cur = score.split("/")
    #         x += int(x_cur)
    #         y += int(y_cur)
    #     final_score = str(x) + "/" + str(y)
    #     return final_score

    def generate_data(self):
        data = [self.student_id]
        for score, test_reviews in zip(self.features_scores, self.features_reviews):
            test_reviews_str = '\n'.join(test_reviews)
            data.append(score)
            data.append(test_reviews_str)
        data.append(self.final_score)
        return data

    def print(self):
        print(f"student_id: {self.student_id},")
        for feature_score, feature_review in zip(self.features_scores, self.features_reviews):
            print(f"feature_score: {feature_score}, feature_review: {feature_review}")
        print(f"final_score: {self.final_score}")


