import pandas as pd


class ReportGenerator:
    """
    This component is responsible for producing reports after the tests are completed

    Attributes
    ----------
    results_report_path
    students_data
    table_headers
    frames

    Methods
    -------
    generate_report()
    student_row_generator(student_id)
    """
    def __init__(self, results_report_path: str, students_data: list, table_headers: list):

        self.results_report_path = results_report_path
        self.students_data = students_data
        self.table_headers = table_headers
        self.frames = []

    def generate_report(self):
        """
        generate_report(...) responsible for creating a readable and compiled
            report for each student by the outputs obtained from performing the test set.
        :return: None
        """
        for student_data in self.students_data:
            self.student_row_generator(student_data)
        result = pd.concat(self.frames)
        result.to_csv(f'{self.results_report_path}\\Students_Grades.csv', index=None)

        df = pd.read_csv(f'{self.results_report_path}\\Students_Grades.csv')

        # then to_excel method converting the .csv file to .xlsx file.
        df.to_excel("Students_Grades.xlsx", sheet_name="Students_Grades", index=False)

    def student_row_generator(self, student_data):
        """
        student_row_generator(...) Create a student entry with the relevant information
        :param student_data: student_id, features_scores, features_reviews, final_score
        :type student_data: Class StudentData
        :return: None
        """
        df = pd.DataFrame([student_data], columns=self.table_headers)
        self.frames.append(df)


