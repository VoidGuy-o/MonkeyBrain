import tkinter as tk
from tkinter import ttk, filedialog as fd
#from lab4module.logic import stuff


class Frame4(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(width=400, height=200)
        options = {'fill':'both', 'expand':True}



        self.selected_file_name = tk.StringVar()
        print(self.selected_file_name)
        self.pack(**options)

        container.notebook.add(self, text="Lab 4")
        
        self.encoded_text_field = tk.Text(self, width = 100, height = 5)
        self.encoded_text_field.pack(side="bottom", fill="x")

        self.text_label_1 = ttk.Label(self, text="Message you want to encode")
        self.text_label_1.pack(side="bottom", pady=5, anchor="w")

        self.selectfile_buttom = ttk.Button(self, text="Select a file", command=lambda: self.file_selection())
        self.selectfile_buttom.pack(side="bottom", pady=5, anchor="w")

        self.selected_file_label = ttk.Label(self, textvariable=self.selected_file_name)
        self.selected_file_label.pack(side="bottom", pady=5, anchor="w")


    def file_selection(self):
        self.selected_file_name.set(fd.askopenfilename())
        print(self.selected_file_name)
        print(type(self.selected_file_name))


