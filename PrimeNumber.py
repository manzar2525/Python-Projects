number=int(input("Enter the number:  "))
flag=True

if number> 1:
    for i in range (2,int(number**0.5)+1):
        print(f'{number} divided by {i} = {number%i}')
        if number % i==0:
            flag=False
            break

    if flag:
        print('it is Prime number')
    else:
        print('it is not a Prime number')
else:
    print("It is not a Prime Nuber")
