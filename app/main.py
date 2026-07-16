import tkinter as tk
from tkinter import ttk
from lab1module.lab1 import Frame1
from lab2module.lab2 import Frame2
from lab3module.lab3 import Frame3
from lab4module.lab4 import Frame4
#from lab5module.lab5 import Frame5
#from lab6module.lab6 import Frame6


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.notebook = ttk.Notebook(self, padding=10)
        self.notebook.pack(pady=10, fill='both', expand=True)


if __name__ == "__main__":
    App = App()
    Frame1 = Frame1(App)
    Frame2 = Frame2(App)
    Frame3 = Frame3(App)
    Frame4 = Frame4(App)
    #Frame5 = Frame5(App)
    #Frame6 = Frame6(App)
    App.mainloop()
