from customtkinter import *

class AddNewTaskBox(CTkToplevel):
    def __init__(self, master, geometry="400x200", font=None):
        super().__init__(master)
        self.resizable(False, False)
        self.geometry(geometry)
        self.title("Dodaj nowe zadanie")
        self.font = font
        self.task = StringVar()
        self.message_frame = CTkFrame(master=self, width=500, height=300, border_color="#4BF6C3", border_width=2)
        self.message_frame.pack(fill="both", expand=True)
        self.entry_label = CTkLabel(master=self.message_frame, text="Wpisz zadanie:", font=self.font)
        self.entry_label.pack(pady=(30,0))
        self.entry = CTkEntry(master=self.message_frame, width=400, height=30, textvariable=self.task)
        self.entry.pack(pady=(0,10), padx=30)
        self.button_add = CTkButton(master=self.message_frame, width=100, height=30, text="Dodaj", font=self.font, command=self.button_add_command)
        self.button_add.pack(side="left", padx=(30,0))
        self.button_close = CTkButton(master=self.message_frame, fg_color="#F44336", hover_color="#B6342A", width=100, height=30, text="Anuluj", font=self.font, command=self.button_close_command)
        self.button_close.pack(side="right", padx=(0,30))
        
    def get_task_value(self):
        return self.task.get()

    def button_add_command(self):
        self.destroy()
    
    def button_close_command(self):
        self.task.set("")
        self.destroy()
