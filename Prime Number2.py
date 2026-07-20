import math
number=int(input("1. Number:  "))
number2=int(input("2. Number:  "))
def prime():
    for numbers in range(number,number2+1):
        if numbers<2:
            continue
        sqrt1=int(math.sqrt(numbers))+1
        prime1=True
        for sqrt2 in range(2,sqrt1):
            if numbers % sqrt2 == 0:
                prime1=False
                break
        if prime1 == True:
            print(f"\nPrime numbers between {number} and {number2}",{numbers})
prime()