import main
from tkinter import *
import db
import bcrypt
import signup
import userInterface
import forgetPassword


def credCheckMasterAccount(root,userName,passw):

    # check if the username and password entered is correct by checking the value in the db
    #refreshing the window to load new UI
    widget_list = main.all_children(root)
    for item in widget_list:
        item.destroy()

    rows=db.fetchfromMaster(userName)

    wd=main.screenwidth(root)/3.5
    ht=main.screenheight(root)/5

    if rows ==None:
        # add message that user does not exists
        print("User not available, Pelase signup first")
        signup.signUp(root)
        # add logic if the user does not provide any input and click on the login button
    else:
        u,p=rows
        bytepass=passw.encode('UTF-8')
        if bcrypt.checkpw(bytepass,p):
                    
            frame3 = Frame(root,background='#009688')
            frame3.place(x=wd-80,y=ht-100)
            Button(frame3,text='Add New Credentials to Vault', bd=5, width=25, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: userInterface.saveCredentialsUI(root,userName)).pack(padx=10,side=LEFT)
            Button(frame3,text='Show all Credentials', bd=5,width=25, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: home(root,userName)).pack(padx=10,side=LEFT)
            Button(frame3,text='Exit', bd=5,width=25, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: main.exitFunc(root)).pack(padx=10,side=LEFT)
            
            data=db.fetchfromStore(userName)

            if len(data) ==0:
                frame0 = Frame(root,background='#009688')
                frame0.place(x=wd+150,y=ht+150)
                l1=Label(frame0,text='! No Stored Credetnails',font=('arial', 20, 'bold'), relief="groove", fg="red",bg="#CDDC39")
                l1.pack(side=TOP)

            else:
                
                frame1 = Frame(root,background='#009688')
                frame1.place(x=wd-70,y=ht-10) 
                Label(frame1,text='userID',bd=2,width=16,font=('arial', 12, 'bold'), relief="groove", fg="#303F9F",bg="#B2DFDB").pack(side=LEFT)
                Label(frame1,text='Account',bd=2,width=16,font=('arial', 12, 'bold'), relief="groove", fg="#303F9F",bg="#B2DFDB").pack(side=LEFT)
                Label(frame1,text='Username',bd=2,width=16,font=('arial', 12, 'bold'), relief="groove", fg="#303F9F",bg="#B2DFDB").pack(side=LEFT)
                Label(frame1,text='Password',bd=2,width=16,font=('arial', 12, 'bold'), relief="groove", fg="#303F9F",bg="#B2DFDB").pack(side=LEFT)
                yInc=15
                
                for i in (data):
                    f=Frame(root,background='#009688')
                    f.place(x=wd-70,y=ht+yInc)
                    userID, account,username,password=i
                    print(userID,account,username,password)
                    Label(f,text=userID,bd=1,width=20,font=('arial', 10 ), relief="groove", fg="#303F9F",bg="#FFFFFF").pack(side=LEFT)
                    Label(f,text=account,bd=1,width=20,font=('arial', 10 ), relief="groove", fg="#303F9F",bg="#FFFFFF").pack(side=LEFT)
                    Label(f,text=username,bd=1,width=20,font=('arial', 10 ), relief="groove", fg="#303F9F",bg="#FFFFFF").pack(side=LEFT)
                    Label(f,text=password,bd=1,width=20,font=('arial', 10), relief="groove", fg="#303F9F",bg="#FFFFFF").pack(side=LEFT)   
                    yInc+=20   
        else:
            print("pelase enter the correct password")
            signin(root)

def signin(root):

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # clearing previous widgets
    widget_list = main.all_children(root)
    for item in widget_list:
        item.destroy()

    #print("login button clicked")
    
    root.title("Login Page")
    
    username=StringVar(root)
    password=StringVar(root)
    
    
    frame1=Frame(root)
    frame1.config(background='#009688')
    frame1.place(x=ws/3.5,y=hs/4)   
    l1=Label(frame1,text='Username',font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39")
    e1=Entry(frame1,textvariable=username)
    l1.config(height=2,width=20)
    e1.config(font=('arial', 14),width=20)
    l1.pack(side=LEFT)
    e1.pack(side=LEFT,padx=10)
    
    frame2 = Frame(root)
    frame2.config(background='#009688')
    frame2.place(x=ws/3.5,y=hs/4+50) 
    l2=Label(frame2,text='Password',font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39")
    e2=Entry(frame2,textvariable=password,show='*')
    l2.config(height=2,width=20)
    e2.config(font=('ariel',14),width=20)
    l2.pack(side=LEFT)   
    e2.pack(side=LEFT,padx=10)

    frame3 = Frame(root, background='#009688', padx=5, pady=5)
    frame3.place(x=ws/4,y=hs/4+100)
    b1=Button(frame3,text='Log In', height="1",width="20", bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: credCheckMasterAccount(root,username.get(),password.get()))
    b2=Button(frame3,text='Forget Password', height="1",width="20", bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda:   forgetPassword.forgetPasswordUI(root))
    b1.pack(side=LEFT,padx=10)
    b2.pack(side=LEFT,padx=10)