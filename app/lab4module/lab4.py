import tkinter as tk
from tkinter import ttk, filedialog as fd
from lab4module.logic import encode


class Frame4(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(width=400, height=200)
        options = {'fill':'both', 'expand':True}


        self.encoding = tk.BooleanVar()
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

        self.radiobutton_10 = ttk.Radiobutton(self, text='10', value=True, variable=self.encoding)
        self.radiobutton_10.pack(side="left", anchor='s' ,pady=10,padx=10)

        self.radiobutton_100 = ttk.Radiobutton(self, text='100', value=False, variable=self.encoding)
        self.radiobutton_100.pack(side="left", anchor='s' ,pady=10,padx=10)
        

        self.start_button = ttk.Button(self, text="Encode", command=lambda: encode(message = self.encoded_text_field.get(1.0, 'end'), BMPfilepath=self.filepathBMP(), IsTen=self.encoding.get()))
        self.start_button.pack(side="bottom", pady=0, anchor="center")

    def filepathBMP(self):
        fpath = self.selected_file_name.get()
        return fpath

    
    def file_selection(self):
        self.selected_file_name.set(fd.askopenfilename())
        print(self.selected_file_name.get())
        print(type(self.selected_file_name))


