from tkinter import *
from tkinter.constants import *
import os
import pyautogui

def internet():
    os.system(r'"C:\Program Files (x86)\Google\Chrome\Application\chrome"')
    pyautogui.click(700, 50)
    pyautogui.typewrite('gmx.ch')


window = Tk()
window.geometry('200x200')
frame = Frame(window)
frame.pack(fill=BOTH)
label = Label(frame, text="Hello, World")
label.pack(fill=X)
button = Button(frame, text="Gmx", command= internet)
button.pack(expand=2)
window.mainloop()
