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
        result.to_csv(f'{self.results_report_path}\\Students_Grades.csv', index=None)

        df = pd.read_csv(f'{self.results_report_path}\\Students_Grades.csv')

        # then to_excel method converting the .csv file to .xlsx file.
        df.to_excel("Students_Grades.xlsx", sheet_name="Students_Grades", index=False)

    def student_row_generator(self, student_data):
        df = pd.DataFrame([student_data], columns=self.table_headers)
        self.frames.append(df)


# headers = ["student id", "feature1 score", "feature1 review", "final score"]

