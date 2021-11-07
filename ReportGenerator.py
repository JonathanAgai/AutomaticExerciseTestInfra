import pandas as pd
import csv

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


    #TODO implement with pandas
    def generate_report(self, test_case_runners):
        pass

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


class ReportGenerator:
    def __init__(self, student_data: list, table_headers: list, frames: list):
        self.student_data = student_data
        self.table_headers = table_headers
        self.frames = frames

    def generate_report(self):
        result = pd.concat(self.frames)
        result.to_csv('data.csv')
        return result

    def student_row_generator(self):
        df = pd.DataFrame(self.student_data, columns=self.table_headers)
        self.frames.append(df)


headers = ["student id", "feature1 score", "feature1 review", "feature2 score", "feature2 review", "final score"]
sd1 = StudentData("308418367", ["10/20", "20/40"], ["wasnt good enough", "good"])
sd2 = StudentData("204691588", ["15/20", "10/40"], ["crap", "crap"])
students = [sd1, sd2]

students_data = []
for student in students:
    students_data.append(student.generate_data())


frames = []
rg = ReportGenerator(students_data, headers, frames)
rg.student_row_generator()
print(rg.generate_report())

a = pd.read_csv("data.csv", index_col=0)
a.to_html("students.html")
