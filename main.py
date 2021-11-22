import HomeworkExecutioner
from TestcaseRunner import TestcaseRunner


testcase_runner = TestcaseRunner('308418367', 'C:\\Users\\Ben\\PycharmProjects\\pythonProject\\ShayExam.json')
HomeworkExecutioner.run_student_solution('C:\\Users\\Ben\\PycharmProjects\\pythonProject\\testing.py', 'testing')
testcase_runner.run()


