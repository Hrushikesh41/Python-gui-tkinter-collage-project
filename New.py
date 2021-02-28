# we again start from importing the tkinter package
from tkinter import *
master= Tk()

# giving background to the application
master.configure(background="#64C0E3")

# in this the variable names are given in arranged manner
# variables are given in alphabetical order
# empty labels are given name starting from e followed by the number e.g.- e1, e2 etc
# variable name for entry are given in such order that they ressemble to the label fot which that particular entry has been given e.g. entry for label d has been given name as d1


# giving labels and entry's using grid method to position them
a=Label(master, text="REGISTER HERE", font="100px", bg="yellow", fg="red")
a.grid(row=0)

# this is an empty label to give spacing between the 2 labels 
e1=Label(master, bg="#64C0E3")
e1.grid(row=1)

b=Label(master, text="PERSONAL DETAILS", font="70px", bg="#64C0E3", fg="blue").grid(row=2)

# this is an empty label
e2=Label(master, bg="#64C0E3")
e2.grid(row=3)

# this is an empty label
e3=Label(master, bg="#64C0E3")
e3.grid(row=4)

c=Label(master, text="FIRST NAME :", font="60px", bg="#64C0E3")
c.grid(row=5)
c1=Entry(master, width="40", bd="5")
c1.grid(row=5, column=2)

# here to keep it in same line with label first name we will give same number of row which is given in label first name
# for input box we give specific column number 
d=Label(master, text="LAST NAME :", font="60px", bg="#64C0E3")
d.grid(row=5, column=4)
d1=Entry(master, width="40", bd="5")
d1.grid(row=5, column=6)

# this is an empty label
e4=Label(master, bg="#64C0E3")
e4.grid(row=6)

e=Label(master, text="GENDER :", font="60px", bg="#64C0E3")
e.grid(row=7)

# defining a user define function for radio buttons
# as it a radio button we give same variable
    
var=IntVar()
A1 = Radiobutton(master, text="Male", variable=var, value=1,  bg="#64C0E3", font="40px")
A1.grid(row=7, column=2)

A2 = Radiobutton(master, text="Female", variable=var, value=2, bg="#64C0E3", font="40px")
A2.grid(row=7, column=3)

A3= Radiobutton(master, text="Others", variable=var, value=3,  bg="#64C0E3", font="40px")
A3.grid(row=7, column=4)


# this is an empty label
e5=Label(master, bg="#64C0E3")
e5.grid(row=8)

# this is an empty label
e6=Label(master, bg="#64C0E3")
e6.grid(row=9)

f=Label(master, text="CONTACT DETAILS", font="70px", bg="#64C0E3", fg="blue")
f.grid(row=10)

# this is an empty label
e7=Label(master, bg="#64C0E3")
e7.grid(row=11)

# this is an empty label
e8=Label(master, bg="#64C0E3")
e8.grid(row=12)

g=Label(master, text="MOBILE NO:", font="60px", bg="#64C0E3")
g.grid(row=13)
g1=Entry(master, width="40", bd="5")
g1.grid(row=13, column=2)


h=Label(master, text="TELEPHONE NO:", font="60px", bg="#64C0E3")
h.grid(row=13, column=4)
h1=Entry(master, width="40", bd="5")
h1.grid(row=13, column=6)

# this is an empty label
e9=Label(master, bg="#64C0E3")
e9.grid(row=14)

i=Label(master, text="FATHER'S CONTACT NO:", font="60px", bg="#64C0E3")
i.grid(row=15)
i1=Entry(master, width="40", bd="5")
i1.grid(row=15, column=2)

j=Label(master, text="MOTHER'S CONTACT NO:", font="60px", bg="#64C0E3")
j.grid(row=15, column=4)
j1=Entry(master, width="40", bd="5")
j1.grid(row=15, column=6)

# this is an empty label
e10=Label(master, bg="#64C0E3")
e10.grid(row=16)

# this is an empty label
e11=Label(master, bg="#64C0E3")
e11.grid(row=17)

k=Label(master, text="EDUCATIONAL QUALIFICATION", font="70px", fg="blue", bg="#64C0E3")
k.grid(row=18)

# this is an empty label
e12=Label(master, bg="#64C0E3")
e12.grid(row=19)

# this is an empty label
e13=Label(master, bg="#64C0E3")
e13.grid(row=20)

l=Label(master, text="SSC PERCENTAGE:", font="60px", bg="#64C0E3")
l.grid(row=21)
l1=Entry(master, width="40", bd="5")
l1.grid(row=21, column=2)

m=Label(master, text="HSC PERCENTAGE:", font="60px", bg="#64C0E3")
m.grid(row=21, column=4)
m1=Entry(master, width="40", bd="5")
m1.grid(row=21, column=6)

# this is an empty label
e14=Label(master, bg="#64C0E3")
e14.grid(row=22)


# this is an empty label
e15=Label(master, bg="#64C0E3")
e15.grid(row=23)

n=Label(master, text="LOGIN DETAILS", font="70px", fg="blue", bg="#64C0E3")
n.grid(row=24)

# this is an empty label
e16=Label(master, bg="#64C0E3")
e16.grid(row=25)

o=Label(master, text="USERNAME:", font="60px", bg="#64C0E3")
o.grid(row=26)
o1=Entry(master, width="40", bd="5")
o1.grid(row=26, column=2)

p=Label(master, text="PASSWORD:", font="60px", bg="#64C0E3")
p.grid(row=26, column=4)
p1=Entry(master, width="40", bd="5")
p1.grid(row=26, column=6)
q=Label(master, text="(This will be used as your Password)", bg="#64C0E3")
q.grid(row=26, column=7)

r=Label(master, text="(This will be used as your Username)", bg="#64C0E3")
r.grid(row=27, column=2)


# this is an empty label
e17=Label(master, bg="#64C0E3")
e17.grid(row=27)

s=Label(master, text="CONFIRM PASSWORD", font="60px", bg="#64C0E3")
s.grid(row=28, column=4)
s1=Entry(master, width="40", bd="5")
s1.grid(row=28, column=6)


# this is an empty label
e18=Label(master, bg="#64C0E3")
e18.grid(row=29)

# here we import a module messagebox from tkinter
from tkinter import messagebox

# defining another user define function for the submit button
def functiontone():
    messagebox.showinfo("OK", "Proceed With Login")
    import Loginpage
B1=Button(master, text="SUBMIT", height="1", width="14", font="1px", command=functiontone)
B1.grid(row=30)

mainloop()

