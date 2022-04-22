from tkinter import *
import pickle


class Nations:

    def __init__(self):
        window = Tk()
        # Added Scalling
        window.tk.call('tk', 'scaling', 2.0)
        window.wm_attributes("-topmost", 1)
        window.title("Members of U.N.")
        self._nationDict = \
            pickle.load(open("UNdict.dat", 'rb'))
        print(f"number of countries is : {len(self._nationDict.keys())}")
        self._nationList = \
            list((self._nationDict).keys())
        self._nationList.sort()
        self._conOFlstNations = StringVar()
        yscroll = Scrollbar(window, orient=VERTICAL)
        yscroll.grid(
            row=0, column=1, rowspan=7, sticky=NS)
        self._lstNations = \
            Listbox(window, height=10, width=30,
                    listvariable=self._conOFlstNations,
                    yscrollcommand=yscroll.set)
        self._lstNations.grid(
            row=0, column=0, rowspan=7, sticky=NSEW)
        self._conOFlstNations.set(tuple(self._nationList))
        self._lstNations.bind("<<ListboxSelect>>", self.displayData)
        yscroll["command"] = self._lstNations.yview
        Label(window,
              text="Continent:").grid(row=0, column=3,
                                      padx=4, sticky=E)
        Label(window,
              text="Population:").grid(row=1, column=3,
                                       padx=4, sticky=E)
        Label(window,
              text="Area (sq. miles):").grid(row=2, column=3,
                                             padx=4, sticky=E)
        self._conOFentContinent = StringVar()
        entContinent = \
            Entry(window, width=15, state="readonly",
                  textvariable=self._conOFentContinent)
        entContinent.grid(row=0, column=4, sticky=W)
        self._conOFentPopulation = StringVar()
        entPopulation = \
            Entry(window, width=15, state="readonly",
                  textvariable=self._conOFentPopulation)
        entPopulation.grid(row=1, column=4, )
        self._conOFentArea = StringVar()
        entArea = Entry(window, width=15, state="readonly",
                        textvariable=self._conOFentArea)
        entArea.grid(row=2, column=4)
        window.geometry('%dx%d+%d+%d' % (700, 300, 10, 10))
        window.mainloop()

    def displayData(self, e):
        nation = \
            self._lstNations.get(self._lstNations.curselection())
        self._conOFentContinent.set(
            self._nationDict[nation]["cont"])
        self._conOFentPopulation.set(
            "{0:,.0f}".format(
                1000000 * float(self._nationDict[nation]["popl"])))
        self._conOFentArea.set(
            "{0:,.2f}".format(self._nationDict[nation]["area"]))


Nations()
