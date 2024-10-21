from customtkinter import *
import winsound
from classes.payload import load_config
from googletrans import Translator

class MessageInfoBox(CTkToplevel):
    def __init__(self, master, title, message, geometry="400x200", border_color="#4BF6C3", font=None, type=None):
        super().__init__(master)
        self.translator = Translator()
        self.config = load_config()
        if self.config['language'] == "Language: English":
            language = "en"
        elif self.config['language'] == "Język: Polski":
            language = "pl"
        translated_message = self.translator.translate(message, dest=language).text
        translated_title = self.translator.translate(title, dest=language).text
        self.resizable(False, False)
        self.geometry(geometry)
        self.title(translated_title)
        self.message = translated_message
        self.font = font
        self.border_color = border_color
        self.attributes("-topmost", True)
        self.grab_set()
        self.type = type
        self.message_frame = CTkFrame(master=self, width=500, height=300, border_color=self.border_color, border_width=2)
        self.message_frame.pack(fill="both", expand=True)
        self.message_label = CTkLabel(master=self.message_frame, text=self.message, wraplength=350, anchor="w", font=self.font)
        self.message_label.pack(pady=(50,25), padx=30)
        self.button_close = CTkButton(master=self.message_frame, width=100, height=30, fg_color="#F44336", hover_color="#B6342A", text="OK.", font=self.font, command=self.destroy)
        self.button_close.pack()
        
        self.bind("<FocusOut>", self.on_focus)
        
        
    def shake_window(self):
        x = self.winfo_x()
        y = self.winfo_y()
        shake_distance = 3
        for i in range(5):
            self.geometry(f"+{x + shake_distance * (-1) ** i}+{y}")
            self.update()
            self.after(5)
    
    def on_focus(self, event):
        if self.type == "error":
            self.shake_window()
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)