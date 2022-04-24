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
        failed_solution_str = 'score: 0/0, could not find gui elements'
        for score, test_reviews in zip(self.features_scores, self.features_reviews):
            if failed_solution_str not in test_reviews:
                test_reviews_str = '\n'.join(test_reviews)
                test_reviews_str = test_reviews_str.replace("_", " ")
                test_reviews_and_score = f"score:{score}\n" + test_reviews_str
                data.append(test_reviews_and_score)
            else:
                data.append(test_reviews)

        data.append(self.final_score)
        return data

    def print(self):
        print(f"student_id: {self.student_id},")
        for score, feature_review in zip(self.features_scores, self.features_reviews):
            print(f"feature_score: {score}, feature_review: {feature_review}")
        print(f"final_score: {self.final_score}")


