import datetime as dt
from customtkinter import *
from classes.messageInfoBox import MessageInfoBox
from classes.task import Task
from classes.addNewTaskBox import AddNewTaskBox
from classes.removeTaskBox import RemoveTaskBox
from tkinter import *
from PIL import Image
from classes.payload import load_data, load_config
from classes.save import save_data, save_config
from googletrans import Translator


data = load_data()
config = load_config()
FONT = ("Courier", 15, 'bold')
completed_tasks = 0
try:
    tasks = data['tasks']
except Exception:
    tasks = []

translator = Translator()

def translate_text(language_var):
    global config
    language = None
    if language_var == "Język: Polski":
        config["language"] = "Język: Polski"
        save_config(config)
        language = "pl"
    elif language_var == "Language: English":
        config["language"] = "Language: English"
        save_config(config)
        language = "en"
    title_label.configure(text=translator.translate(title_label.cget("text"), dest=language).text)
    question_label.configure(text=translator.translate(question_label.cget("text"), dest=language).text)
    add_button.configure(text=translator.translate(add_button.cget("text"), dest=language).text)
    remove_button.configure(text=translator.translate(remove_button.cget("text"), dest=language).text)
    close_app_button.configure(text=translator.translate(close_app_button.cget("text"), dest=language).text)

def clicked_checkbox(checkbox_var): 
    global completed_tasks
    if checkbox_var.get():
        completed_tasks += 1
    else:
        completed_tasks -= 1
    update_progress()
     
def update_progress():
    if len(tasks) != 0:
        progress = round((completed_tasks/len(tasks)) * 100, 2)
        progressLabel.configure(text=f"{progress}%")
        progressBar.set((completed_tasks/len(tasks)))
    
    if progress == 100:
        completed_window = MessageInfoBox(master=app, title="Brawo!", message="Zrobiłeś wszystkie zadania na dzisiaj!", font=FONT)

def update_tasks():
    global tasks
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    if len(tasks) != 0:
        for task in tasks:
            task_instance = Task(master=scrollable_frame, text=f"{task['id']}.{task['text']}", font=FONT)
            task_instance.grid(row=task['id'], column=0,sticky="w", padx=(40,10))
            task_instance.checkbox(row=task['id'], command=lambda var=task_instance.checkbox_var: clicked_checkbox(var))
    
def add_task():
    global tasks
    add_new_task_window = AddNewTaskBox(master=app, font=FONT)
    app.wait_window(add_new_task_window)
    new_task_text = add_new_task_window.get_task_value()
    if new_task_text != "":
        task_id = len(tasks) + 1
        tasks.append({"id": task_id, "text": new_task_text})
        save_data({"tasks": tasks})
        update_tasks()    
        
        
def remove_task():
    global tasks
    remove_task_window = RemoveTaskBox(master=app, font=FONT)
    app.wait_window(remove_task_window)
    value = remove_task_window.get_task_value()
    if value != "":
        task_id = int(value)
        tasks = [task for task in tasks if task['id'] != task_id]
        for index, task in enumerate(tasks):
            task['id'] = index + 1;
        save_data({"tasks": tasks})
        update_tasks()
    
def change_theme():
    current_mode = get_appearance_mode()
    if current_mode == "Dark":
        config['theme'] = "Light"
        set_appearance_mode("Light")
        # canvas.configure(bg="#B5ACAC")
    else:
        config['theme'] = "Dark"
        set_appearance_mode("Dark")
        # canvas.configure(bg="#282828")
    save_config(config)
def close_app():
    app.destroy()


now = dt.datetime.now()
month = now.month
day = now.day
if day < 10:
    day = '0' + str(day)
if month < 10:
    month = '0' + str(month)
    

app = CTk()
set_appearance_mode(config['theme'])
set_default_color_theme("green")
app.geometry("500x700")
app.title("Things to do today.")
app.resizable(False, False)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

frame_app = CTkFrame(master=app, border_color="#4BF6C3", border_width=2)
frame_app.grid(row=0, column=0, columnspan=2, sticky="nsew")
frame_app.grid_columnconfigure(0, weight=1)


title_label = Task(master=frame_app, text=f"Rzeczy do zrobienia na dzień {day}-{month}", font=FONT)
title_label.grid(row=0, column=0, columnspan=3, pady=10)
frame_tasks = CTkFrame(master=frame_app, border_color="#4BF6C3", border_width=2)
frame_tasks.grid(row=2, column=0, columnspan=3)

question_label = Task(master=frame_app,text="ZADANIA", font=FONT)
question_label.grid(row=1, column=0, columnspan=3, pady=5)

#Scrollbar
canvas = CTkCanvas(frame_tasks, bg="#282828", height=100)
canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")

scrollbar = CTkScrollbar(frame_tasks, command=canvas.yview, button_hover_color="#4BF6C3")
scrollbar.grid(row=0, column=3, sticky="ns")

canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = CTkFrame(master=canvas)
canvas.create_window(0, 0, window=scrollable_frame, width=550)

scrollable_frame.bind(
    "<Configure>",
    lambda e: (
        canvas.configure(
            scrollregion=canvas.bbox("all"),
            width=550,
        ),
        canvas.yview_moveto(0)
    )
   
)
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * event.delta/120), "units"))

update_tasks() 
    
progressLabel = Task(master=frame_app, text="0.0%", font=FONT)
progressLabel.grid(row=3, column=0, columnspan=3, pady=(10, 5))    

progressBar = CTkProgressBar(frame_app, orientation="horizontal")
progressBar.set(0)
progressBar.grid(row=4, column=0, columnspan=3, pady=(0, 20))


add_button = CTkButton(master=frame_app, text="Dodaj zadanie", width=400, height=45, font=FONT, command=add_task)
add_button.grid(row=5, column=0, columnspan=3, pady=(10, 5))

remove_button = CTkButton(master=frame_app, fg_color="#f44336", hover_color="#B6342A", text="Usuń zadanie", width=400, height=45, font=FONT, command=remove_task)
remove_button.grid(row=6, column=0,columnspan=3, pady=(10,5))

dark_theme_image = Image.open("images/dark_theme.png")
light_theme_image = Image.open("images/light_theme.png")

button_image = CTkImage(light_image=dark_theme_image,dark_image=light_theme_image, size=(20,20))

theme_button = CTkButton(master=frame_app, fg_color="#4A4646", hover_color="#848080", width=100,height=50, corner_radius=6, image=button_image, text="", command=change_theme)
theme_button.grid(row=7, column=0, pady=(10,5), sticky="w", padx=(45,0))

close_app_button = CTkButton(master=frame_app,fg_color="#f44336", hover_color="#B6342A", text="Zamknij", width=100,height=50, font=FONT, command=close_app)
close_app_button.grid(row=8, column=2, pady=(90,5), sticky="e", padx=(0,45)) 


language_var = StringVar(value=config["language"])
language_button = CTkComboBox(master=frame_app, width=250,height=50, values=["Język: Polski", "Language: English"], justify="center", font=FONT, variable=language_var,command=translate_text)
language_button.grid(row=7, column=1, columnspan=2, pady=(10,5),sticky="e", padx=(0,45))
translate_text(language_var.get())


app.mainloop()
