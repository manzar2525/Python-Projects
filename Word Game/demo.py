from tkinter import *

def displayResult(msg,lastWord):
    global winMsg
    global label3
    global resultFrame
    label3.config(text="")
    label3.pack()
    print(msg)

    scoreOne=len(playerOne)*10
    scoreTwo=len(playerTwo)*10
    if(scoreTwo>=scoreOne):
        winMsg+=nameTwo+" you are the winner\n"
    else:
        winMsg += nameOne + " you are the winner\n"
    winMsg+="Score==================\n"
    winMsg+=nameOne+" : "+str(scoreOne)+"\n"
    winMsg+=nameTwo+" : "+str(scoreTwo)

    label3.config(text=winMsg)
    label4 = Label(resultFrame, text=nameOne+str(playerOne), bg='#cc7a00', fg='black',font=('TimesNewRoman',10))
    label5 = Label(resultFrame, text=nameTwo+str(playerTwo), bg='#cc7a00', fg='black',font=('TimesNewRoman',10))

    print(winMsg)
    print(playerOne)
    print(playerTwo)


    label3.pack(side=TOP)
    label4.pack(side=TOP)
    label5.pack(side=TOP)

def playOne():

    global flag
    global nameOne
    global playerOne
    if(flag==True):
        s1 = textBoxOne.get(1.0, END)
        #print(type(st))
        nameOne=label1['text']
        if(nameOne=='Player 1'):
            label1.config(text='')
            label1.config(text=s1)
        else:
            s1=str(s1)
            s1 = s1.strip()
            #print(wordnet.synsets(s1))
            if (s1 in word_list):
                if (len(playerOne) == 0):
                    playerOne.append(s1)
                else:
                    if (len(playerTwo) > 0):
                        ch1 = s1[0]
                        ch2 = playerTwo[-1][-1]
                        if (ch1 != ch2):
                            displayResult("You enter an unmathing word",s1)
                        else:
                            if (s1 in playerOne or s1 in playerTwo):
                                displayResult("You entered a duplicate word",s1)
                            else:
                                playerOne.append(s1)
            else:
                displayResult("You tried to invent a new word",s1)
        textBoxOne.delete(1.0, END)
        flag=False
    else:
        pass

def playTwo():
    global flag
    global nameTwo
    global playerTwo
    if(flag==False):
        s2 = textBoxTwo.get(1.0, END)
        nameTwo = label2['text']
        if (nameTwo == 'Player 2'):
            label2.config(text='')
            label2.config(text=s2)
        else:
            ##################################
            s2 = str(s2)
            s2=s2.strip()
            if (s2 in word_list):
                if (len(playerOne) > 0):
                    ch1 = s2[0]
                    ch2 = playerOne[-1][-1]
                    if (ch1 != ch2):
                        displayResult("You entered an unmatching word",s2)
                    else:
                        if (s2 in playerOne or s2 in playerTwo):
                            displayResult("You entered a duplicate word",s2)
                        else:
                            playerTwo.append(s2)
            else:
                displayResult("You tried to invent a new word",s2)
        ############################
        textBoxTwo.delete(1.0,END)
        flag = True
    else:
        pass




def exitGame():
    r.destroy()




f=open("words_alpha.txt","r")
word_list=f.read()
flag=True
word=[]
playerOne=[]
playerTwo=[]
winMsg=""
nameOne=""
nameTwo=""
rule="1.\t Don't use the enter key  of the keybord.\n" \
     "2.\t After typing the word click on enter button.\n" \
     "3. \t First enter your name.\n" \
     "4. \t Once both entered the name game will start.\n"
#creating the GUI
r=Tk()
r.title("Word Game")
r.configure(background='silver')
w=800
h=600

# get screen width and height
ws = r.winfo_screenwidth()
hs = r.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
r.geometry('%dx%d+%d+%d' % (w, h, x, y))
r.resizable(False,False)

playerOneFrame=Frame(r,bg='#cc7a00')
playerTwoFrame=Frame(r,bg='#669900')
resultFrame=Frame(r,bg='#cc7a00')

playerOneFrame.pack(fill=BOTH,expand=1)
playerTwoFrame.pack(fill=BOTH,expand=1)
resultFrame.pack(side=BOTTOM,fill=BOTH,expand=1)

label1=Label(playerOneFrame,text='Player 1',bg='#cc7a00',fg='white',font=('Algerian',30))
label2=Label(playerTwoFrame,text='Player 2',fg='white',bg='#669900',font=('Algerian',30))
label3=Label(resultFrame,text=rule,anchor=CENTER,bg='#cc7a00',fg='white',width=50,font=('TimesNewRoman',15))

textBoxOne=Text(playerOneFrame,height=1,width=40)
textBoxOne.insert(1.0,"Enter your name")

textBoxTwo=Text(playerTwoFrame,height=1,width=40)
textBoxTwo.insert(1.0,"Enter your name")


b1=Button(playerOneFrame,text="enter",bg='#669900',width=15,bd=3,command=playOne)
b2=Button(playerTwoFrame,text="enter",bg='#cc7a00',width=15,bd=3,command=playTwo)
b3=Button(resultFrame,text="Stop",bg='white',command=exitGame)
#b1.bind('<Return>',playOne())


label1.pack()
label2.pack()
label3.pack(side=TOP)
b1.pack()
b2.pack()
b3.pack(side=BOTTOM)

textBoxOne.pack()
textBoxTwo.pack()

r.mainloop()