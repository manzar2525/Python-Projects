sum=0
def sumOfDigits(num):
    global sum
    reminder=(num%10)
    sum= sum + reminder
    if num>0:
        sumOfDigits(num=num//10)
    return sum

number=int(input("enter a number whose sum of digit is needed:  "))
print(sumOfDigits(number))
        
        

