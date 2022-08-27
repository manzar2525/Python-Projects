from tkinter import  *
from tkinter import font
import time
import datetime
import pytz

def quit(*agrs):
    root.destroy()



def clock_time():

    time=datetime.datetime.now()

    tz = pytz.timezone('Asia/Kolkata')
    i = time.astimezone(tz).strftime("%H:%M:%S")
    indianTimeTxt.set(i)

    date = (time.strftime("%d-%m-%Y"))
    dateTxt.set(date)

    tz = pytz.timezone('Europe/London')
    l = time.astimezone(tz).strftime("%H:%M:%S")
    londonTimeTxt.set(l)

    tz = pytz.timezone('US/Eastern')
    n = time.astimezone(tz).strftime("%H:%M:%S")
    newYorkTimeTxt.set(n)

    tz = pytz.timezone('Asia/Tokyo')
    t = time.astimezone(tz).strftime("%H:%M:%S")
    tokyoTimeTxt.set(t)

    root.after(1000,clock_time)


root=Tk()
root.bind("x",quit)
root.title("Digital Clock")
root.resizable(False,False)
w=300
h=500

# get screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.after(1000,clock_time)

fnt=font.Font(family='Helvetica',size=40,weight='bold')
fnt2=font.Font(family='Algerian',size=20)
fnt3=font.Font(family='Helvetica',size=30,weight='bold')

dateTxt=StringVar()
indianTimeTxt=StringVar()
londonTimeTxt=StringVar()
newYorkTimeTxt=StringVar()
tokyoTimeTxt=StringVar()


dateLabel=Label(root,textvariable=dateTxt,font=fnt3,foreground='#669900',background='orange')
label1=Label(root,text="Date",font=fnt2,foreground='#669900',background='white')
label2=Label(root,text="India",font=fnt2,foreground='#669900',background='white')
label3=Label(root,text="London",font=fnt2,foreground='#669900',background='white')
label4=Label(root,text="New York",font=fnt2,foreground='#669900',background='white')
label5=Label(root,text="Tokyo",font=fnt2,foreground='#669900',background='white')
indianTimeLabel=Label(root,textvariable=(indianTimeTxt),font=fnt,foreground='#669900',background='orange')
newYorkTimeLabel=Label(root,textvariable=(newYorkTimeTxt),font=fnt,foreground='#669900',background='orange')
tokyoTimeLabel=Label(root,textvariable=(tokyoTimeTxt),font=fnt,foreground='#669900',background='orange')
londonTimeLabel=Label(root,textvariable=(londonTimeTxt),font=fnt,foreground='#669900',background='orange')
"""
dateLabel.grid(row=0,column=0)
indianTimeLabel.grid(row=0,column=1)
newYorkTimeLabel.grid(row=1,column=1)
tokyoTimeLabel.grid(row=2,column=0)
londonTimeLabel.grid(row=2,column=1)
"""
label1.pack(side=TOP,fill=X)
dateLabel.pack(side=TOP,fill=X)
label2.pack(side=TOP,fill=X)
indianTimeLabel.pack(side=TOP,fill=X)
label3.pack(side=TOP,fill=X)
londonTimeLabel.pack(side=TOP,fill=X)
label4.pack(side=TOP,fill=X)
newYorkTimeLabel.pack(side=TOP,fill=X)
label5.pack(side=TOP,fill=X)
tokyoTimeLabel.pack(side=TOP,fill=X)

root.update()
root.mainloop()