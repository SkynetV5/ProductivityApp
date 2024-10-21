from customtkinter import *
from classes.messageInfoBox import MessageInfoBox
from classes.payload import load_config
from googletrans import Translator

class AddNewTaskBox(CTkToplevel):
    def __init__(self, master, geometry="400x200", font=None):
        super().__init__(master)
        self.translator = Translator()
        self.config = load_config()
        if self.config['language'] == "Language: English":
            language = "en"
        elif self.config['language'] == "Język: Polski":
            language = "pl"
        title = "Dodaj nowe zadanie"
        translated_title = self.translator.translate(title, dest=language).text
        entry_text = "Wpisz zadanie:"
        translated_entry_text = self.translator.translate(entry_text, dest=language).text
        add_text = "Dodaj"
        translated_add_text = self.translator.translate(add_text, dest=language).text
        close_text = "Anuluj"
        translated_close_text = self.translator.translate(close_text, dest=language).text
        self.resizable(False, False)
        self.geometry(geometry)
        self.title(translated_title)
        self.font = font
        self.attributes("-topmost", True)
        self.grab_set()
        self.task = StringVar()
        self.message_frame = CTkFrame(master=self, width=500, height=300, border_color="#4BF6C3", border_width=2)
        self.message_frame.pack(fill="both", expand=True)
        self.entry_label = CTkLabel(master=self.message_frame, text=translated_entry_text, font=self.font)
        self.entry_label.pack(pady=(30,0))
        self.entry = CTkEntry(master=self.message_frame, width=400, height=30, textvariable=self.task)
        self.entry.pack(pady=(0,10), padx=30)
        self.button_add = CTkButton(master=self.message_frame, width=100, height=30, text=translated_add_text, font=self.font, command=self.button_add_command)
        self.button_add.pack(side="left", padx=(30,0))
        self.button_close = CTkButton(master=self.message_frame, fg_color="#F44336", hover_color="#B6342A", width=100, height=30, text=translated_close_text, font=self.font, command=self.button_close_command)
        self.button_close.pack(side="right", padx=(0,30))
        
    def get_task_value(self):
        return self.task.get()

    def button_add_command(self):
        if self.task.get() == "":
             error_message_window = MessageInfoBox(master=self.master, title="Błąd!", message="Wpisz zadanie!", border_color="#f44336", font=self.font, type="error")
        else: 
            self.destroy()
    
    def button_close_command(self):
        self.task.set("")
        self.destroy()