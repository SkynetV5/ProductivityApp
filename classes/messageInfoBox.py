from customtkinter import *

class MessageInfoBox(CTkToplevel):
    def __init__(self, master, title, message, geometry="400x200", font=None):
        super().__init__(master)
        self.resizable(False, False)
        self.geometry(geometry)
        self.title(title)
        self.message = message
        self.font = font
        self.message_frame = CTkFrame(master=self, width=500, height=300, border_color="#4BF6C3", border_width=2)
        self.message_frame.pack(fill="both", expand=True)
        self.message_label = CTkLabel(master=self.message_frame, text=self.message, font=self.font)
        self.message_label.pack(pady=50, padx=30)
        self.button_close = CTkButton(master=self.message_frame, width=100, height=30, text="Zamknij", command=self.destroy)
        self.button_close.pack()
        