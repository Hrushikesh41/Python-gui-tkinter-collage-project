#importing tk module 

from tkinter import *

nd = Tk()

#giving background
nd.configure(background="#F9ED86")

# in this the variable names are given in arranged manner
# variables are given in alphabetical order
# empty labels are given name starting from e followed by the number e.g.- e1, e2 etc
# variable name for entry are given in such order that they ressemble to the label for which that particular entry has been given e.g. entry for label c has been given name as c1

a=Label(nd, text="MAKE SURE TO UPLOAD RIGHT DOCUMENT", font="70px", bg="#F9ED86")
a.pack()

e1=Label(nd, bg="#F9ED86")
e1.pack()

e2=Label(nd, bg="#F9ED86")
e2.pack()

e3=Label(nd, bg="#F9ED86")
e3.pack()

b=Label(nd, text="Paste the path of your Document", font="60px", bg="#F9ED86")
b.pack(anchor=W)

c=Label(nd, text="The Document should be in pdf/jpg/png format and should not exceed size more than 5MB", font="60px", bg="#F9ED86")
c.pack(anchor=W)

e4=Label(nd, bg="#F9ED86")
e4.pack()

e5=Label(nd, bg="#F9ED86")
e5.pack()

d=Label(nd, text="Upload Birth Certificate", font="60px", bg="#F9ED86")
d.pack(anchor=W)
d1=Entry(nd, width="40", bd="5")
d1.pack(anchor=W)


e6=Label(nd, bg="#F9ED86")
e6.pack()

e7=Label(nd, bg="#F9ED86")
e7.pack()

e=Label(nd, text="Upload SSC Marksheet", font="60px", bg="#F9ED86")
e.pack(anchor=W)
a1=Entry(nd, width="40", bd="5")
a1.pack(anchor=W)

e8=Label(nd, bg="#F9ED86")
e8.pack()

e9=Label(nd,bg="#F9ED86")
e9.pack()

f=Label(nd, text="Upload Your HSC Document", font="60px", bg="#F9ED86")
f.pack(anchor=W)
f1=Entry(nd, width="40", bd="5")
f1.pack(anchor=W)

e10=Label(nd, bg="#F9ED86")
e10.pack()

e11=Label(nd, bg="#F9ED86")
e11.pack()

g=Label(nd, text="Address Proof(Aadhar Card/ Driving Liscense/ Electric bill)", font="60px", bg="#F9ED86")
g.pack(anchor=W)
g1=Entry(nd, width="40", bd="5")
g1.pack(anchor=W)

e12=Label(nd, bg="#F9ED86")
e12.pack()

e13=Label(nd, bg="#F9ED86")
e13.pack()

h=Label(nd, text="School Leaving Certificate", font="60px", bg="#F9ED86")
h.pack(anchor=W)
h1=Entry(nd, width="40", bd="5")
h1.pack(anchor=W)


e14=Label(nd, bg="#F9ED86")
e14.pack()

e15=Label(nd, bg="#F9ED86")
e15.pack()

# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functionone():
    messagebox.showinfo("OK", "Uploaded")
    
A1=Button(nd, text="UPLOAD",  width="14", font="1px", command=functionone)
A1.pack()

e16=Label(nd, bg="#F9ED86")
e16.pack()

def functiontwo():
    messagebox.showinfo("OK", "Loged Out Successfully")
    
B1=Button(nd, text="LOGOUT",  width="14", font="1px", command=functiontwo)
B1.pack()

mainloop()
