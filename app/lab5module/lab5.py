import tkinter as tk
from tkinter import ttk
from lab5module.logic import encode




class Frame4(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(width=400, height=200)
        options = {'fill':'both', 'expand':True}

        self.pack(**options)

        container.notebook.add(self, text="Lab 5")

