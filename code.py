from tkinter import *
import random
import pyperclip

root = Tk()
root.geometry("1000x500")
passwrd = StringVar()

def generate(): 
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', '!', '@', '#', '$', '%', '^', '&', '*']
    password = "".join(random.choice(pass1) for _ in range(6)) 
    passwrd.set(password)

def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)

Label(root, text="Password Generator", font="Arial 50 bold").pack()
Button(root, text="Generate Password", font="Arial 13 bold", command=generate).pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=7)
Button(root, text="Copy to Clipboard", font="Arial 13 bold", command=copyclipboard).pack()

root.mainloop()
