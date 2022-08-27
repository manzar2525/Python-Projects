import random

#==================== Function to generate password======
def generatePassword(pLength):
    indices=[0, 1 ,2 ,3]
    password=" "

    for j in range(0,pLength-4):
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

    return password

#=======================Main Program=================================
lowerAlpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperAlpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9',]
specialCharacter=[ '!','#','$','%','&','(',')','*','+','-','/',':',';','<','=','>','?','@' ,'_']
passwords=[]



print("1. Password length must be greater than 4")
print("2. password length greater less than 8 is considered weak")
print("2. Enter both the values in the same line")
print("Please enter the length and number of password you want to generate")

passLength,passNumber=input().split()
passLength=int(passLength)
passNumber=int(passNumber)

if(passLength<4):
    print("Error: Password length must be greater than four")
for i in range(passNumber):
    passwords.append(generatePassword(passLength))

for i in passwords:
    print(i)

