"""
iteratre over each solution, run it, and create test_case_runner
hand over all test case runner to report Generator

"""

import os
import importlib
import ReportGenerator
import TestcaseRunner

class DeprecatedHomeworkExecutioner: #TODO delete this later
    def __init__(self,fileLocation):
        txt = open(fileLocation+"\studenIDs.txt", "r")
        self.students = txt.read().split('\n')
        self.studentsPath = self.students
        j=0
        for x in self.students:
            self.studentsPath[j]=fileLocation+"\\"+x+".py"
            j=j+1
        self.i=0
        self.studentAmount=self.students.__len__()
    def __next__(self):
        spec = importlib.util.spec_from_file_location(self.students[self.i], self.studentsPath[self.i])
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        self.i=self.i+1


    class HomeWorkExecutioner:
        def __init__(self, solutions_path, output_path, exercise_path):
            self.solutions_path = solutions_path #Students path
            self.output_path = output_path #Grades path
            self.exercise_path = exercise_path
            self.test_case_runners = []
            self.report_generator = ReportGenerator(self.output_path)

        def run(self):
            files = os.listdir(self.solutions_path)
            def substring(org_string):
                size = len(org_string)
                # Slice string to remove last 3 characters from string
                return org_string[:size - 3]
            studentIds = map(substring, files)
            self.test_case_runners = map(lambda x: self.test_case_runners.append(TestcaseRunner(x)) , studentIds)
            """ for i in studentIds:
                self.test_case_runners.append(TestCaseRunner(i))"""
            #open file and then
            for i in self.test_case_runners:
                spec = importlib.util.spec_from_file_location(i.student_id, self.solutions_path + "\\" + i.student_id +".py") #spec_from_file_location(studentId, path\studenId.py)
                foo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(foo)
                i.run()#TODO what to do with the exercise?

#This is a test #TODO: delete this later
#HE = Homework_Executioner("C:\\StudentProjects")
#while HE.i!=HE.studentAmount:
#    HE.__next__()
