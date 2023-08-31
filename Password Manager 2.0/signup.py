import bcrypt
import main
import db
from tkinter import *
import login


# to create new user accounts
def createMasterAccount(root,firstName,lastName,email,password,cpassword):
    print("User Provided values are",firstName,lastName,email,password,cpassword)

    #checking if the password and confirm password is same
    if password==cpassword:
        print("Password matched, creating the user account")

        #creating the hash of the password provided to be stored in the db
        salt=bcrypt.gensalt()
        bytepass=password.encode('UTF-8')
        encpass=bcrypt.hashpw(bytepass,salt)
        print(bytepass,salt,encpass)

        db.insertIntoMaster(firstName,lastName,email,encpass)

        print("user created")
        signUp(root)
    
        # enter the value provided into the db 
    else:
        print("password did not match")
        signUp(root)



def signUp(root):

    # clearing previous widgets
    widget_list = main.all_children(root)
    for item in widget_list:
        item.destroy()

    print("create an account button clicked")
    root.title("Sing up Page")
    
    fname=StringVar(root)
    lname=StringVar(root)
    emailid=StringVar(root)
    password=StringVar(root)
    cpassword=StringVar(root)
    wd=main.screenwidth(root)/3.5
    ht=main.screenheight(root)/5
    frame1=Frame(root)
    frame1.config(background='#009688')
    frame1.place(x=wd,y=ht)  
       
    l1=Label(frame1,height=1,width=20,text='First Name',font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39")

    l1.pack(side=LEFT)
    e1=Entry(frame1,textvariable=fname)
    e1.pack(side=LEFT,padx=10)

    frame2=Frame(root)
    frame2.config(background='#009688')
    frame2.place(x=wd,y=ht+25)
    l2=Label(frame2,height=1,width=20,text='Last Name',font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39")
    e2=Entry(frame2,textvariable=lname)
    l2.pack(side=LEFT)
    e2.pack(side=LEFT,padx=10)


    frame3=Frame(root)
    frame3.config(background='#009688')
    frame3.place(x=wd,y=ht+50)
    l3=Label(frame3,height=1,width=20,text='Email ID',font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39")
    e3=Entry(frame3,textvariable=emailid)
    l3.pack(side=LEFT)    
    e3.pack(side=LEFT,padx=10)

    frame4=Frame(root)
    frame4.config(background='#009688')
    frame4.place(x=wd,y=ht+75)
    l4=Label(frame4,height=1,width=20,text='Password',font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39")
    e4=Entry(frame4,textvariable=password,show='*')
    l4.pack(side=LEFT)
    e4.pack(side=LEFT,padx=10)

    frame5=Frame(root)
    frame5.config(background='#009688')
    frame5.place(x=wd,y=ht+100)
    l5=Label(frame5,height=1,width=20,text='confirm Password',font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39")
    e5=Entry(frame5,textvariable=cpassword,show='*')
    l5.pack(side=LEFT)
    e5.pack(side=LEFT,padx=10)

    

    frame6=Frame(root)
    frame6.config(background='#009688')
    frame6.place(x=wd-25,y=ht+150)       
    b1=Button(frame6,text='Submit', height="1",width="12", bd=5, font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: createMasterAccount(root,fname.get(),lname.get(),emailid.get(),password.get(),cpassword.get()))
    b2=Button(frame6,text='Cancle', height="1",width="12", bd=5, font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: main.exitFunc(root))
    b3=Button(frame6,text='Login', height="1",width="12", bd=5, font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: login.signin(root))

    b1.pack(side=LEFT,padx=10)
    b2.pack(side=LEFT,padx=10)
    b3.pack(side=LEFT,padx=10)