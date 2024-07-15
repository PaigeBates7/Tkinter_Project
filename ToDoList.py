#Author: Paige Bates
#Date Written: 06/20/2024
#Module 06 Project Status Report II
#The program will allow you to open two windows, one being a to-do list and the other is a login form.

#Importing Tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font

#Creating The First WebPage - Will Be Defined As: 1WP
root = Tk()
root.title('ToDo-List')
root.geometry("600x600")
root.config(background="#00FFFF")

#Creating Main ToDoList Label For 1WB
label = Label(root, text="To-Do-List")
label.pack()

#Creating The Second WebPage - Will Be Defined As: 2WP
root2 = Tk()
root2.title('Login-List')
root2.geometry("400x400")
root2.config(background="#00FFFF")

#Creating Main Login Form Label For 2WP
label = Label(root2, text="Login Form")
label.pack()

#Creating The Frame 1WB
frame =Frame(root)
frame.pack(pady=10) 

#Creathing The Frames 2WP
frames=Frame(root2)
frames.pack(pady=10)

#Creating Username And Password Label For WP2
username_label = Label(root2, text="Enter Username",)         
username_label.place(x=150, y=40) 
password_label = Label(root2, text="Enter Password")                        
password_label.place(x=150, y=100)     

#Creating The Font Style For 1WP
font =Font(root,
    family="Footlight MT Light",
    size=25,
    weight="normal",)

#Creating The Font Style For 1WP
font =Font(root2,
    family="Footlight MT Light",
    size=25,
    weight="normal",)

#Creating The Listbox For To-Do-List Entry For 1WB
list =Listbox(frame,
    width = 40,
    height=20,                                                       
    bd=0,
    font = font,
    selectbackground="#04D8B2",
    fg="#04D8B2",
    highlightthickness=3,
    activestyle="none",)
list.pack(side=LEFT,)

#Creating Label For User To Enter Their ToDoList For 1WP
label = Label(root, text="Enter Your To-Do-List Here:")
label.pack()

#Creating The Scrollbar For The ToDoList So The User Can Enter As Many Inputs As They Need 1WP
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill="y")

#Adding Scrollbar For ToDoList 1WP
list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list.yview)

#Creating List Boxes 1WP
entry = Entry(root, font=("Footlight MT Light", 14))
entry.pack(pady=20)

#Creating Entry Boxes For Username And Password For 2WP
username = Entry(root2, font=("Footlight MT Light", 14))
username.place(x=80, y=60)                                      
password = Entry(root2,font=("Footlight MT Light", 14))
password.place(x=80, y=120)

#Creating Labels To Let The User Know Where They Can Add, Delete, Or Complete Their ToDoList Items 1WP
label = Label(root, text="Add,Delete,or Complete your To-Do-List here:")
label.pack()

#Creating Button Frame For 1WP
button_frame = Frame(root)
button_frame.pack(pady=20)

#Creating Button Frames For 2WP
button_frames = Frame(root)
button_frames.pack(pady=20)

#Creating Button Functions For Delete, Add, and Complete Buttons, 1WP
def delete_item():
    list.delete(ANCHOR)
def add_item():
    list.insert(END, entry.get())
    entry.delete(0,END)
def complete_item():
    list.itemconfig(list.curselection(),
    fg="#04D8B2")                                                                      
    list.selection_clear(0, END)
def delete_completed():
    count = 0
    while count < list.size():
        if list.itemcget(count, "fg") == "#04D8B2":
            list.delete(list.index(count))
        else:
            count += 1
#Adding Menu Functions To Save, Exit, and Delete The File/Inputs, 1WP
def Save():
    file = filedialog.asksaveasfile(initialdir="C:\\User\paige\OneDrive\SDEV140\ToDoList.py",
                                    defaultextension='.txt',
                                    title="Save As",
                                    filetypes=(
                                        ("Text file",".txt"),
                                        ("All files","*.*"))
    )
    filetext =str(1.0,END)
    file.wrirte(filetext)
    file.close()
def Exit():
    root.destroy()
def Delete():
    list.delete(0,END)

#Creating Menu 1WP
menu = Menu(root)
root.config(menu=menu) 

#Adding The Menu 1WP
main_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=main_menu)

#Adding The Menu File 1WP
main_menu.add_command(label="Save", command=Save)
main_menu.add_command(label="Exit", command=Exit)
main_menu.add_separator()
main_menu.add_command(label="Delete", command=Delete)

#Adding The Buttons For 1WP
delete_button = Button(button_frame, text="Delete Item", command=delete_item) 
add_button = Button(button_frame, text="Add Item", command=add_item)
complete_button = Button(button_frame, text="Complete Item", command=complete_item)
delete_complete_button = Button(button_frame, text="Delete Completed Items", command=delete_completed)

#Placing The Buttons For 1WP
delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=15)
complete_button.grid(row=0, column=2)
delete_complete_button.grid(row=0, column=4)

root.mainloop()
root.mainloop()