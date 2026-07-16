import tkinter as tk
from tkinter import ttk
from lab2module.logic import encode

class Frame2(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        
        self.config(width=400, height=200)
        options = {'fill':'both', 'expand':True}

        self.pack(**options)

        container.notebook.add(self, text="Lab 2")
        
        self.entry_result = tk.Text(self, width=100, height=5)
        self.entry_result.pack(side="bottom", fill="x")

        self.label_result = ttk.Label(self, text="Result")
        self.label_result.pack(side="bottom",pady=5, anchor="w")

        self.separator_before_after = ttk.Separator(self, orient="horizontal")
        self.separator_before_after.pack(side="bottom", pady=10)

        self.entry_before = tk.Text(self, width=100, height=5)
        self.entry_before.pack(side="bottom", fill="x")

        self.label_before = ttk.Label(self, text="Enter the text")
        self.label_before.pack(side="bottom",pady=5, anchor="w")

        self.separator_entry_buttons = ttk.Separator(self, orient="horizontal")
        self.separator_entry_buttons.pack(side="bottom", pady=10, fill="x")

        self.subframe_iter = ttk.Frame(self)
        self.subframe_iter.pack(side="bottom", anchor="w", fill="x", padx=10, pady=10)

        self.label_iter_button = ttk.Label(self.subframe_iter, text="Зсув")
        self.label_iter_button.pack(side="left", pady=10,padx=10)

        self.spinbox_shift = ttk.Spinbox(self.subframe_iter, from_ = 0, to=100, wrap=True, width=5)
        self.spinbox_shift.pack(side="left", pady=10,padx=10)

        self.button_start = ttk.Button(self.subframe_iter, text="Start", padding=10, command=lambda: self.entry_result_command(self.entry_before, int(self.spinbox_shift.get())))   
        self.button_start.pack(padx=100, anchor="center")

    def entry_result_command(self, from_, int_):
        text = encode(from_.get(1.0, 'end'), int_)
        for i in text:
            print(i)
        print(text)
        self.entry_result.delete(1.0, 'end')
        self.entry_result.insert(index=1.0, chars=text)
        print(self.spinbox_shift.get())
        print(type(self.spinbox_shift.get()))
        print(text)
