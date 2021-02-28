#importing tk module 

from tkinter import *

nb = Tk()

#giving background
nb.configure(background="#82FDD1")

# in this the variable names are given in arranged manner
# variables are given in alphabetical order
# empty labels are given name starting from e followed by the number e.g.- e1, e2 etc
# variable name for entry are given in such order that they ressemble to the label for which that particular entry has been given e.g. entry for label c has been given name as c1

a=Label(nb, text="ALL THE BEST", font="70px", bg="#82FDD1")
a.pack()

e1=Label(nb, bg="#82FDD1")
e1.pack()

e2=Label(nb, bg="#82FDD1")
e2.pack()

b=Label(nb, text="ENTER ROLL NO:", font="70px", bg="#82FDD1")
b.pack(anchor=W)

e3=Label(nb, bg="#82FDD1")
e3.pack()

b1=Entry(nb, width="40", bd="5")
b1.pack(anchor=W)

e4=Label(nb, bg="#82FDD1")
e4.pack()

e5=Label(nb, bg="#82FDD1")
e5.pack()


# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functionone():
    e7=Label(nb, text="", bg="#82FDD1")
    e7.pack()
    l1=Label(nb, text="Passed With 75%", font="100px")
    l1.pack()

A1=Button(nb, text="SEE RESULTS",  width="22", font="1px", command=functionone)
A1.pack()

e6=Label(nb, bg='#82FDD1')
e6.pack()

def functiontwo():
    messagebox.showinfo("OK", "Loged out Successfully")

A1=Button(nb, text="LOGOUT",  width="22", font="1px", command=functiontwo)
A1.pack()

mainloop()
