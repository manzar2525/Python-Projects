'''
def numberOfDigit(number):
    digitCount=0
    while number>0:
        digitCount=digitCount+1
        number = number // 10
    #print(f'number of digit={digitCount}')
    return digitCount
'''
number=int(input("Please enter the number:\t"))
number1=number

length=len(str(number1))
#length=numberOfDigit(number)
sum=0

while number1 !=0:
    r=number1%10
    sum=sum+(r**length)
    number1=number1//10

if number==sum:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")