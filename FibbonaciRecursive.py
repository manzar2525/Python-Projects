
def fibbonaci(number):

    if number<0:
        print("incorecct number")

    elif number == 0:
        return 0

    elif number==1 or number==2:
        return 1

    else:
        return fibbonaci(number-1) + fibbonaci(number-2)

number=int(input("Please enter how many number u want in the series:  "))
for i in range(number):
    print(fibbonaci(i))