import tkinter as tk
from tkinter import ttk
from lab3module.logic import analysis
class Frame3(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        
        self.config(width=400, height=200)
        options = {'fill':'both', 'expand':True}

        self.pack(**options)

        container.notebook.add(self, text="Lab 3")

        self.entry = tk.Text(self, width=100, height=5)
        self.entry.pack(side="bottom", fill="x")
        
        self.separator_before_after = ttk.Separator(self, orient="horizontal")
        self.separator_before_after.pack(side="bottom", pady=10)

        self.button_start = ttk.Button(self, text="Start", padding=10, command= lambda: analysis(self.entry.get(1.0, 'end')))
        self.button_start.pack(padx=100, anchor="center")
