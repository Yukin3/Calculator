

import tkinter as tk   #variable for tkinter
from tkinter import messagebox #imports message box for popup messages
import time
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


calculation =  ""  #calculation starts as an empty string
root = tk.Tk()
root.geometry("318x300+500+200")   #sets window GUI size
root.title("Calculator")
root.resizable(False,False)
root.configure(bg = "#808080")

def addToCalculation(symbol):
    global calculation
    calculation += str(symbol) 
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluatenum():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clearField()
        text_result.insert(1.0, "Error")

def delete():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def clearField():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def quit():
    #quit warning
    if messagebox.askyesno("You are about to quit. Your work will not be saved") == True:
        #wait before quiting
        time.sleep(2)
        root.quit()



#button output size
text_result = tk.Text(root, height = 2, width = 15, font=("Arial", 36))   
text_result.grid(columnspan = 5)



#bttns
    #numbers/decimal
bttn1 = tk.Button(root, text = "1", command = lambda: addToCalculation(1), width = 5, font = ("Arial", 14))    #lambda refers to function rather than imemediately calls
bttn1.grid(row = 1, column = 0)
bttn2 = tk.Button(root, text = "2", command = lambda: addToCalculation(2), width = 5, font = ("Arial", 14))
bttn2.grid(row = 1, column = 1)
bttn3 = tk.Button(root, text = "3", command = lambda: addToCalculation(3), width = 5, font = ("Arial", 14))
bttn3.grid(row = 1, column = 2)
bttn4 = tk.Button(root, text = "4", command = lambda: addToCalculation(4), width = 5, font = ("Arial", 14))
bttn4.grid(row = 2, column = 0)
bttn5 = tk.Button(root, text = "5", command = lambda: addToCalculation(5), width = 5, font = ("Arial", 14))
bttn5.grid(row = 2, column = 1)
bttn6 = tk.Button(root, text = "6", command = lambda: addToCalculation(6), width = 5, font = ("Arial", 14))
bttn6.grid(row = 2, column = 2)
bttn7 = tk.Button(root, text = "7", command = lambda: addToCalculation(7), width = 5, font = ("Arial", 14))
bttn7.grid(row = 3, column = 0)
bttn8 = tk.Button(root, text = "8", command = lambda: addToCalculation(8), width = 5, font = ("Arial", 14))
bttn8.grid(row = 3, column = 1)
bttn9 = tk.Button(root, text = "9", command = lambda: addToCalculation(9), width = 5, font = ("Arial", 14))
bttn9.grid(row = 3, column = 2)
bttn0 = tk.Button(root, text = "0", command = lambda: addToCalculation(0), width = 5, font = ("Arial", 14))
bttn0.grid(row = 4, column = 0)
bttnDcml = tk.Button(root, text = ".", command = lambda: addToCalculation("."), width = 5, font = ("Arial", 14))
bttnDcml.grid(row = 6, column = 0)



    #operations
bttnPls = tk.Button(root, text = "+", command = lambda: addToCalculation("+"), width = 5, font = ("Arial", 14))
bttnPls.grid(row = 1, column = 3)
bttnMns = tk.Button(root, text = "-", command = lambda: addToCalculation("-"), width = 5, font = ("Arial", 14))
bttnMns.grid(row = 2, column = 3)
bttnMltply = tk.Button(root, text = "x", command = lambda: addToCalculation("*"), width = 5, font = ("Arial", 14))
bttnMltply.grid(row = 3, column = 3)
bttnDvd = tk.Button(root, text = "/", command = lambda: addToCalculation("/"), width = 5, font = ("Arial", 14))
bttnDvd.grid(row = 4, column = 3)
bttnLprnths = tk.Button(root, text = "(", command = lambda: addToCalculation("("), width = 5, font = ("Arial", 14))
bttnLprnths.grid(row = 4, column = 1)
bttnRprnths = tk.Button(root, text = ")", command = lambda: addToCalculation(")"), width = 5, font = ("Arial", 14))
bttnRprnths.grid(row = 4, column = 2)
bttnEql = tk.Button(root, text = "=", command = lambda: evaluatenum(), width = 15, font = ("Arial", 14))
bttnEql.grid(row = 5, column = 0, columnspan = 2)



    #commands
bttnDel = tk.Button(root, text = "Del", command = lambda: delete(), width = 5, font = ("Arial", 14))
bttnDel.grid(row = 5, column = 2)
bttnClr = tk.Button(root, text = "Clr", command = lambda: clearField(), width = 5, font = ("Arial", 14))
bttnClr.grid(row = 5, column = 3)
bttnQuit = tk.Button(root, text = "Close Calculator", command = lambda: quit(), width = 25, font = ("Arial", 14))
bttnQuit.grid(row = 6, column = 1, columnspan = 3)



root.mainloop()


