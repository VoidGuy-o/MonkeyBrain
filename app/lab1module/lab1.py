import tkinter as tk
from tkinter import ttk
from lab1module.logic import encode, decode


class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(width=400, height=200)
        options = {'fill':'both', 'expand':True}

        self.pack(**options)

        container.notebook.add(self, text="Lab 1")
        
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

        self.subframe_shift = ttk.Frame(self)
        # style="TEST.TFrame" just in case
        self.subframe_shift.pack(side="bottom", anchor="w", fill="x", padx=10, pady=10)

        self.label_shift_button = ttk.Label(self.subframe_shift, text="Зсув")
        self.label_shift_button.pack(side="left", pady=10,padx=10)

        self.spinbox_shift = ttk.Spinbox(self.subframe_shift, from_ = 0, to=25, wrap=True, width=5)
        self.spinbox_shift.pack(side="left", pady=10,padx=10)

        self.Encoding = tk.BooleanVar()
        self.radiobutton_decode = ttk.Radiobutton(self.subframe_shift, text='Decode', value=False, variable=self.Encoding)
        self.radiobutton_decode.pack(side="left",pady=10,padx=10)
        self.radiobutton_encode = ttk.Radiobutton(self.subframe_shift, text='Encode', value=True, variable=self.Encoding)
        self.radiobutton_encode.pack(side="left",pady=10,padx=10)

        self.button_start = ttk.Button(self.subframe_shift, text="Start", padding=10, command=lambda: self.entry_result_command())   
        self.button_start.pack(padx=100, anchor="center")
        #Styles

        self.style = ttk.Style()
        self.style.configure("TEST.TFrame", background="gray", foreground="black")

    def display(self, from_, int_=0, encoding=True):
        if int_ == '':
            int_ = 0
        else:
            print(type(int_))
            int_ = int(int_)
            print(type(int_))
        text = from_.get(1.0, 30.0)
        text = text.replace("0", "")
        encoding = self.Encoding.get()
        print(text)
        if encoding == True:
            return encode(text, int_)
        elif encoding == False:
            return decode(text, int_)

    def entry_result_command(self):
        self.entry_result.delete(1.0, 30.0)
        result = self.display(from_=self.entry_before, int_=self.spinbox_shift.get())
        self.entry_result.insert(index=1.0, chars=self.display(from_=self.entry_before, int_=self.spinbox_shift.get()))
        print(self.spinbox_shift.get())
        print(type(self.spinbox_shift.get()))




