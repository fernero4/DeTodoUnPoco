from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator
import googletrans
import textblob


root = Tk()
root.title("Translator")
root.geometry("1080x400")
root.configure(bg="white")


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

# path of images
Images_Path = "C:/Users/ferna/Downloads/python/DeTodoUnPoco/images/"


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)


def translate_text():
    global language
    try:
        text_ = text1.get(1.0, END)
        if (text_):
            translator=Translator()
            words = textblob.TextBlob(text_)
            lan = combo2.get()

            for i, j in language.items():
                if (j == lan):
                    language_traslate = i

            words = translator.translate(text_, dest=language_traslate)
            words=words.text
            text2.delete(1.0, END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror("Translator", "Please try again!")

# icon
icon_image = PhotoImage(file=Images_Path+"icon.png")
root.iconphoto(False, icon_image)

# arrow/image
arrow_image = PhotoImage(file=Images_Path+"arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)


# combos
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUEGE")


# labels
label1 = Label(root, text="ENGLISH", font="segoe 30 bold",
               bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

label2 = Label(root, text="ENGLISH", font="segoe 30 bold",
               bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# frames
f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

f2 = Frame(root, bg="black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

# text
text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

text2 = Text(f2, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

# scrolbar
scrolbar1 = Scrollbar(f)
scrolbar1.pack(side="right", fill="y")
scrolbar1.configure(command=text1.yview)

scrolbar2 = Scrollbar(f2)
scrolbar2.pack(side="right", fill="y")
scrolbar2.configure(command=text2.yview)


text1.configure(yscrollcommand=scrolbar1.set)
text2.configure(yscrollcommand=scrolbar1.set)

# translate button
translate = Button(root, text="Translate", font=("Roboto 15 bold italic"),
                   activebackground="white", cursor="hand2", bd=1,
                   bg="black", fg="white", command=translate_text)
translate.place(x=480, y=250)


label_change()

root.mainloop()
