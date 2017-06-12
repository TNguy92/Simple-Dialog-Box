##Thomas Nguyen
from tkinter import *
import tkinter.messagebox

root = Tk()
def enterName():
    tkinter.messagebox.showinfo("Continue", "You must enter your name")

def quitBox():
    quitAns = tkinter.messagebox.askquestion("Quit" , "Are you sure?" )


answer = tkinter.messagebox.askquestion('Simple Dialog Box - Thomas Nguyen', "Do you want to enter your name?")

if answer == 'yes':
    enterName()

if answer == 'no':
    quitBox()

root.mainloop()