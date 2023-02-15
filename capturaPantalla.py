import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

#Interface
try:
    def createWigets():
        save=Label(vn, text='Directory:', font=('Arial', 12))
        save.grid(row=1, column= 0, padx=5, pady= 5)

        vn.textSave=Entry(vn, width=30)
        vn.textSave.grid(row=1, column=1, padx=5, pady=5)
        buttomSave=Button(vn, text="Save", width=10, command=Navegate)
        buttomSave.grid(row=1, column=2, padx=5, pady=5)
        buttomCapture=Button(vn, text="Capture", width=10, command=capture)
        buttomCapture.grid(row=2, column=1, padx=5, pady=5)
except:
    print("an issue has occurred")

def Navegate():
    vn.fileName=filedialog.asksaveasfilename(title="Save",
                                                  initialdir="C:/Users/ferna/Downloads",
                                                  defaultextension=".png",
                                                  filetypes=(("File Png", "*.png"), 
                                                             ("File jpg", "*.jpg"),   
                                                             ("File jpge", "*.jpge"),
                                                             ("All files", "*.*")))

    vn.textSave.insert("1", vn.fileName)

def capture():
    capture=pyautogui.screenshot()
    capture.save(vn.fileName)
    messagebox.showinfo("Success", "The capture has been taken successfully")







vn=tk.Tk()
vn.title("Screenshot")
createWigets()
vn.mainloop()








