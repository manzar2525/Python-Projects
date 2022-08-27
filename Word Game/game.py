from nltk.corpus import wordnet


def firstPlay():
    print("It's yout turn: "+firstPlayer)
    w1=input()
    f1=True
    if(len(wordnet.synsets(w1))>0):
        if(len(player1)==0):
            player1.append(w1)
        else:
            if (len(player2) > 0):
                ch1 = w1[0]
                ch2 = player2[-1][-1]
                if (ch1 != ch2):
                    f1=False
                else:
                    if(w1 in player1 or w1 in player2):
                        print("You entered a duplicate value")
                        f1 = False
                    else:
                        player1.append(w1)
                        f1 = True
    else:
        print("You entered a wrong word")
        f1=False
    return f1

def secondPlay():
    print("It's yout turn: " + secondPlayer)
    w2=input()
    f2=True
    if(wordnet.synsets(w2)):
        if (len(player1) > 0):
            ch1 = player1[-1][-1]
            ch2 = w2[0]
            if (ch1 != ch2):
                f2=False
            else:
                if(w2 in player2 or w2 in player1):
                    print("You have entered a duplicate value")
                    f2=False
                else:
                    player2.append(w2)
                    f2=True
    else:
        print("You entered a wrong word")
        f2=False

    return f2


#===================Main method===================
print("**********GAME STARTED**********")
player1=[]
player2=[]
print("enter the name of the first player")
firstPlayer=input()
print("enter the name of the second player")
secondPlayer=input()

flag1=True
flag2=True
while(flag1==True & flag2==True):
    flag1=firstPlay()
    if(flag1==False):
        break
    flag2=secondPlay()



score1=len(player1)*10
score2=len(player2)*10
if(score1>score2):
    print(firstPlayer+" you are the winner",score1)
else:
    print(secondPlayer + " you are the winner",score2)
print("words enter by "+firstPlayer)
print(player1)
print("words enter by "+secondPlayer)
print(player2)
