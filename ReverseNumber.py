
from turtle import clear
from unicodedata import name


def reverseNumber(num):
    revNumber=0
    while(num>0):
        revNumber=revNumber*10+num%10
        num=num//10
    return revNumber

def main():
    number=int(input("enter a number whose reverse is required:\t"))
    print(reverseNumber(number))

if __name__=="__main__":
    main()
    