import datetime as dt
from customtkinter import *
from classes.messageInfoBox import MessageInfoBox
from classes.task import Task
from classes.addNewTaskBox import AddNewTaskBox
from tkinter import *
FONT = ("Courier", 15, 'bold')

completed_tasks = 0
tasks = []
now = dt.datetime.now()
month = now.month
day = now.day
if day < 10:
    day = '0' + str(day)
if month < 10:
    month = '0' + str(month)
    
    
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
    add_new_task_window = AddNewTaskBox(master=app)
    app.wait_window(add_new_task_window)
    new_task_text = add_new_task_window.get_task_value()
    if new_task_text != "":
        tasks.append(Task(master=scrollable_frame, text=new_task_text, font=FONT))
        update_tasks()    


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
title_label.grid(row=0, column=0, columnspan=3, pady=5)
frame_tasks = CTkFrame(master=frame_app, border_color="#4BF6C3", border_width=2)
frame_tasks.grid(row=2, column=0, columnspan=3)

#Scrollbar
canvas = CTkCanvas(frame_tasks, bg="#282828")
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
        Task(master=scrollable_frame, text="Zrobienie kolejnej sekcji na Udemy odnośnie Python'a", font=FONT),
        Task(master=scrollable_frame, text="Zrobienie kolejnej sekcji na Udemy odnośnie Python'a", font=FONT),
        Task(master=scrollable_frame, text="Zrobienie kolejnej sekcji na Udemy odnośnie Python'a", font=FONT),
        Task(master=scrollable_frame, text="Zrobienie kolejnej sekcji na Udemy odnośnie Python'a", font=FONT),
        Task(master=scrollable_frame, text="Zrobienie kolejnej sekcji na Udemy odnośnie Python'a", font=FONT),
        ]


update_tasks()
    
    
progressLabel = Task(master=frame_app, text="0.0%", font=FONT)
progressLabel.grid(row=len(tasks)+1, column=0, columnspan=3, pady=(10, 5))    

progressBar = CTkProgressBar(frame_app, orientation="horizontal")
progressBar.set((completed_tasks/len(tasks)))
progressBar.grid(row=len(tasks) + 2, column=0, columnspan=3, pady=(0, 20))


add_button = CTkButton(master=frame_app, text="Dodaj zadanie", width=400, height=30, command=add_task)
add_button.grid(row=len(tasks)+3, column=0, columnspan=3, pady=(10, 5))

app.mainloop()
