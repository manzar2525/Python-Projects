from tkinter import *
import main
import db

def home(root,uname):
    #refreshing the window to load new UI
    widget_list = main.all_children(root)
    for item in widget_list:
        item.destroy()

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    wd=ws/3.5
    ht=hs/5

    frame3 = Frame(root,background='#009688')
    frame3.place(x=wd-80,y=ht-100)
    Button(frame3,text='Add New Credentials to Vault', bd=5, width=25, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: saveCredentialsUI(root,uname)).pack(padx=10,side=LEFT)
    Button(frame3,text='Show all Credentials', bd=5,width=25, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: home(root,uname)).pack(padx=10,side=LEFT)
    Button(frame3,text='Exit', bd=5,width=25, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: main.exitFunc(root)).pack(padx=10,side=LEFT)

   
    data=db.fetchfromStore(uname)
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


def saveCredentials(root,userID, account,userName,password):
    wd=main.screenwidth(root)/3.5
    ht=main.screenheight(root)/5

    if len(account)==0 or len(userName)==0 or len(password)==0 :
        print("Please enter all the values")
        frame5=Frame(root)
        frame5.config(background='#009688')
        frame5.place(x=wd+50,y=ht+150)     
        Label(frame5,text='Please enter all the values',height=2,width=30,font=('arial', 15, 'bold'), relief="groove", fg="red",bg="#CDDC39").pack(side=LEFT)        
    else:
        print("non empty")
        db.insertIntoStore(userID,account,userName,password)
        print("credentials saved successfully")
        home(root,userID)
    #print("testing")



def saveCredentialsUI(root,userID):
    #print("testing2")
    # clearing previous widgets
    widget_list = main.all_children(root)
    for item in widget_list:
        item.destroy()

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    root.title("Store New Credentials to the Vault")
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    wd=ws/3.5
    ht=hs/5
    
    account=StringVar(root)
    userName=StringVar(root)
    password=StringVar(root)

    frame1=Frame(root)
    frame1.config(background='#009688')
    frame1.place(x=wd+50,y=ht)   
    Label(frame1,text='Account',height=1,width=20,font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39").pack(side=LEFT)
    Entry(frame1,textvariable=account).pack(side=LEFT,padx=10)

    frame2=Frame(root)
    frame2.config(background='#009688')
    frame2.place(x=wd+50,y=ht+25) 
    Label(frame2,text='userName',height=1,width=20,font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39").pack(side=LEFT)
    Entry(frame2,textvariable=userName).pack(side=LEFT,padx=10)

    frame3=Frame(root)
    frame3.config(background='#009688')
    frame3.place(x=wd+50,y=ht+50)     
    Label(frame3,text='Password',height=1,width=20,font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#CDDC39").pack(side=LEFT)
    Entry(frame3,textvariable=password,show='*').pack(side=LEFT,padx=10)

            
    frame4 = Frame(root, padx=5, pady=5)
    frame4.config(background='#009688')
    frame4.place(x=wd+55,y=ht+100)
    Button(frame4,text='Submit', height="1",width="10", bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: saveCredentials(root,userID,account.get(),userName.get(),password.get())).pack(side=LEFT,padx=10)
    Button(frame4,text='Cancle', height="1",width="10", bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: home(root,userID)).pack(side=LEFT,padx=10)
