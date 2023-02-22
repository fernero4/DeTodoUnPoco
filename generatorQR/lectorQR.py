from tkinter import *
import qrcode
import qrcode.image.svg

IMAG_PATH="C:/Users/ferna/Downloads/python/DeTodoUnPoco/generatorQR/"

root=Tk()
root.title("Qr generator")
root.geometry("1000x500")
root.config(bg="#AE2321")
root.resizable(False, False)

#icon image
image_icon=PhotoImage(file=IMAG_PATH+"icon.png")
root.iconphoto(False, image_icon)


def Generate_QR():
    name=title.get()
    text=content.get()
    qr=qrcode.make(text)
    qr.save(IMAG_PATH+str(name)+".png")

    global image_QR
    image_QR=PhotoImage(file=IMAG_PATH+str(name)+".png")
    label_QR.config(image=image_QR)

label_QR=Label(root, bg="#AE2321")
label_QR.pack(padx=50, pady=10, side=RIGHT)

Label(root, text="TITLE OF QR", fg="white", bg="#AE2321", font=("arial", 15)).place(x=50, y=170)
title=Entry(root, width=13, font=("Microsoft YaHei UI Light", 15))
title.place(x=50, y=200)

content=Entry(root, width=28, font=("Microsoft YaHei UI Light", 15))
content.place(x=50, y=250)
Button(root, text="Generate", width=20, height=2, bg="black", fg="white", command=Generate_QR).place(x=50, y=300)

root.mainloop()