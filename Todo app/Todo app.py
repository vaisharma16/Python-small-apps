import tkinter as tk

from tkinter import messagebox

win = tk.Tk() 

win.geometry( '500x450') 
win.title('Todo App')

win.config(bg='#00001a')
def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk. END, task) 
        task_entry.delete(0, "end")
    else: messagebox.showwarning("Error", "Please enter your task.")
    
def delete_task(): 
    task_list.delete(tk.ANCHOR)

def clear_entry(event, entry): 
    entry.delete(0, tk. END)

frame = tk.Frame (win) 
frame.pack(pady=10)

task_list = tk. Listbox (frame, width=25, height=8, font=( 'Times', 18), fg='#464646', selectbackground='#333333', activestyle="none",) 
task_list.pack(side=tk. LEFT, fill=tk. BOTH)

scroll_bar = tk.Scrollbar(frame) 
scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

task_list.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=task_list.yview)

task_entry = tk.Entry(win, font=('times', 24))

task_entry.insert(0, 'Enter Task Here') 
task_entry.bind( "<Button-1>", lambda event: clear_entry(event, task_entry)) 
task_entry.pack(pady=20)

button_frame= tk. Frame (win) 
button_frame.pack(pady=20)

addTask_btn = tk.Button(button_frame, text='Add Task', font=( 'times 14'), bg='green', fg='white', padx=20, pady=10, command=add_task) 
addTask_btn.pack(fill=tk. BOTH, expand=True, side=tk. LEFT)

delTask_btn = tk.Button(button_frame, text='Delete Task', font=('times 14'), bg='red', fg='white', padx=20, pady=10, command=delete_task)

delTask_btn.pack(fill=tk. BOTH, expand=True, side=tk. LEFT)

win.mainloop()