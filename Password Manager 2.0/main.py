from tkinter import *
import db
import userInterface
import login
import generatpass
import signup

def screenwidth(root):
    return root.winfo_screenwidth()

def screenheight(root):
    return root.winfo_screenheight()

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

# to close the program
def exitFunc(root):
    root.destroy()


# Drive code - Creating the Main GUI window 
root= Tk()
root.title("Home Page")
#root.resizable(False,False)
root.config(background='#009688')
root.geometry("%dx%d" % (screenwidth(root),screenheight(root)))

frame1=Frame(root,width=100,height=100,background='#B2DFDB')

frame1.place(x=screenwidth(root)//3,y=screenwidth(root)//6)
print(screenwidth(root),screenheight(root))

logInButton=Button(frame1, text='Log In', bd=6, font=('arial', 12, 'bold'), relief="groove", fg="#FFFFFF",bg="#1DE9B6",command= lambda: login.signin(root))
signUpButton=Button(frame1,text='Create a new Account', bd=6, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: signup.signUp(root))
generatePasswordButton=Button(frame1,text='Generate Password', bd=6, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="#1DE9B6",command= lambda: generatpass.generatePasswordUI(root))

logInButton.config(height=2,width=20)
logInButton.pack(side=TOP,padx=2,pady=2)
signUpButton.pack(side=TOP,padx=2,pady=2)
signUpButton.config(height=2,width=20)
generatePasswordButton.config(height=2,width=20)
generatePasswordButton.pack(side=TOP,padx=2,pady=2)
root.mainloop()
