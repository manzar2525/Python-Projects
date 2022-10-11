from ReverseNumber import reverseNumber

#def main():
number=int(input("Please enter the number to check Palindrom or Not:  "))

revNumber=reverseNumber(number)

if revNumber==number:
    print("It is a palindrom Number")
else:
    print("It is not a palindrom Number")
'''
if __name__=="__main__":
    main()
''' 