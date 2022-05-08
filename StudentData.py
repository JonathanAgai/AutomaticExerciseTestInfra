"""
class containing:
  string - student ID
  dict/list - amount of score recv for each feature
  dict/list - summery for each feature
  string - final score
"""


class StudentData:
    # TODO documentation
    """
        write in one line class description here

        write long description of class here

        Attributes
        ----------
        student_id : write the parameter's type here
            write parameter description here
        features_scores : write the parameter's type here
            write parameter description here
        features_reviews : write the parameter's type here
            write parameter description here
        final_score : write the parameter's type here
            write parameter description here

        Methods
        -------
        generate_data()
            write function description here
        print()
            write function description here
        """
    def __init__(self, student_id: str, features_scores: list, features_reviews: list, final_score: str):
        # TODO documentation
        """
        __init__(...) write function description here
        :param student_id: write parameter description here
        :type student_id: write the parameter's type here
        :param features_scores: write parameter description here
        :type features_scores: write the parameter's type here
        :param features_reviews: write parameter description here
        :type features_reviews: write the parameter's type here
        :param final_score: write parameter description here
        :type final_score: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.student_id = student_id
        self.features_scores = features_scores
        self.features_reviews = features_reviews
        self.final_score = final_score

    def generate_data(self):
        # TODO documentation
        """
        generate_data(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
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


