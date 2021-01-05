#importing Libraries
from tkinter import *
import random, string
import pyperclip

# user defined functions
# GENERATOR used to generate random password
def Generator():
    sampleSet = string.ascii_letters + string.digits + string.punctuation
    passOutput = ''.join(random.choice(sampleSet) for i in range(int(passLen.get())))
    password.delete('1.0',END)
    password.insert(INSERT,passOutput)

# CopyToClipBoard used to copy the generated password from textbox to system ClipBoard
def CopyToClipBoard():
    pyperclip.copy(password.get('1.0',END))

# initialize window
root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("YAY - PASSWORD GENERATOR")

# GUI
Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
passLen = Spinbox(root, from_ = 8, to = 32)
passLen.pack()
Button(root, text = "GENERATE PASSWORD", command = Generator).pack(pady= 5)
password = Text(root, height = 1, width = 17)
password.pack()
Button(root, text = "Copy To Clip Board", command = CopyToClipBoard).pack(pady= 5)

root.mainloop()
