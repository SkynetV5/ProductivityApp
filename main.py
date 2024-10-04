import datetime as dt
from customtkinter import *
from classes.messageInfoBox import MessageInfoBox
from classes.task import Task
FONT = ("Courier", 15, 'bold')

completed_tasks = 0

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
    progress = (completed_tasks/len(tasks)) * 100
    progressLabel.configure(text=f"{progress}%")
    progressBar.set((completed_tasks/len(tasks)))
    
    if progress == 100:
        completed_window = MessageInfoBox(master=app, title="Brawo!", message="Zrobiłeś wszystkie zadania na dzisiaj!", font=FONT)

app = CTk()
set_appearance_mode("dark")
set_default_color_theme("green")
app.geometry("400x500")
app.title("Things to do today.")


frame_app = CTkFrame(master=app, width=400, height=500, border_color="#4BF6C3", border_width=2)
frame_app.grid(row=0, column=0, columnspan=2, padx=5)

title_label = Task(master=frame_app, text=f"Rzeczy do zrobienia na dzień {day}-{month}", font=FONT)
title_label.grid(row=0, column=0, columnspan=2, pady=5)
frame_tasks = CTkFrame(master=frame_app, width=400, height=500, border_color="#4BF6C3", border_width=2)
frame_tasks.grid(row=2, column=0, columnspan=2)

tasks = [Task(master=frame_tasks, text="Czytanie książki o rozwoju",
        font=FONT),Task(master=frame_tasks, text="Medytacja przynajmniej przez 5 minut", font=FONT),
        Task(master=frame_tasks, text="Zrobienie kolejnej sekcji na Udemy odnośnie Python'a", font=FONT)]
for task in range (len(tasks)):
    tasks[task].grid(row=task,column=0, padx=10,pady=10)
    tasks[task].checkbox(task, command=lambda var=tasks[task].checkbox_var: clicked_checkbox(var))
    
progressLabel = Task(master=frame_app, text=f"{(completed_tasks/len(tasks)) *100}%", font=FONT)
progressLabel.grid(row=len(tasks)+1, column=0, columnspan=2, pady=(10, 5))    

progressBar = CTkProgressBar(frame_app, orientation="horizontal")
progressBar.set((completed_tasks/len(tasks)))
progressBar.grid(row=len(tasks) + 2, column=0, columnspan=2, pady=(0, 20))



app.mainloop()
