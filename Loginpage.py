# creating a Python based GUI Application

# start from importing the tkinter package

from tkinter import *

master = Tk()

# giving background colour to application
master.configure(background="#455FEF")

# in this the variable names are given in arranged manner
# variables are given in alphabetical order
# empty labels are given name starting from e followed by the number e.g.- e1, e2 etc
# variable name for entry are given in such order that they ressemble to the label fot which that particular entry has been given e.g. entry for label c has been given name as c1

# we use pack method to position the labels and entry's
a= Label(master, text="WELCOME", font="70px", bg="#455FEF", fg="cyan")
a.pack()

e1=Label(master, bg="#455FEF")
e1.pack()

b= Label(master, text="Login To Continue", font="70px", bg="#455FEF", fg="cyan")
b.pack()

# this is an empty label
e2=Label(master, background="#455FEF")
e2.pack()

# this is an empty label
e3= Label(master, background="#455FEF")
e3.pack()

c= Label(master, text="USERNAME: ", font="70px", bg="#455FEF")
c.pack()
c1=Entry(master, width="40", bd="5")
c1.pack()

# this is an empty label
e4= Label(master, background="#455FEF")
e4.pack()


d= Label(master, text="PASSWORD:", font="70px", bg="#455FEF")
d.pack()
d1=Entry(master, width="40", bd="5")
d1.pack()

# this is an empty label
e5= Label(master, background="#455FEF")
e5.pack()

# giving a submit button
# importing the messagebox

from tkinter import messagebox

def myfunction():
    messagebox.showinfo("Thank You", "Successfull")
    
A1=Button(master, text="SUBMIT", command=myfunction, height="1", width="7", bg="white", fg="black")
A1.pack()

# this is an empty label
e6= Label(master, background="#455FEF")
e6.pack()

e=Label(master, text="FOR FACULTY LOGIN CLICK BELOW", font="70px", bg="#455FEF")
e.pack()

# this is an empty label
e7= Label(master, background="#455FEF")
e7.pack()

def importfunction():
    messagebox.showinfo("Thank You", "Successfull")
     
    
A2=Button(master, text="CLICK HERE", command=importfunction, height="1", width="9", bg="white")
A2.pack()

# this is an empty label
e8= Label(master, background="#455FEF")
e8.pack()


f= Label(master, text="Click The button Below for New Registration", font="70px", bg="#455FEF")
f.pack()


# this is an empty label
e9= Label(master, background="#455FEF")
e9.pack()
def importfunctionone():
     messagebox.showinfo("Thank You", "Successfull")
B2=Button(master, text="CLICK HERE", command=importfunctionone, height="1", width="9", bg="white")
B2.pack()

mainloop()
