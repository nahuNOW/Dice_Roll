import random
import time as t
import tkinter
from tkinter import messagebox

keepRolling = True

def rollDice():
    num = random.randint(1,6)
    messagebox.showinfo("Result", num)


def createWindow():
    window = tkinter.Tk()
    window.title("Roll a dice")

    rollButton = tkinter.Button(window, width=25, height=10, text="Roll Dice", command=rollDice)
    rollButton.pack(pady=10)

    window.mainloop()

createWindow()