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
    master.destroy
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
        root.destroy()
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

        def functionone():
            na.destroy()
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
            # submit button for last login page (about)
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
                messagebox.showinfo("Thank You","Successfull")
            # click here button for last login page (about)
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
                messagebox.showinfo("Welcome","Welcome")
            # click here button for last login page (about)
            B2=Button(master, text="CLICK HERE", command=importfunctionone, height="1", width="9", bg="white")
            B2.pack()

        # logout button for about page    
        A1=Button(na, text="LOGOUT",  width="22", font="1px", command=functionone)
        A1.pack()


    # about button for student access page
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
        root.destroy()
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
        # see results button for result page 
        A1=Button(nb, text="SEE RESULTS",  width="22", font="1px", command=functionone)
        A1.pack()

        e6=Label(nb, bg='#82FDD1')
        e6.pack()

        def functiontwo():
            nb.destroy()
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
            # submit button for last login page (results)
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
                messagebox.showinfo("Thank You","Successfull")
            # click here button for last login page (results)
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
                messagebox.showinfo("Welcome","Welcome")
            # click here button for last login page (results)
            B2=Button(master, text="CLICK HERE", command=importfunctionone, height="1", width="9", bg="white")
            B2.pack()

        # logout button for see resulte page    
        A1=Button(nb, text="LOGOUT",  width="22", font="1px", command=functiontwo)
        A1.pack()



    # see results button for student access page
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
        root.destroy
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
        # upload button for assignment page
        A1=Button(nc, text="UPLOAD",  width="14", font="1px", command=functionone)
        A1.pack()

        e10=Label(nc, bg="#0080FF")
        e10.pack()

        def functiontwo():
            nc.destroy()
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
            # submit button for last login page (assignment)
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
                messagebox.showinfo("Thank You","Successfull")
            # click here button for last login page (assignment)
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
                messagebox.showinfo("Welcome","Welcome")
            # click here button for last login page (assignments)
            B2=Button(master, text="CLICK HERE", command=importfunctionone, height="1", width="9", bg="white")
            B2.pack()

        # logout button for assignment page    
        B1=Button(nc, text="LOGOUT",  width="14", font="1px", command=functiontwo)
        B1.pack()



        
    # upload assignment button for student access page 
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
        root.destroy()
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
        # upload button for documents page
        A1=Button(nd, text="UPLOAD",  width="14", font="1px", command=functionone)
        A1.pack()

        e16=Label(nd, bg="#F9ED86")
        e16.pack()

        def functiontwo():
            nd.destroy()
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
            # submit button for last login page (documents)
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
                messagebox.showinfo("Thank You","Successfull")
            # click here button for last login page (documents)
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
                messagebox.showinfo("Welcome","Welcome")
            # click here button for last login page (documents)
            B2=Button(master, text="CLICK HERE", command=importfunctionone, height="1", width="9", bg="white")
            B2.pack()

        # logout button for documents page     
        B1=Button(nd, text="LOGOUT",  width="14", font="1px", command=functiontwo)
        B1.pack()



    # upload documents button for student access page 
    D1=Button(root, text="UPLOAD DOCUMENT",  width="22", font="1px", command=functionfive)
    D1.pack()


    e13=Label(root, bg="#B9B7FD")
    e13.pack()

    e14=Label(root, bg="#B9B7FD")
    e14.pack()

    e15=Label(root, bg="#B9B7FD")
    e15.pack()

    def functionseven():
        root.destroy()
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
        # submit button for last login page (student access)
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
            messagebox.showinfo("Thank You","Successfull")
        # click here last login page (student access)
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
            messagebox.showinfo("Welcome","Welcome")
        # click here button for last login page (student access)
        B2=Button(master, text="CLICK HERE", command=importfunctionone, height="1", width="9", bg="white")
        B2.pack()


    # logut button for student access page
    F1=Button(root, text="LOGOUT",  width="22", font="1px", command=functionseven)
    F1.pack()


# Submit button of first page
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


