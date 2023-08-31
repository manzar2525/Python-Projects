import random
from tkinter import *
import main


def generatePasswordUI(root,pLength):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    widget_list = main.all_children(root)
    for item in widget_list:
        item.destroy()

    #print("Generate Password button clicked")
    
    root.title("Password Generator")
    
    passLength=StringVar(root)
       
    frame1=Frame(root)
    frame1.config(background='#009688')
    frame1.place(x=ws/3.5,y=hs/4)   
    l1=Label(frame1,text='Password Length',font=('arial', 10, 'bold'), relief="groove", fg="white",bg="#FFDE03")
    e1=Entry(frame1,textvariable=passLength)
    l1.config(height=2,width=20)
    e1.config(font=('arial', 14),width=20)
    l1.pack(side=LEFT)
    e1.pack(side=LEFT,padx=10)

    frame3 = Frame(root, background='#009688', padx=5, pady=5)
    frame3.place(x=ws/4,y=hs/4+100)
    b1=Button(frame3,text='Generate', height="1",width="20", bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: generatePassword(passLength.get(),root))
    b2=Button(frame3,text='Home', height="1",width="20", bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: login(root))
    b1.pack(side=LEFT,padx=10)
    b2.pack(side=LEFT,padx=10)

def generatePassword(pLength,root):
    lowerAlpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperAlpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers=['0','1','2','3','4','5','6','7','8','9',]
    specialCharacter=[ '!','#','$','%','&','(',')','*','+','-','/',':',';','<','=','>','?','@' ,'_']
    indices=[0, 1 ,2 ,3]
    password=""

    for j in range(0,int(pLength)-4):
        indices.append(random.randint(0,3))

    random.shuffle(indices)

    for j in indices:
        if(j==0):
            index=random.randint(0,25)
            password+=lowerAlpha[index]
        elif(j==1):
            index = random.randint(0,25)
            password += upperAlpha[index]
        elif(j==2):
            index = random.randint(0,8)
            password += numbers[index]
        else:
            index = random.randint(0,18)
            password += specialCharacter[index]
        tmsg="Password Generated:\t"+password
    
    print(password)
    frame11=Frame(root)
    frame11.config(background='#009688')
    frame11.place(x=ws/3.5,y=hs/4-50)
    l1=Label(frame11,text=tmsg,bd=2,width=36,font=('arial', 12, 'bold'), relief="groove", fg="#303F9F",bg="#B2DFDB").pack(side=LEFT)