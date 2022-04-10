from tkinter import *

def checkAnswer():
    try:
       m = people.index(lstPeople.get(lstPeople.curselection()))
       n = placesSorted.index(lstPlaces.get(lstPlaces.curselection()))
       if m == n:
           conOFentAnswer.set("CORRECT")
       else:
           conOFentAnswer.set("INCORRECT")
    except Exception:
        conOFentAnswer.set("INCORRECT")
    #Added clear listbox curse selecting
    lstPeople.selection_clear(0, END)
    lstPlaces.selection_clear(0, END)

window = Tk()
#Added Scalling
window.tk.call('tk', 'scaling', 2.0)
window.title("Workplaces")
window.wm_attributes("-topmost", 1)
Label(window, text="Person").grid(row=0, column=0)
Label(window, text="Workplace").grid(row=0, column=1)
people = ["Bruce Wayne", "Clark Kent", "Peter Parker",
          "Rick Blaine", "Willie Wonka"]
places = ["Wayne Enterprises", "Daily Planet", "Daily Bugle",
          "Rick's American Cafe", "Chocolate Factory"]
placesSorted = list(places)
#TODO list order
placesSorted.sort()
conOFlstPeople = StringVar()
lstPeople = Listbox(window, width=12, height=5, \
       exportselection=0, listvariable=conOFlstPeople)
lstPeople.grid(row=1, column=0, padx=10)
conOFlstPeople.set(tuple(people))
conOFlstPlaces = StringVar()
lstPlaces = Listbox(window, width=18,
   height=5, exportselection=0, listvariable=conOFlstPlaces)
lstPlaces.grid(row=1, column=1, padx=10)
conOFlstPlaces.set(tuple(placesSorted))
btnDetermine = Button(window,
   text="Determine if Match is Correct", command=checkAnswer)
btnDetermine.grid(row=2, column=0, columnspan=2, pady=5)
Label(window, text="Answer:").grid(row=3, column=0, sticky=E)
conOFentAnswer = StringVar()
entAnswer = Entry(window, width=10, \
                  textvariable=conOFentAnswer, state="readonly")
entAnswer.grid(row=3, column=1, padx=10, pady=(0,5), sticky=W)
#Added Geometry
window.geometry('%dx%d+%d+%d' % (400, 300, 10, 10))
window.mainloop()

