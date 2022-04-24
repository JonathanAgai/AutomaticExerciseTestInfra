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

    def generate_data(self):
        data = [self.student_id]
        for score, test_reviews in zip(self.features_scores, self.features_reviews):
            data.append(score)
            if "_" in test_reviews:
                test_reviews_str = '\n'.join(test_reviews)
                test_reviews_str = test_reviews_str.replace("_", " ")
                data.append(test_reviews_str)
            else:
                data.append(test_reviews)

        data.append(self.final_score)
        return data

    def print(self):
        print(f"student_id: {self.student_id},")
        for feature_score, feature_review in zip(self.features_scores, self.features_reviews):
            print(f"feature_score: {feature_score}, feature_review: {feature_review}")
        print(f"final_score: {self.final_score}")