#faculty login starts here
def importfunction():
    master.destroy()
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
        nm.destroy()
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


        d=Label(ne, text="SELECT ROLL NO:", font="70px", bg="#8EDBFF")
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
        ma.grid(row=9, column=2)

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
        # first submit button for faculty access page 
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
        # second submit button for faculty access page
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
        # last submit button for faculty access page
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
            ne.destroy()
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
            # submit button for last login page (faculty access)
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
                messagebox.showinfo("Thank You","Successfull")
            #click here button for last click here (faculty access)
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
                messagebox.showinfo("Welcome","Welcome")
            # Click here of last page of facultyaccess
            B2=Button(master, text="CLICK HERE", command=importfunctionone, height="1", width="9", bg="white")
            B2.pack()

         # logout button of facultyaccess  page 
        C1=Button(ne, text="LOGOUT", height="1", width="14", font="1px",  command=functionfour)
        C1.grid(row=30)


    # login button of first facultylogin page    
    A1=Button(nm, text="LOGIN", height="1", width="14", font="1px", command=myfunction)
    A1.pack()


# click here button of first login page for faculty login
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

# start of new reg page
def importfunctionone():
    master.destroy()
    nh= Tk()

    # giving background to the application
    nh.configure(background="#64C0E3")

    # in this the variable names are given in arranged manner
    # variables are given in alphabetical order
    # empty labels are given name starting from e followed by the number e.g.- e1, e2 etc
    # variable name for entry are given in such order that they ressemble to the label fot which that particular entry has been given e.g. entry for label d has been given name as d1


    # giving labels and entry's using grid method to position them
    a=Label(nh, text="REGISTER HERE", font="100px", bg="yellow", fg="red")
    a.grid(row=0)

    # this is an empty label to give spacing between the 2 labels 
    e1=Label(nh, bg="#64C0E3")
    e1.grid(row=1)

    b=Label(nh, text="PERSONAL DETAILS", font="70px", bg="#64C0E3", fg="blue").grid(row=2)

    # this is an empty label
    e2=Label(nh, bg="#64C0E3")
    e2.grid(row=3)

    # this is an empty label
    e3=Label(nh, bg="#64C0E3")
    e3.grid(row=4)

    c=Label(nh, text="FIRST NAME :", font="60px", bg="#64C0E3")
    c.grid(row=5)
    c1=Entry(nh, width="40", bd="5")
    c1.grid(row=5, column=2)

    # here to keep it in same line with label first name we will give same number of row which is given in label first name
    # for input box we give specific column number 
    d=Label(nh, text="LAST NAME :", font="60px", bg="#64C0E3")
    d.grid(row=5, column=4)
    d1=Entry(nh, width="40", bd="5")
    d1.grid(row=5, column=6)

    # this is an empty label
    e4=Label(nh, bg="#64C0E3")
    e4.grid(row=6)

    e=Label(nh, text="GENDER :", font="60px", bg="#64C0E3")
    e.grid(row=7)

    # defining a user define function for radio buttons
    # as it a radio button we give same variable
    def myfunction():
        sel= "" + str(var.get())
    
    var=IntVar()
    A1 = Radiobutton(nh, text="Male", variable=var, value=1, command=myfunction, bg="#64C0E3", font="40px")
    A1.grid(row=7, column=2)

    A2 = Radiobutton(nh, text="Female", variable=var, value=2, command=myfunction, bg="#64C0E3", font="40px")
    A2.grid(row=7, column=3)

    A3= Radiobutton(nh, text="Others", variable=var, value=3, command=myfunction, bg="#64C0E3", font="40px")
    A3.grid(row=7, column=4)


    # this is an empty label
    e5=Label(nh, bg="#64C0E3")
    e5.grid(row=8)

    # this is an empty label
    e6=Label(nh, bg="#64C0E3")
    e6.grid(row=9)

    f=Label(nh, text="CONTACT DETAILS", font="70px", bg="#64C0E3", fg="blue")
    f.grid(row=10)

    # this is an empty label
    e7=Label(nh, bg="#64C0E3")
    e7.grid(row=11)

    # this is an empty label
    e8=Label(nh, bg="#64C0E3")
    e8.grid(row=12)

    g=Label(nh, text="MOBILE NO:", font="60px", bg="#64C0E3")
    g.grid(row=13)
    g1=Entry(nh, width="40", bd="5")
    g1.grid(row=13, column=2)


    h=Label(nh, text="TELEPHONE NO:", font="60px", bg="#64C0E3")
    h.grid(row=13, column=4)
    h1=Entry(nh, width="40", bd="5")
    h1.grid(row=13, column=6)

    # this is an empty label
    e9=Label(nh, bg="#64C0E3")
    e9.grid(row=14)

    i=Label(nh, text="FATHER'S CONTACT NO:", font="60px", bg="#64C0E3")
    i.grid(row=15)
    i1=Entry(nh, width="40", bd="5")
    i1.grid(row=15, column=2)

    j=Label(nh, text="MOTHER'S CONTACT NO:", font="60px", bg="#64C0E3")
    j.grid(row=15, column=4)
    j1=Entry(nh, width="40", bd="5")
    j1.grid(row=15, column=6)

    # this is an empty label
    e10=Label(nh, bg="#64C0E3")
    e10.grid(row=16)

    # this is an empty label
    e11=Label(nh, bg="#64C0E3")
    e11.grid(row=17)

    k=Label(nh, text="EDUCATIONAL QUALIFICATION", font="70px", fg="blue", bg="#64C0E3")
    k.grid(row=18)

    # this is an empty label
    e12=Label(nh, bg="#64C0E3")
    e12.grid(row=19)

    # this is an empty label
    e13=Label(nh, bg="#64C0E3")
    e13.grid(row=20)

    l=Label(nh, text="SSC PERCENTAGE:", font="60px", bg="#64C0E3")
    l.grid(row=21)
    l1=Entry(nh, width="40", bd="5")
    l1.grid(row=21, column=2)

    m=Label(nh, text="HSC PERCENTAGE:", font="60px", bg="#64C0E3")
    m.grid(row=21, column=4)
    m1=Entry(nh, width="40", bd="5")
    m1.grid(row=21, column=6)

    # this is an empty label
    e14=Label(nh, bg="#64C0E3")
    e14.grid(row=22)


    # this is an empty label
    e15=Label(nh, bg="#64C0E3")
    e15.grid(row=23)

    n=Label(nh, text="LOGIN DETAILS", font="70px", fg="blue", bg="#64C0E3")
    n.grid(row=24)

    # this is an empty label
    e16=Label(nh, bg="#64C0E3")
    e16.grid(row=25)

    o=Label(nh, text="USERNAME:", font="60px", bg="#64C0E3")
    o.grid(row=26)
    o1=Entry(nh, width="40", bd="5")
    o1.grid(row=26, column=2)

    p=Label(nh, text="PASSWORD:", font="60px", bg="#64C0E3")
    p.grid(row=26, column=4)
    p1=Entry(nh, width="40", bd="5")
    p1.grid(row=26, column=6)
    q=Label(nh, text="(This will be used as your Password)", bg="#64C0E3")
    q.grid(row=26, column=7)

    r=Label(nh, text="(This will be used as your Username)", bg="#64C0E3")
    r.grid(row=27, column=2)


    # this is an empty label
    e17=Label(nh, bg="#64C0E3")
    e17.grid(row=27)

    s=Label(nh, text="CONFIRM PASSWORD", font="60px", bg="#64C0E3")
    s.grid(row=28, column=4)
    s1=Entry(nh, width="40", bd="5")
    s1.grid(row=28, column=6)


    # this is an empty label
    e18=Label(nh, bg="#64C0E3")
    e18.grid(row=29)

    # here we import a module messagebox from tkinter
    from tkinter import messagebox

    # defining another user define function for the submit button
    def functiontone():
        nh.destroy()
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
        # login button of last login page (new reg)
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
            messagebox.showinfo("Thank You","Successfull")
        # click here button of last login page (new reg)
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
            messagebox.showinfo("Welcome","Welcome")
        # click here button of last login page (new reg)
        B2=Button(master, text="CLICK HERE", command=importfunctionone, height="1", width="9", bg="white")
        B2.pack()

    # submit button for new reg page    
    B1=Button(nh, text="SUBMIT", height="1", width="14", font="1px", command=functiontone)
    B1.grid(row=30)

# click here button for first login page     
B2=Button(master, text="CLICK HERE", command=importfunctionone, height="1", width="9", bg="white")
B2.pack()

mainloop()
