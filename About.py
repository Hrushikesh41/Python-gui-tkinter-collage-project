#importing tk module 

from tkinter import *

na = Tk()

#giving background
na.configure(background="#8080FF")

# in this the variable names are given in arranged manner
# variables are given in alphabetical order
# empty labels are given name starting from e followed by the number e.g.- e1, e2 etc
# variable name for entry are given in such order that they ressemble to the label fot which that particular entry has been given e.g. entry for label c has been given name as c1


# we use pack method to position the labels and entry's
a=Label(na, text="WELCOME", font="150px", bg="#8080FF")
a.pack()

# this is an empty label
e1=Label(na, bg='#8080FF')
e1.pack()


b=Label(na, text="BCA- BACHELORS IN COMPUTER APPLICATION", font='80px', bg='#8080FF')
b.pack()

# this is an empty label
e2=Label(na, bg='#8080FF')
e2.pack()

# this is an empty label
e3=Label(na, bg='#8080FF')
e3.pack()


c=Label(na, text="About BCA Program :", font="70px",bg='#8080FF')
c.pack(anchor=W)

# this is an empty label
e4=Label(na, bg='#8080FF')
e4.pack()

# this is an empty label
e5=Label(na, bg='#8080FF')
e5.pack()


d=Label(na, text="This is a unique program focussing on hands-on experience with different technologies and its applications in real life. BCA is a 3-year program ",font='70px', bg='#8080FF')
d.pack(anchor=W)


e=Label(na, text="BCA is a program designed to meet the evolving requirements of the IT sector and to produce a dynamic breed of computer professionals with excellent managerial skills", font="70px", bg='#8080FF')
e.pack(anchor=W)


f=Label(na, text="Starting with the basic introduction of computer architecture and programming concepts to web design and database management, and leading to advanced studies",font="70px", bg='#8080FF')
f.pack(anchor=W)


# this is an empty label
e6=Label(na, bg='#8080FF')
e6.pack()


# this is an empty label
e7=Label(na, bg='#8080FF')
e7.pack()


g=Label(na, text="BCA Subjects :",font="70px", bg='#8080FF')
g.pack(anchor=W)


# this is an empty label
e8=Label(na, bg='#8080FF')
e8.pack()


# this is an empty label
e9=Label(na, bg='#8080FF')
e9.pack()


h=Label(na, text="1.  DIGITAL COMPUTER ARCHITECTURE (DCA)",font="70px", bg='#8080FF')
h.pack(anchor=W)


i=Label(na, text="2.  PROGRAMMING CONCEPT AND ALGORITHM (PCA) AND IT'S APPLICATION",font="70px", bg='#8080FF')
i.pack(anchor=W)


j=Label(na, text="3.  WEB DESIGN AND PROGRAMMING CONCEPT (WDPC) AND IT'S APPLICATION",font="70px", bg='#8080FF')
j.pack(anchor=W)


k=Label(na, text="4.  COMPUTER NETWORKS 1 (CN1)",font="70px", bg='#8080FF')
k.pack(anchor=W)


l=Label(na, text="5.  FOUNDATION OF BASIC MATHEMATICIS",font="70px", bg='#8080FF')
l.pack(anchor=W)


m=Label(na, text="6.  BASICS OF COMMUNICATION (BC)",font="70px", bg='#8080FF')
m.pack(anchor=W)


n=Label(na, text="7.  INTODUCTION TO COMPUTER (ITC)",font="70px", bg='#8080FF')
n.pack(anchor=W)


# this is an empty label
e10=Label(na, bg='#8080FF')
e10.pack()


# this is an empty label
e11=Label(na, bg='#8080FF')
e11.pack()


o=Label(na, text="Marking System :",font="70px", bg='#8080FF')
o.pack(anchor=W)


# this is an empty label
e12=Label(na, bg='#8080FF')
e12.pack()


p=Label(na, text="Internals will carry 60 marks followed by an END Sem exams of 40 marks.",font="70px", bg='#8080FF')
p.pack(anchor=W)


q=Label(na, text="The 60 Marks in Internals inculdes Assignment, Submission of daily practicals, Class Test, Viva's, Projects (can be group or indivisual) and most importantly Class Participation.",font="70px", bg='#8080FF')
q.pack(anchor=W)

e13=Label(na, bg='#8080FF')
e13.pack()

def functionseven():
    messagebox.showinfo("OK", "Loged Out Successfully")
    
A1=Button(na, text="LOGOUT",  width="22", font="1px", command=functionseven)
A1.pack()

mainloop()
