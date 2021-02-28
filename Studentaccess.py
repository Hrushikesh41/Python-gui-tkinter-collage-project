#importing tk module 

from tkinter import *

root = Tk()

#giving background
root.configure(background="#B9B7FD")

# in this the variable names are given in arranged manner
# variables are given in alphabetical order
# empty labels are given name starting from e followed by the number e.g.- e1, e2 etc
# variable name for entry are given in such order that they ressemble to the label for which that particular entry has been given e.g. entry for label c has been given name as c1

a=Label(root, text="SELECT THE OPTION BELOW :", font="70px", bg="#B9B7FD")
a.pack()


e1=Label(root, bg="#B9B7FD")
e1.pack()

e2=Label(root, bg="#B9B7FD")
e2.pack()

e3=Label(root, bg="#B9B7FD")
e3.pack()
# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functiontone():
    messagebox.showinfo("OK", "Proceed")
    
A1=Button(root, text="ABOUT BCA PROGRAM",  width="22", font="1px", command=functiontone)
A1.pack()


e4=Label(root, bg="#B9B7FD")
e4.pack()

e5=Label(root, bg="#B9B7FD")
e5.pack()

e6=Label(root, bg="#B9B7FD")
e6.pack()
# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functiontwo():
    messagebox.showinfo("OK", "Best Wishes")
    
    
B1=Button(root, text="SEE RESULTS",  width="22", font="1px",  command=functiontwo)
B1.pack()


e7=Label(root, bg="#B9B7FD")
e7.pack()

e8=Label(root, bg="#B9B7FD")
e8.pack()

e9=Label(root, bg="#B9B7FD")
e9.pack()
# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functionfour():
    messagebox.showinfo("OK", "Proceed")

C1=Button(root, text="UPLOAD ASSIGNMENT",  width="22", font="1px", command=functionfour)
C1.pack()


e10=Label(root, bg="#B9B7FD")
e10.pack()

e11=Label(root, bg="#B9B7FD")
e11.pack()

e12=Label(root, bg="#B9B7FD")
e12.pack()


# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functionfive():
    messagebox.showinfo("OK", "Make Sure You Upload Corrrect Document")
    
    
D1=Button(root, text="UPLOAD DOCUMENT",  width="22", font="1px", command=functionfive)
D1.pack()


e13=Label(root, bg="#B9B7FD")
e13.pack()

e14=Label(root, bg="#B9B7FD")
e14.pack()

e15=Label(root, bg="#B9B7FD")
e15.pack()


# here we import a module messagebox from tkinter
from tkinter import messagebox


def functionseven():
    messagebox.showinfo("OK", "Loged Out Successfully")
    
F1=Button(root, text="LOGOUT",  width="22", font="1px", command=functionseven)
F1.pack()

root.mainloop()
