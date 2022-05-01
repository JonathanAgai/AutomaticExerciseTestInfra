import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from HomeworkExecutioner import *
from RunTimeTestConfigurations import *


class App:
    def __init__(self, root):
        #init paths
        self.teachers_folder_path = ""
        self.students_work_folder_path = ""
        self.result_folder_path = ""
        #setting title
        root.title("undefined")
        #setting window size
        width=470
        height=290
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        run_button=tk.Button(root)
        run_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        run_button["font"] = ft
        run_button["fg"] = "#000000"
        run_button["justify"] = "center"
        run_button["text"] = "Run"
        run_button.place(x=195,y=240,width=70,height=25)
        run_button["command"] = self.run_button_command

        students_work_folder_button=tk.Button(root)
        students_work_folder_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        students_work_folder_button["font"] = ft
        students_work_folder_button["fg"] = "#000000"
        students_work_folder_button["justify"] = "center"
        students_work_folder_button["text"] = "..."
        students_work_folder_button.place(x=390,y=50,width=30,height=30)
        students_work_folder_button["command"] = self.students_work_folder_button_command

        students_work_folder_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        students_work_folder_label["font"] = ft
        students_work_folder_label["fg"] = "#333333"
        students_work_folder_label["justify"] = "center"
        students_work_folder_label["text"] = "Student's work folder"
        students_work_folder_label.place(x=40,y=50,width=140,height=30)

        self.students_work_folder_text=tk.Text(root)
        ft = tkFont.Font(family='Times',size=10)
        self.students_work_folder_text["font"] = ft
        self.students_work_folder_text["fg"] = "#333333"
        self.students_work_folder_text.place(x=190,y=50,width=180,height=30)

        self.teachers_folder_text=tk.Text(root)
        ft = tkFont.Font(family='Times',size=10)
        self.teachers_folder_text["font"] = ft
        self.teachers_folder_text["fg"] = "#333333"
        self.teachers_folder_text.place(x=190,y=110,width=180,height=30)

        self.result_folder_text=tk.Text(root)
        ft = tkFont.Font(family='Times',size=10)
        self.result_folder_text["font"] = ft
        self.result_folder_text["fg"] = "#333333"
        self.result_folder_text.place(x=190,y=170,width=180,height=30)

        teachers_folder_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        teachers_folder_label["font"] = ft
        teachers_folder_label["fg"] = "#333333"
        teachers_folder_label["justify"] = "center"
        teachers_folder_label["text"] = "Teacher's folder"
        teachers_folder_label.place(x=40,y=110,width=140,height=30)

        result_folder_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        result_folder_label["font"] = ft
        result_folder_label["fg"] = "#333333"
        result_folder_label["justify"] = "center"
        result_folder_label["text"] = "Result folder"
        result_folder_label.place(x=40,y=170,width=140,height=30)

        teachers_folder_button=tk.Button(root)
        teachers_folder_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        teachers_folder_button["font"] = ft
        teachers_folder_button["fg"] = "#000000"
        teachers_folder_button["justify"] = "center"
        teachers_folder_button["text"] = "..."
        teachers_folder_button.place(x=390,y=110,width=30,height=30)
        teachers_folder_button["command"] = self.teachers_folder_button_command

        result_folder_button=tk.Button(root)
        result_folder_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        result_folder_button["font"] = ft
        result_folder_button["fg"] = "#000000"
        result_folder_button["justify"] = "center"
        result_folder_button["text"] = "..."
        result_folder_button.place(x=390,y=170,width=30,height=30)
        result_folder_button["command"] = self.result_folder_button_command

    def run_button_command(self):
        hw_path = "hw1"

        # RunTimeTestConfigurations.set_hw_path(hw_path)
        # RunTimeTestConfigurations.set_is_lecturer_mode(False)
        #
        # json_configuration_file_path = f'./configuration/{hw_path}/tests_configurations.json'
        #
        # gui_elements_images_path = f"configuration/{hw_path}/gui_elements_images"
        # TestConfigurationParser.initialize(json_configuration_file_path, gui_elements_images_path)
        #
        # students_solution_folder_path = f'students_solution_execs/{hw_path}'
        # results_report_path = 'results_report'

        homework_exe = HomeWorkExecutioner( self.students_work_folder_text.get("1.0", tk.END).replace("\n", ""),
                                            self.result_folder_text.get("1.0", tk.END).replace("\n", ""),
                                            self.teachers_folder_text.get("1.0", tk.END).replace("\n", "") + '/tests_configurations.json')

        homework_exe.run()
        print("run_button_command")

    def students_work_folder_button_command(self):
        self.students_work_folder_path = filedialog.askdirectory()
        self.students_work_folder_text.delete("1.0", "end")
        self.students_work_folder_text.insert(tk.END, self.students_work_folder_path)


    def teachers_folder_button_command(self):
        self.teachers_folder_path = filedialog.askdirectory()
        self.teachers_folder_text.delete("1.0","end")
        self.teachers_folder_text.insert(tk.END, self.teachers_folder_path)


    def result_folder_button_command(self):
        self.result_folder_path = filedialog.askdirectory()
        self.result_folder_text.delete("1.0","end")
        self.result_folder_text.insert(tk.END, self.result_folder_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
