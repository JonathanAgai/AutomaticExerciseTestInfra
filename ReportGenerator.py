import pandas as pd
from StudentData import StudentData


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
sd1 = StudentData("308418367", ["10/20", "20/40"], ["test_name: review"])
sd2 = StudentData("204691588", ["15/20", "10/40"], ["test_name: review"])
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
