import pandas as pd


class ReportGenerator:
    def __init__(self, results_report_path: str, students_data: list, table_headers: list):
        self.results_report_path = results_report_path
        self.students_data = students_data
        self.table_headers = table_headers
        self.frames = []

    # TODO generate report into specific dir
    def generate_report(self):
        for student_data in self.students_data:
            self.student_row_generator(student_data)
        result = pd.concat(self.frames)
        result.to_csv(f'{self.results_report_path}\\data.csv')
        convert_to_html(f'{self.results_report_path}\\data.csv')

    def student_row_generator(self, student_data):
        df = pd.DataFrame([student_data], columns=self.table_headers)
        self.frames.append(df)


def convert_to_html(filename):
    a = pd.read_csv(filename)
    a.to_html(filename)


# headers = ["student id", "feature1 score", "feature1 review", "feature2 score", "feature2 review", "final score"]
# sd1 = StudentData("308418367", ["10/20", "20/40"], ["test_name: review"])
# sd2 = StudentData("204691588", ["15/20", "10/40"], ["test_name: review"])
# students = [sd1, sd2]
