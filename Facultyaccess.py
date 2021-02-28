#importing tk module 

from tkinter import *

ne = Tk()

#giving background
ne.configure(background="#8EDBFF")

# in this the variable names are given in arranged manner
# variables are given in alphabetical order
# empty labels are given name starting from e followed by the number e.g.- e1, e2 etc
# variable name for entry are given in such order that they ressemble to the label fot which that particular entry has been given e.g. entry for label c has been given name as c1


a=Label(ne, text=" ACCESS YOUR ACCOUNT", font="100px", fg="blue", bg="yellow")
a.grid(row=0)

e1=Label(ne, bg="#8EDBFF")
e1.grid(row=1)

e2=Label(ne, bg="#8EDBFF")
e2.grid(row=2)


b=Label(ne, text="SELECT YOUR DEPARTMENT", font="70px", bg="#8EDBFF")
b.grid(row=3)


from tkinter import messagebox

mb=Menubutton(ne, text="Select Your Department")
mb.grid(row=3, column=2)

mb.menu=Menu(mb, tearoff=0)
mb["menu"]=mb.menu

bca=IntVar()
mca=IntVar()
bba=IntVar()
mba=IntVar()
bsc=IntVar()
msc=IntVar()
btech=IntVar()
mtech=IntVar()

mb.menu.add_checkbutton(label="BCA", variable=bca)
mb.menu.add_checkbutton(label="MCA", variable=mca)
mb.menu.add_checkbutton(label="BBA", variable=bba)
mb.menu.add_checkbutton(label="MBA", variable=mba)
mb.menu.add_checkbutton(label="BSC", variable=bsc)
mb.menu.add_checkbutton(label="MSC", variable=msc)
mb.menu.add_checkbutton(label="B-Tech", variable=btech)
mb.menu.add_checkbutton(label="M-Tech", variable=mtech)
mb.grid(row=3, column=2)

e3=Label(ne, bg="#8EDBFF")
e3.grid(row=4)

e4=Label(ne, bg="#8EDBFF")
e4.grid(row=5)

c=Label(ne, text="MARKS ENTRY", font="70px", bg="#8EDBFF", fg="red")
c.grid(row=6)

e5=Label(ne, bg="#8EDBFF")
e5.grid(row=7)

e6=Label(ne, bg="#8EDBFF")
e6.grid(row=8)


d=Label(ne, text="SELECT ROLE NO:", font="70px", bg="#8EDBFF")
d.grid(row=9)

ma=Menubutton(ne, text="Select Roll No")
ma.grid(row=9, column=2)

ma.menu=Menu(ma, tearoff=0)
ma["menu"]=ma.menu

rno=IntVar()
ma.menu.add_radiobutton(label="20102001", variable=rno)
ma.menu.add_radiobutton(label="20102002", variable=rno)
ma.menu.add_radiobutton(label="20102003", variable=rno)
ma.menu.add_radiobutton(label="20102004", variable=rno)
ma.menu.add_radiobutton(label="20102005", variable=rno)
ma.menu.add_radiobutton(label="20102006", variable=rno)
ma.menu.add_radiobutton(label="20102007", variable=rno)
ma.menu.add_radiobutton(label="20102008", variable=rno)
ma.menu.add_radiobutton(label="20102009", variable=rno)
ma.menu.add_radiobutton(label="20102010", variable=rno)


e7=Label(ne, bg="#8EDBFF")
e7.grid(row=10)

e8=Label(ne, bg="#8EDBFF")
e8.grid(row=11)

e=Label(ne, text=" MARKS OF SUBJECT 1:", font="70px", bg="#8EDBFF")
e.grid(row=12)
a1=Entry(ne, width="40", bd="5")
a1.grid(row=12, column=2)

e9=Label(ne, bg="#8EDBFF")
e9.grid(row=12, column=3)


# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functiontone():
    messagebox.showinfo("OK", "Submitted")
    
A1=Button(ne, text="SUBMIT",  width="7",  command=functiontone)
A1.grid(row=12, column=4)


