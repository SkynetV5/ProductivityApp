import datetime as dt
from customtkinter import *
from classes.messageInfoBox import MessageInfoBox
from classes.task import Task
from classes.addNewTaskBox import AddNewTaskBox
from tkinter import *
from PIL import Image


FONT = ("Courier", 15, 'bold')
completed_tasks = 0
tasks = []


def clicked_checkbox(checkbox_var): 
    global completed_tasks
    if checkbox_var.get():
        completed_tasks += 1
    else:
        completed_tasks -= 1
    update_progress()
     
def update_progress():
    progress = round((completed_tasks/len(tasks)) * 100,2)
    progressLabel.configure(text=f"{progress}%")
    progressBar.set((completed_tasks/len(tasks)))
    
    if progress == 100:
        completed_window = MessageInfoBox(master=app, title="Brawo!", message="Zrobiłeś wszystkie zadania na dzisiaj!", font=FONT)

def update_tasks():
    global tasks
    for task in range (len(tasks)):
        tasks[task].grid(row=task,column=0,sticky="w", padx=(40,10))
        tasks[task].checkbox(task, command=lambda var=tasks[task].checkbox_var: clicked_checkbox(var))
    
def add_task():
    global tasks
    add_new_task_window = AddNewTaskBox(master=app, font=FONT)
    app.wait_window(add_new_task_window)
    new_task_text = add_new_task_window.get_task_value()
    if new_task_text != "":
        tasks.append(Task(master=scrollable_frame, text=new_task_text, font=FONT))
        update_tasks()    

def change_theme():
    current_mode = get_appearance_mode()
    print(current_mode)
    if current_mode == "Dark":
        set_appearance_mode("Light")
        canvas.configure(bg="#B5ACAC")
    else:
        set_appearance_mode("Dark")
        canvas.configure(bg="#282828")

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
set_appearance_mode("dark")
set_default_color_theme("green")
app.geometry("500x700")
app.title("Things to do today.")
app.resizable(False, False)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

frame_app = CTkFrame(master=app, border_color="#4BF6C3", border_width=2)
frame_app.grid(row=0, column=0, columnspan=2, padx=5, sticky="nsew")
frame_app.grid_columnconfigure(0, weight=1)


title_label = Task(master=frame_app, text=f"Rzeczy do zrobienia na dzień {day}-{month}", font=FONT)
title_label.grid(row=0, column=0, columnspan=3, pady=10)
frame_tasks = CTkFrame(master=frame_app, border_color="#4BF6C3", border_width=2)
frame_tasks.grid(row=2, column=0, columnspan=3)

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

#Tasks
tasks = [Task(master=scrollable_frame, text="Czytanie książki o rozwoju", font=FONT),
        Task(master=scrollable_frame, text="Medytacja przynajmniej przez 5 minut", font=FONT),
        Task(master=scrollable_frame, text="Zrobienie kolejnej sekcji na Udemy odnośnie Python'a", font=FONT),
        Task(master=scrollable_frame, text="Zrobienie kolejnej sekcji na Udemy odnośnie Python'a", font=FONT),
        ]


update_tasks()
    
    
progressLabel = Task(master=frame_app, text="0.0%", font=FONT)
progressLabel.grid(row=len(tasks)+1, column=0, columnspan=3, pady=(10, 5))    

progressBar = CTkProgressBar(frame_app, orientation="horizontal")
progressBar.set((completed_tasks/len(tasks)))
progressBar.grid(row=len(tasks) + 2, column=0, columnspan=3, pady=(0, 20))


add_button = CTkButton(master=frame_app, text="Dodaj zadanie", width=400, height=45, font=FONT, command=add_task)
add_button.grid(row=len(tasks)+3, column=0, columnspan=3, pady=(10, 5))

remove_button = CTkButton(master=frame_app, fg_color="#f44336", hover_color="#B6342A", text="Usuń zadanie", width=400, height=45, font=FONT, command=None)
remove_button.grid(row=len(tasks)+4, column=0,columnspan=3, pady=(10,5))

dark_theme_image = Image.open("images/dark_theme.png")
light_theme_image = Image.open("images/light_theme.png")

button_image = CTkImage(light_image=dark_theme_image,dark_image=light_theme_image, size=(20,20))

theme_button = CTkButton(master=frame_app, fg_color="#4A4646", hover_color="#848080", width=100,height=50, corner_radius=6, image=button_image, text="", command=change_theme)
theme_button.grid(row=len(tasks)+5, column=0, pady=(10,5), sticky="w", padx=(45,0))

language_button = CTkButton(master=frame_app, width=250,height=50, text="Język: Polski", font=FONT)
language_button.grid(row=len(tasks)+5, column=1, columnspan=2, pady=(10,5),sticky="e", padx=(0,45))

close_app_button = CTkButton(master=frame_app,fg_color="#f44336", hover_color="#B6342A", text="Zamknij", width=100,height=50, font=FONT, command=close_app)
close_app_button.grid(row=len(tasks)+6, column=2, pady=(100,5), sticky="e", padx=(0,45)) 

app.mainloop()
