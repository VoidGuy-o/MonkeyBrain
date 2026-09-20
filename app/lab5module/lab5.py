import tkinter as tk
from tkinter import ttk
from lab5module.logic import encrypt


class Frame5(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(width=400, height=200)
        options = {'fill':'both', 'expand':True}

        self.pack(**options)

        container.notebook.add(self, text="Lab 5")

        self.encoded_text_field = tk.Text(self, width = 100, height = 5)
        self.encoded_text_field.pack(side="bottom", fill="x")

        self.label_result = ttk.Label(self, text="Result")
        self.label_result.pack(side="bottom",pady=5, anchor="w")

        self.start_button = ttk.Button(self, text="Encode", command=lambda: self.entry_result_command(self.input_text_field, int(self.spinbox_shift.get())))
        self.start_button.pack(side="bottom", pady=0, anchor="center")


        self.input_text_field = tk.Text(self, width=100, height=5)
        self.input_text_field.pack(side="bottom", fill="x")

        
        self.label_input = ttk.Label(self, text="Message you want to encode")
        self.label_input.pack(side="bottom", pady=5, anchor="w")

        self.spinbox_shift = ttk.Spinbox(self, from_ = 0, to=100, wrap=True, width=5)
        self.spinbox_shift.pack(side="left", pady=10,padx=10)


    # i have no idea what is this, I just copied it from the lab2 
    def entry_result_command(self, from_, int_):
        extracted_message = from_.get(1.0, 'end')
        text = encrypt(extracted_message[:-1], int_, debug=True)
        self.encoded_text_field.delete(1.0, 'end')
        self.encoded_text_field.insert(index=1.0, chars=text)
        print(self.spinbox_shift.get())
        print(type(self.spinbox_shift.get()))
