import HomeworkExecutioner
from TestcaseRunner import TestcaseRunner
from multiprocessing import Process


if __name__ == '__main__':
    testcase_runner = TestcaseRunner('308418367', 'C:\\Users\\Ben\\PycharmProjects\\pythonProject\\ShayExam.json')
    p = Process(target=HomeworkExecutioner.run_student_solution,
                args=('C:\\Users\\Ben\\PycharmProjects\\pythonProject\\testing.py', 'testing'))
    p.start()
    testcase_runner.run()
    p.terminate()
