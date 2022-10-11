from re import A


num1=int(input("enter the 1st number:  "))
num2=int(input("enter the 2nd number:  "))
num3=int(input("enter the 3rd number:  "))

largest=0

if num1 >= num2 and num1>=num3:
    largest=num1

elif num2> num3:
    largest=num2

else:
    largest=num3

print(largest)