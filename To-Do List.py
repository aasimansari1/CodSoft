from tkinter import *

r = Tk()

def delete_task():
    lb.delete(lb.curselection())

def add_task():
    def add_task_final():
        task = inp.get()
        lb.insert(END, task)
        win.destroy()
        
    win = Tk()
    inp = Entry(win)
    inp.pack()
    confirm = Button(win,text="OK", command=add_task_final)
    confirm.pack()
    confirm_not = Button(win,text="Cancel", command=win.destroy)
    confirm_not.pack()
    win.mainloop()

r.title("ToDo List app")
r.geometry("400x400")

add_task_button = Button(r,text="Add Task", font=("Arial",25), command=add_task)
add_task_button.place(x=0,y=0)
delete_task_button = Button(r,text="Delete Task", font=("Arial",25), command=delete_task)
delete_task_button.place(x=230,y=0)
lb = Listbox(r,width=250,height=300)
lb.place(x=0,y=50)
r.mainloop()