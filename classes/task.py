from customtkinter import *
class Task(CTkLabel):
    def __init__(self, master, text, font, wrap_length=350, anchor="w"):
        super().__init__(master=master, text=text, font=font)
        self.configure(wraplength=wrap_length)
        self.configure(anchor=anchor)
        self.checkbox_var = BooleanVar()

    def create_line(self,row):
        line = CTkCanvas(master=self.master, height=1, width=400)
        line.create_line(0, 0, 250, 1, width=2)
        line.grid(row=row, column=0 ,columnspan=2, padx=50,pady=10)
        
    def checkbox(self, row, command=None):
        self.checkbox_widget = CTkCheckBox(master=self.master, text="", width=20, height=20, variable=self.checkbox_var ,command=command)
        self.checkbox_widget.grid(row=row, column=1, padx=10, pady=10, sticky="e")
