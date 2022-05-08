import tkinter as tk
import tkinter.font as tkFont
from HomeworkExecutioner import *
from RunTimeTestConfigurations import *
import os


def get_possible_homeworks():
    """
    get_possible_homeworks(...) extract existing homeworks options dirs
    :return: homeworks options
    :rtype: tuple
    """
    config_files = os.listdir("configuration")
    homework_config = [cdir for cdir in config_files if cdir.startswith('hw')]
    return tuple(homework_config)


class App:
    def __init__(self, root):
        root.title("Gui Automation Testing Tool")
        # setting window size
        width = 470
        height = 290
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        tk.ttk.Label(root,
                     text="Select Homework :",
                     font=("Times New Roman", 10)).grid(column=0, row=5, padx=10, pady=25)

        # Combobox creation
        self.homework_opts = tk.ttk.Combobox(root, width=27, state='readonly')

        # Adding combobox drop down list
        self.homework_opts['values'] = get_possible_homeworks()
        self.homework_opts.grid(column=1, row=5)
        self.homework_opts.current(0)

        run_button = tk.Button(root)

        run_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        run_button["font"] = ft
        run_button["fg"] = "#000000"
        run_button["justify"] = "center"
        run_button["text"] = "Run"
        run_button.place(x=195, y=240, width=70, height=25)
        run_button["command"] = self.run_button_command

    def generate_hw_solution_tree(self, hw_path: str):

        directories = [
            f"students_solution",
            f"students_solution/{hw_path}"
        ]

        for d in directories:
            if not os.path.exists(d):
                os.mkdir(d)


    def run_button_command(self):
        """
        run_button_command(...) Run the program according to the selection of the desired exercise
        :return: None
        """
        hw_path = self.homework_opts.get()
        self.generate_hw_solution_tree(hw_path)
        RunTimeTestConfigurations.set_hw_path(hw_path)
        RunTimeTestConfigurations.set_is_lecturer_mode(False)

        json_configuration_file_path = f'./configuration/{hw_path}/tests_configurations.json'

        gui_elements_images_path = f"configuration/{hw_path}/gui_elements_images"
        TestConfigurationParser.initialize(json_configuration_file_path, gui_elements_images_path)

        students_solution_folder_path = f'students_solution_execs/{hw_path}'
        results_report_path = f'students_solution/{hw_path}'
        homework_exe = HomeWorkExecutioner(students_solution_folder_path,
                                           results_report_path,
                                           json_configuration_file_path)
        homework_exe.run()
        print("run_button_command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
