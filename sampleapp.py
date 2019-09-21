##https://www.youtube.com/watch?v=D8-snVfekto
##https://github.com/KeithGalli/GUI
##https://www.tutorialspoint.com/python3/tk_button.htm
from tkinter import *
from tkinter import messagebox

import tkinter as tk # used at _QueryDialog for tkinter._default_root

root=tk.Tk()

Height=500
Width=600

#root.mainloop()
Canvas=tk.Canvas(root, height=Height, width=Width)
Canvas.pack()

frame=tk.Frame(root, bg='blue')
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

button=tk.Button(frame,text="Test",bg="gray")
#button.pack()
#button.pack(side='left',fill='both',expand=True)
#button.grid(row=0,column=0)
button.place(relx=0,rely=0,relwidth=0.25,relheight=0.25)

label=tk.Label(frame,text="Path of the file : ",bg='red')
#label.pack()
#label.pack(side='left',fill='both',expand=True)
#label.grid(row=0,column=1)
label.place(relx=0.3,rely=0,relwidth=0.45,relheight=0.25)

entry=tk.Entry(frame,bg='yellow')
#entry.pack()
#entry.pack(side='left',fill='both',expand=True)
#entry.grid(row=0,column=2)
entry.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.2)

#button1=tk.Button(root,text="Test1",bg="gray")
#button1.pack()

tk.mainloop()