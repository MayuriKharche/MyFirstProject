from tkinter import *
from tkinter import messagebox
import mysql.connector
          
root=Tk()                               
root.title("LOGIN ")                
root.geometry('1200x1000')

def valid_digit(inp):                                       
    if inp.isdigit():
        return True
    elif inp=='':
        return True
    else:
        return False
    return

reg1 = root.register(valid_digit)

l=Label(root,text="LOGIN")
l.pack
l1=Label(root,text="Username :")
l1.pack()
l2=Label(root,text="UPI PIN :")
l2.pack()

e1=Entry(root)
e1.pack()
e1.config(validate = "key", validatecommand = (reg1,'%P'))
e2=Entry(root)
e2.pack()

b1=Button(root,text="login", fg="blue", command="Login")
b1.pack()
b2=Button(root,text="cancel", fg="blue", command="Cancel")
b2.pack()

l.place(x=595,y=265)
l1.place(x=500,y=300)
e1.place(x=600,y=300)
l2.place(x=500,y=330)
e2.place(x=600,y=330)
b1.place(x=560,y=360)
b2.place(x=640,y=360)

ac = e1.get()
pin = e2.get()

conn = mysql.connector.connect(host="localhost",username="root",passwd="root",database="banking")
cursor = conn.cursor()
conn.commit()

root.mainloop()
