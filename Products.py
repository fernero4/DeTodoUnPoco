from tkinter import ttk
from tkinter import *
import sqlite3
import os

class Product:
    
    def __init__(self, window):
        self.wind=window
        self.wind.title('Products app')

        #frame
        frame=LabelFrame(self.wind, text='Register a new product', font=("Arial", 12, 'bold'), fg="black")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        label1=Label(frame, text='Name: ', font=("Arial", 12))
        label1.grid(row=1, column=0)
        self.name=Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        #price
        Label(frame, text='Price', font=("Arial", 12)).grid(row=2, column=0)
        self.price=Entry(frame)
        self.price.grid(row=2, column=1)

        #Buttom
        ttk.Button(frame, text='Save product', command=self.add_product).grid(row=3, columnspan=2, sticky=W+E)
        ttk.Button(text='Delete', command=self.delete_product).grid(row=5, column=0, sticky=W+E)
        ttk.Button(text='Edit', command=self.edit_product).grid(row=5, column=1, sticky=W+E)


        #Messages
        self.message=Label(text='', fg="red")
        self.message.grid(row=3, column=0, columnspan=2, sticky=W+E)


        #table
        self.tree=ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Name', anchor=CENTER)
        self.tree.heading('#1', text='Price', anchor=CENTER)
        self.get_products()
    

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "ProductsDataBase.db")

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_path) as conn:
            cursor=conn.cursor()
            result=cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_products(self):
        #cleaning table
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        #query
        query='SELECT * FROM product ORDER BY name DESC'
        db_rows=self.run_query(query)
        
        #filling data
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])

    def validate(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0
            
    def add_product(self):
        if self.validate():
            query='INSERT INTO product VALUES(NULL, ?, ?)'
            parameters=(self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text']='Product {} added successfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)

        else:
            self.message['text']='Name and Price is required'

        self.get_products()
    
    def delete_product(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        
        except IndexError as e:
            self.message['text']='Please Select a Record'
            return
        self.message['text']=''
        name=self.tree.item(self.tree.selection())['text']        
        query='DELETE FROM product WHERE name = ?'
        self.run_query(query, (name, ))
        self.message['text']='Record {} deleted Successfully'.format(name)
        self.get_products()

    def edit_product(self):
        pass





if (__name__=='__main__'):
    window=Tk()
    app=Product(window)
    window.resizable(False, False)
    window.mainloop()