e10=Label(ne, bg="#8EDBFF")
e10.grid(row=13)


e11=Label(ne, bg="#8EDBFF")
e11.grid(row=14, column=3)


f=Label(ne, text=" MARKS OF SUBJECT 2:", font="70px", bg="#8EDBFF")
f.grid(row=14)
f1=Entry(ne, width="40", bd="5")
f1.grid(row=14, column=2)

# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functiontwo():
    messagebox.showinfo("OK", "Submitted")
    
B1=Button(ne, text="SUBMIT",  width="7",  command=functiontwo)
B1.grid(row=14, column=4)



e12=Label(ne, bg="#8EDBFF")
e12.grid(row=15)

e13=Label(ne, bg="#8EDBFF")
e13.grid(row=16)

g=Label(ne, text="ENTER NOTES", font="70px", fg="red", bg="#8EDBFF")
g.grid(row=17)


e14=Label(ne, bg="#8EDBFF")
e14.grid(row=18)

e15=Label(ne, bg="#8EDBFF")
e15.grid(row=18)


e16=Label(ne, text="SELECT SUBJECT CODE:", font="70px", bg="#8EDBFF")
e16.grid(row=19)


ma1=Menubutton(ne, text="Select Subject Code:")
ma1.grid(row=19, column=2)

ma1.menu=Menu(ma1, tearoff=0)
ma1["menu"]=ma1.menu

s1=IntVar()
s2=IntVar()
s3=IntVar()
s4=IntVar()
s5=IntVar()
s6=IntVar()
s7=IntVar()
s8=IntVar()
s9=IntVar()


ma1.menu.add_checkbutton(label="CS 101", variable=s1)
ma1.menu.add_checkbutton(label="CS 110", variable=s2)
ma1.menu.add_checkbutton(label="CS 161", variable=s3)
ma1.menu.add_checkbutton(label="CS 108", variable=s4)
ma1.menu.add_checkbutton(label="CS 163", variable=s5)
ma1.menu.add_checkbutton(label="CS 162", variable=s6)
ma1.menu.add_checkbutton(label="MA 154", variable=s7)
ma1.menu.add_checkbutton(label="LC 131", variable=s8)
ma1.menu.add_checkbutton(label="CS 109", variable=s9)
ma1.grid(row=19, column=2)

e17=Label(ne, font="70px", bg="#8EDBFF")
e17.grid(row=20)


h=Label(ne,text="ADD NOTES:", font="70px", bg="#8EDBFF")
h.grid(row=21)
h1=Entry(ne,width="80", bd="5")
h1.grid(row=21, column=2)


e18=Label(ne, bg="#8EDBFF")
e18.grid(row=22)


e19=Label(ne, bg="#8EDBFF")
e19.grid(row=23)


i=Label(ne, text="UPLOAD VIDEO LECTURE", font="70px", fg="red", bg="#8EDBFF")
i.grid(row=24)


e20=Label(ne, bg="#8EDBFF")
e20.grid(row=25)


e21=Label(ne, bg="#8EDBFF")
e21.grid(row=26)


j=Label(ne, text="ENTER URL :", font="70px", bg="#8EDBFF")
j.grid(row=27)
j1=Entry(ne, width="40", bd="5")
j1.grid(row=27, column=2)


e22=Label(ne, bg="#8EDBFF")
e22.grid(row=27, column=3)


# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functionthree():
    messagebox.showinfo("OK", "Submitted")
    
C1=Button(ne, text="SUBMIT",  width="7",  command=functionthree)
C1.grid(row=27, column=4)


e23=Label(ne, bg="#8EDBFF")
e23.grid(row=28)

e24=Label(ne, bg="#8EDBFF")
e24.grid(row=29)


# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functionfour():
    messagebox.showinfo("OK", "Loged out Successfully")
    
C1=Button(ne, text="LOGOUT", height="1", width="14", font="1px",  command=functionfour)
C1.grid(row=30)



mainloop()

