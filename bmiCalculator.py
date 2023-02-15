from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.configure(bg="#f0f1f5")

ruta="C:/Users/ferna/Downloads/python/DeTodoUnPoco/images/"

def BMI():
    h=float(Height.get())
    w=float(Weight.get())

    m=h/100
    bmi=round(float(w/m**2), 1)
    label1.config(text=bmi)
    if(bmi>16 and bmi<25):
        label2.config(text="  Normal!")
        label3.config(text="It indicates that you are healty!")
    elif(bmi<16):
        label2.config(text="Underweight!")
        label3.config(text="You have lower weight then normal body!")
    elif(bmi>25 and bmi<29.9):
        label2.config(text="OverWeight!")
        label3.config(text="It indicates that a person is \nslightly overweight!\nA doctor may advise to lose some\nweight for health reasons!")
    else:
        label2.config(text="    Obes!")
        label3.config(text="Health may be at risk, if they do not\n lose weight!")




#icon
image_icon=PhotoImage(file=ruta+"bmi3.png")
root.iconphoto(False, image_icon)

#top
top=PhotoImage(file=ruta+"top.png")
top_image=Label(root, image=top, background="#f0f1f5")
top_image.place(x=85, y=10)

#bottom box
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

#two boxes
box=PhotoImage(file=ruta+"box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

#scale
scale=PhotoImage(file=ruta+"scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=310)



##############Slider1#############
current_value=tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    size=int(float(get_current_value()))
    img=(Image.open(ruta+"man.png"))
    resized_image=img.resize((50, 10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondImage.config(image=photo2)
    secondImage.place(x=70,y=550-size)
    secondImage.image=photo2

style=ttk.Style()
style.configure("TScale", background="white")

slider=ttk.Scale(root, from_=0, to=220, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=80, y=250)


#Slider2
current_value2=tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

style2=ttk.Style()
style2.configure("TScale", background="white")

slider2=ttk.Scale(root, from_=0, to=200, orient='horizontal', command=slider_changed2, variable=current_value2)
slider2.place(x=290, y=250)






#Entry box
Height=StringVar()
Weight=StringVar()

height=Entry(root, textvariable=Height, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=35, y=160)

Height.set(get_current_value())
Weight.set(get_current_value2())


weight=Entry(root, textvariable=Weight, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)


#man image
secondImage=Label(root, bg="lightblue")
secondImage.place(x=70, y=530)

Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=280, y=340)

label1=Label(root, font="arial 45 bold", bg="lightblue", fg="#fff")
label1.place(x=125, y=322)

label2=Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=230, y=430)

label3=Label(root, font="arial 10 bold", bg="lightblue")
label3.place(x=200, y=470)



root.mainloop()