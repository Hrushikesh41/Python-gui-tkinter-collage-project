#importing tk module 

from tkinter import *

nc = Tk()

#giving background
nc.configure(background="#0080FF")

a=Label(nc, text="UPLOAD YOUR ASSIGNMENT", font="70px", bg="#0080FF")
a.pack()

e1=Label(nc, bg="#0080FF")
e1.pack()

e2=Label(nc, bg="#0080FF")
e2.pack()

b=Label(nc, text="UPLOAD ASSIGNMENT FOR BETTER GRADES", font="70px", bg="#0080FF")
b.pack()

e3=Label(nc, bg="#0080FF")
e3.pack()

e4=Label(nc, bg="#0080FF")
e4.pack()

c=Label(nc, text="SELECT SUBJECT", font="70px", bg="#0080FF")
c.pack(anchor=W)


e5=Label(nc, bg="#0080FF")
e5.pack()


ma1=Menubutton(nc, text="Select Subject:")


ma1.menu=Menu(ma1, tearoff=0)
ma1["menu"]=ma1.menu

s=IntVar()

ma1.menu.add_radiobutton(label="CS 101", variable=s)
ma1.menu.add_radiobutton(label="CS 110", variable=s)
ma1.menu.add_radiobutton(label="CS 161", variable=s)
ma1.menu.add_radiobutton(label="CS 108", variable=s)
ma1.menu.add_radiobutton(label="CS 163", variable=s)
ma1.menu.add_radiobutton(label="CS 162", variable=s)
ma1.menu.add_radiobutton(label="MA 154", variable=s)
ma1.menu.add_radiobutton(label="LC 131", variable=s)
ma1.menu.add_radiobutton(label="CS 109", variable=s)
ma1.pack(anchor=W)

e6=Label(nc, bg="#0080FF")
e6.pack()


e7=Label(nc, bg="#0080FF")
e7.pack()

d=Label(nc, text="Paste the path of the Document ", font="70px", bg="#0080FF")
d.pack(anchor=W)

e8=Label(nc, bg="#0080FF")
e8.pack()

d1=Entry(nc, width="40", bd="5")
d1.pack(anchor=W)

e=Label(nc, text="(Note that Assignment to be uploaded should be in pdf format)", font="70px", bg="#0080FF")
e.pack(anchor=W)

e9=Label(nc, bg="#0080FF")
e9.pack()


# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functionone():
    messagebox.showinfo("OK", "Uploaded")
    
A1=Button(nc, text="UPLOAD",  width="14", font="1px", command=functionone)
A1.pack()

e10=Label(nc, bg="#0080FF")
e10.pack()

def functiontwo():
    messagebox.showinfo("OK", "Loged Out Successfully")
    
B1=Button(nc, text="LOGOUT",  width="14", font="1px", command=functiontwo)
B1.pack()

mainloop()
