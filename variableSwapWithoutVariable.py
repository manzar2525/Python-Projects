
number1=int(input("Please enter the 1st number:  "))
number2=int(input("Please enter the 2nd number:  "))

print(f'before swap number1={number1} and number2={number2}')
number1=number1 - number2
number2=number1 + number2
number1=number2 - number1

print(f'after swap number1={number1} and number2={number2}')