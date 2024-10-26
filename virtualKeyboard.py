import tkinter as tk
from tkinter import *
win=tk.Tk()
win.title("On screen Keyboard")
win.configure(background="Cadet Blue")
win.geometry("1260x500+100+100")
win.resizable(0,0)
lblTitle=Label(win,width=39,bg="Cadet Blue",font=("arial",40,"bold"),text="\tOn Screen Keyboard\t",padx=12)
lblTitle.grid(row=0,column=0)
MainFrame=Frame(win,bg="Powder Blue",bd=10,width=1250,height=490,relief=RIDGE )
MainFrame.grid(row=1,column=0,padx=30)
keys=[['1','2','3','4','5','6','7','8','9','0','-','='],
      ['Q','W','E','R','T','Y','U','I','O','P','[',']'],
      ['A','S','D','F','G','H','J','K','L',';','"','"'],
      ['Z','X','C','V','B','N','M',',','.','/','<','>']
     ]
for i,key_row in enumerate(keys):
    for j,key in enumerate(key_row):
        tk.Button(MainFrame,text=key,width=7,height=2 ).grid(row=i,column=j)

display=tk.Entry(MainFrame,font=("arial",28,"bold"),bd=5,width=54)
display.grid(row=len(keys),column=0,columnspan=len(keys[0]),pady=10)
def button_click(key):
    current=display.get()
    display.delete(0,tk.END)
    display.insert(0,str(current)+str(key))

for i,key_row in enumerate(keys):
    for j,key in enumerate(key_row):
        tk.Button(MainFrame,font=("arial",14,"bold"),text=key,width=7,height=2,command=lambda key=key:button_click(key) ).grid(row=i,column=j)
