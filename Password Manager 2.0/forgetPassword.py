import db
from tkinter import *
import main
import bcrypt
import login

def resetPassword(root,username,password):
    
    #creating the hash of the password provided to be stored in the db
    salt=bcrypt.gensalt()
    bytepass=password.encode('UTF-8')
    encpass=bcrypt.hashpw(bytepass,salt)
    print(bytepass,salt,encpass)

    db.updateMaster(encpass,username)

    frameL=Frame(root)
    frameL.config(background='#009688')
    frameL.place(x=main.screenwidth(root)//2,y=main.screenheight(root)//3)   
    l1=Label(frameL,text='Password reset successfull',font=('arial', 10, 'bold'), relief="groove", fg="red",bg="#CDDC39")
    l1.pack()
    login.signin(root)


def forgetPassword(root,username):
    print("inside forgetPassword Method")
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    data=db.fetchfromStore(username)
    if data ==None:

        print("User Not Found")
        frame4=Frame(root)
        frame4.config(background='#009688')
        frame4.place(x=ws/2.5,y=hs/3)   
        l1=Label(frame4,text='User Not Found',font=('arial', 10, 'bold'), relief="groove", fg="red",bg="#CDDC39")
        l1.pack()
        l1.after(5000,l1.forget)
    else:
        print("user found")
        widget_list = main.all_children(root)
        for item in widget_list:
            item.destroy()
        #********************************************
        password=StringVar(root)
        cpassword=StringVar(root)
        wd=ws/3.5
        ht=hs/5
                
        frame7=Frame(root)
        frame7.config(background='#009688')
        frame7.place(x=wd,y=ht+75)
        l4=Label(frame7,height=1,width=20,text='Password',font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39")
        e4=Entry(frame7,textvariable=password,show='*')
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
        b1=Button(frame6,text='Reset Password', height="1",width="12", bd=5, font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: resetPassword(root,username,password.get()))
        b2=Button(frame6,text='Cancle', height="1",width="12", bd=5, font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: main.exitFunc(root))
        b3=Button(frame6,text='Login', height="1",width="12", bd=5, font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: login.signin(root))

        b1.pack(side=LEFT,padx=10)
        b2.pack(side=LEFT,padx=10)
        b3.pack(side=LEFT,padx=10) 
        #********************************************

def forgetPasswordUI(root):
    widget_list = main.all_children(root)
    for item in widget_list:
        item.destroy()

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    username=StringVar(root)    
    frame1=Frame(root)
    frame1.config(background='#009688')
    frame1.place(x=ws/3.5,y=hs/4)   
    l1=Label(frame1,text='Username',font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39")
    e1=Entry(frame1,textvariable=username)
    l1.config(height=2,width=20)
    e1.config(font=('arial', 10),width=20)
    l1.pack(side=LEFT)
    e1.pack(side=LEFT,padx=10)

    frame3 = Frame(root, background='#009688', padx=5, pady=5)
    frame3.place(x=ws/4,y=hs/4+100)
    b1=Button(frame3,text='Check User', height="1",width="20", bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: forgetPassword(root,username.get()))
    b1.pack(side=LEFT,padx=10)



