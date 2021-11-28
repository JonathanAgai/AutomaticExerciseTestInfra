import HomeworkExecutioner
from TestcaseRunner import TestcaseRunner
from multiprocessing import Process

state = False

if __name__ == '__main__':
    if state:
        testcase_runner = TestcaseRunner('308418367', 'C:\\Users\\Ben\\PycharmProjects\\pythonProject\\Solutions.json', state)
    else:
        testcase_runner = TestcaseRunner('308418367', 'C:\\Users\\Ben\\PycharmProjects\\pythonProject\\ShayExam.json', state)

    p = Process(target=HomeworkExecutioner.run_student_solution,
                args=('C:\\Users\\Ben\\PycharmProjects\\pythonProject\\testing.py', 'testing'))
    p.start()
    testcase_runner.run()


    p.terminate()
