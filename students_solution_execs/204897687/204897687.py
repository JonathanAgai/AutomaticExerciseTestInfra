from tkinter import *


def fullname():
    conOFentFullName.set(conOFentFirstName.get())


window = Tk()
window.title("Full Name")
window.wm_attributes("-topmost", 1)
Label(window, text="Last name:").grid(row=0, column=0, sticky=E)
conOFentLastName = StringVar()
entLastName = Entry(window, width=15,
                    textvariable=conOFentLastName)
entLastName.grid(row=0, column=1, padx=5, sticky=W)

Label(window, text="First name:").grid(row=1, column=0, sticky=E)
conOFentFirstName = StringVar()
entFirstName = Entry(window, width=15,
                     textvariable=conOFentFirstName)
entFirstName.grid(row=1, column=1, padx=5, sticky=W)

btnDisplay = Button(text="Display Full Name", command=fullname)
btnDisplay.grid(row=2, column=0, columnspan=2, pady=10)
Label(window, text="Full name:").grid(row=3, column=0, sticky=E)
conOFentFullName = StringVar()
entFullName = Entry(window, width=15, state="readonly", textvariable=conOFentFullName)
# entFullName = Entry(window, state="readonly", textvariable=conOFentFullName)
entFullName.grid(row=3, column=1, padx=5)

window.geometry('%dx%d+%d+%d' % (200, 200, 10, 10))
window.mainloop()



