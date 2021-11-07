class Homework_Executioner:
    def __init__(self,fileLocation):
        txt = open(fileLocation+"\studenIDs.txt", "r") #TODO: add an error message if no file location found
        self.students = txt.read().split('\n')
        self.studentsPath = self.students
        j=0
        for x in self.students:
            self.studentsPath[j]=fileLocation+"\\"+x+".py"
            j=j+1
        self.i=0
        self.studentAmount=self.students.__len__()
    def __next__(self):
        # TODO try catch for this scope for crash
        import importlib.util
        spec = importlib.util.spec_from_file_location(self.students[self.i], self.studentsPath[self.i])
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        self.i=self.i+1

    #SHAY
    class HomeWorkExecutioner:
        def __init__(self, solutions_path, output_path, exercise_path):
            self.solutions_path = solutions_path
            self.output_path = output_path
            self.exercise_path = exercise_path
            self.test_case_runners = []
            self.report_generator = ReportGenerator(self.output_path)

        def run(self):
            """
            iteratre over each solution, run it, and create test_case_runner
            hand over all test case runner to report Generator

            """
#TEST #TODO: delete this later
#HE = Homework_Executioner("C:\\StudentProjects")
#while HE.i!=HE.studentAmount:
#    HE.__next__()
