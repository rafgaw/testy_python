import tkinter

import tkinker1

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self. label1 = tkinter.Label(self.main_window, text="Witaj Lewo")
        self. label2 = tkinter.Label(self.main_window, text="Witaj Prawo")
        self. label3 = tkinter.Label(self.main_window, text="Witaj Góra")
        self. label4 = tkinter.Label(self.main_window, text="Witaj Dół")

        self.label1.pack(side='left')
        self.label2.pack(side='right')
        self.label3.pack(side='top')
        self.label4.pack(side=tkinter.BOTTOM)

        tkinter.mainloop()

my_gui = MyGui()
