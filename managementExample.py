from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Management Example")
root.resizable(False, False)


def Reset():
    entry_dosa.delete(0, END)
    entry_coockies.delete(0, END)
    entry_tea.delete(0, END)
    entry_cofee.delete(0, END)
    entry_juice.delete(0, END)
    entry_pancakes.delete(0, END)
    entry_eggs.delete(0, END)


def Total():
    try:
        a1 = int(entry_dosa.get())
    except:
        a1 = 0
    try:
        a2 = int(entry_coockies.get())
    except:
        a2 = 0
    try:
        a3 = int(entry_tea.get())
    except:
        a3 = 0
    try:
        a4 = int(entry_cofee.get())
    except:
        a4 = 0
    try:
        a5 = int(entry_juice.get())
    except:
        a5 = 0
    try:
        a6 = int(entry_pancakes.get())
    except:
        a6 = 0
    try:
        a7 = int(entry_eggs.get())
    except:
        a7 = 0

    # cost per quantity
    cost1 = 60*a1
    cost2 = 30*a2
    cost3 = 7*a3
    cost4 = 100*a4
    cost5 = 20*a5
    cost6 = 15*a6
    cost7 = 7*a7

    total_cost = cost1+cost2+cost3+cost4+cost5+cost6+cost7
    string_price = str('%.2f $' % total_cost)
    Total_price = StringVar(value=string_price)

    lbl_total = Label(frame3, font=("aria", 20, "bold"),
                      text="Total", width=16, fg="lightyellow", bg="black")
    lbl_total.place(x=0, y=50)

    entry_total = Entry(frame3, font=("aria", 20, "bold"),
                        textvariable=Total_price, width=15, bd=6, bg="lightgreen", justify=CENTER)
    entry_total.place(x=20, y=100)


Label(text="Management Example", bg="black", fg="white",
      font=("calibri", 33), width="300", height="2").pack()

# MENU CARD
frame = Frame(root, bg="lightgreen", highlightbackground="black",
              highlightthickness=1, width=300, height=370)
frame.place(x=10, y=118)


Label(frame, text="Menu", font=("Gabriola", 40, "bold"),
      fg="black", bg="lightgreen").place(x=80, y=0)
Label(frame, text="Dosa.....Rs.60/plate", font=("Lucida Calligraphy",
      15, "bold"), fg="black", bg="lightgreen").place(x=10, y=80)
Label(frame, text="Cookies.....Rs.30/plate", font=("Lucida Calligraphy",
      15, "bold"), fg="black", bg="lightgreen").place(x=10, y=110)
Label(frame, text="Tea.....Rs.7/cup", font=("Lucida Calligraphy",
      15, "bold"), fg="black", bg="lightgreen").place(x=10, y=140)
Label(frame, text="Cofee.....Rs.100/cup", font=("Lucida Calligraphy",
      15, "bold"), fg="black", bg="lightgreen").place(x=10, y=170)
Label(frame, text="Juice.....Rs.20/glass", font=("Lucida Calligraphy",
      15, "bold"), fg="black", bg="lightgreen").place(x=10, y=200)
Label(frame, text="Pancakes.....Rs.15/pack", font=("Lucida Calligraphy",
      15, "bold"), fg="black", bg="lightgreen").place(x=10, y=230)
Label(frame, text="Eggs.....Rs.7/egg", font=("Lucida Calligraphy",
      15, "bold"), fg="black", bg="lightgreen").place(x=10, y=260)


# Total Prices
frame3 = Frame(root, bg="lightyellow", highlightbackground="black",
               highlightthickness=1, width=300, height=370)
frame3.place(x=690, y=118)

Result = Label(frame3, text="Employee", font=("calibri", 20), bg="lightyellow")
Result.place(x=100, y=10)


# ENTRY WORK
frame2 = Frame(root, bd=5, height=370, width=300, relief=RAISED)
frame2.pack()


dosa = StringVar
cookies = StringVar
tea = StringVar
cofee = StringVar
juice = StringVar
pancakes = StringVar
eggs = StringVar


# Labels

label_dosa = Label(frame2, font=("aria", 20, "bold"),
                   text="Dosa", width=12, fg="blue4")
label_coockies = Label(frame2, font=("aria", 20, "bold"),
                       text="Coockies", width=12, fg="blue4")
label_tea = Label(frame2, font=("aria", 20, "bold"),
                  text="Tea", width=12, fg="blue4")
label_cofee = Label(frame2, font=("aria", 20, "bold"),
                    text="Cofee", width=12, fg="blue4")
label_juice = Label(frame2, font=("aria", 20, "bold"),
                    text="Juice", width=12, fg="blue4")
label_pancakes = Label(frame2, font=("aria", 20, "bold"),
                       text="Pancakes", width=12, fg="blue4")
label_eggs = Label(frame2, font=("aria", 20, "bold"),
                   text="Eggs", width=12, fg="blue4")


label_dosa.grid(row=1, column=0)
label_coockies.grid(row=2, column=0)
label_tea.grid(row=3, column=0)
label_cofee.grid(row=4, column=0)
label_juice.grid(row=5, column=0)
label_pancakes.grid(row=6, column=0)
label_eggs.grid(row=7, column=0)

# Entry
entry_dosa = Entry(frame2, font=("aria", 20, "bold"),
                   textvariable=label_dosa, bd=6, width=8, bg="lightpink", justify=CENTER)
entry_coockies = Entry(frame2, font=("aria", 20, "bold"),
                       textvariable=label_coockies, bd=6, width=8, bg="lightpink", justify=CENTER)
entry_tea = Entry(frame2, font=("aria", 20, "bold"),
                  textvariable=label_tea, bd=6, width=8, bg="lightpink", justify=CENTER)
entry_cofee = Entry(frame2, font=("aria", 20, "bold"),
                    textvariable=label_cofee, bd=6, width=8, bg="lightpink", justify=CENTER)
entry_juice = Entry(frame2, font=("aria", 20, "bold"),
                    textvariable=label_juice, bd=6, width=8, bg="lightpink", justify=CENTER)
entry_pancakes = Entry(frame2, font=("aria", 20, "bold"),
                       textvariable=label_pancakes, bd=6, width=8, bg="lightpink", justify=CENTER)
entry_eggs = Entry(frame2, font=("aria", 20, "bold"),
                   textvariable=label_eggs, bd=6, width=8, bg="lightpink", justify=CENTER)


entry_dosa.grid(row=1, column=1)
entry_coockies.grid(row=2, column=1)
entry_tea.grid(row=3, column=1)
entry_cofee.grid(row=4, column=1)
entry_juice.grid(row=5, column=1)
entry_pancakes.grid(row=6, column=1)
entry_eggs.grid(row=7, column=1)


# Buttons
btn_reset = Button(frame2, fg="black", bg="lightblue", font=(
    "ariel", 16, "bold"), width=10, text="Reset", command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(frame2, fg="black", bg="lightblue", font=(
    "ariel", 16, "bold"), width=10, text="Total", command=Total)
btn_total.grid(row=8, column=1)


root.mainloop()
