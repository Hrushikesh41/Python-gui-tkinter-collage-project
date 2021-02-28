#importing tk module 

from tkinter import *

nm = Tk()

#giving background
nm.configure(background="#6FF2A7")

# in this the variable names are given in arranged manner
# variables are given in alphabetical order
# empty labels are given name starting from e followed by the number e.g.- e1, e2 etc
# variable name for entry are given in such order that they ressemble to the label fot which that particular entry has been given e.g. entry for label c has been given name as c1

a=Label(nm, text="WELCOME TO FACULTY LOGIN", font="100px", bg="#6FF2A7")
a.pack()

# this is an empty label 
e1=Label(nm, bg="#6FF2A7")
e1.pack()

# this is an empty label 
e2=Label(nm, bg="#6FF2A7")
e2.pack()


b=Label(nm, text="USERNAME:", font="70px", bg="#6FF2A7")
b.pack()

# this is an empty label 
e3=Label(nm, bg="#6FF2A7")
e3.pack()

b1=Entry(nm, width="40", bd="5")
b1.pack()

# this is an empty label 
e4=Label(nm, bg="#6FF2A7")
e4.pack()

c=Label(nm, text="PASSWORD:", font="70px", bg="#6FF2A7")
c.pack()

# this is an empty label 
e5=Label(nm, bg="#6FF2A7")
e5.pack()

c1=Entry(nm, width="40", bd="5")
c1.pack()

# this is an empty label 
e6=Label(nm, bg="#6FF2A7")
e6.pack()


# we import a modulemessagebox from tkinter
from tkinter import messagebox

def myfunction():
    messagebox.showinfo("OK","Proceed")
A1=Button(nm, text="LOGIN", height="1", width="14", font="1px", command=myfunction)
A1.pack()

mainloop()   
