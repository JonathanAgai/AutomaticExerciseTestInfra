import pandas as pd


class ReportGenerator:
    # TODO documentation
    """
        write in one line class description here

        write long description of class here

        Attributes
        ----------
        results_report_path : write the parameter's type here
            write parameter description here
        students_data : write the parameter's type here
            write parameter description here
        table_headers : write the parameter's type here
            write parameter description here
        frames : write the parameter's type here
            write parameter description here

        Methods
        -------
        generate_report()
            write function description here
        student_row_generator(student_id)
            write function description here
        """
    def __init__(self, results_report_path: str, students_data: list, table_headers: list):
        # TODO documentation
        """
        __init__(...) write function description here
        :param results_report_path: write parameter description here
        :type results_report_path: write the parameter's type here
        :param students_data: write parameter description here
        :type students_data: write the parameter's type here
        :param table_headers: write parameter description here
        :type table_headers: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        self.results_report_path = results_report_path
        self.students_data = students_data
        self.table_headers = table_headers
        self.frames = []

    # TODO generate report into specific dir
    def generate_report(self):
        # TODO documentation
        """
        generate_report(...) write function description here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        for student_data in self.students_data:
            self.student_row_generator(student_data)
        result = pd.concat(self.frames)
        result.to_csv(f'{self.results_report_path}\\Students_Grades.csv', index=None)

        df = pd.read_csv(f'{self.results_report_path}\\Students_Grades.csv')

        # then to_excel method converting the .csv file to .xlsx file.
        df.to_excel("Students_Grades.xlsx", sheet_name="Students_Grades", index=False)

    def student_row_generator(self, student_data):
        # TODO documentation
        """
        student_row_generator(...) write function description here
        :param student_data: write parameter description here
        :type student_data: write the parameter's type here
        :return: write return value and description here or write None if it doesn't have return value.
        :rtype: write the type of the return parameter here
        """
        df = pd.DataFrame([student_data], columns=self.table_headers)
        self.frames.append(df)


