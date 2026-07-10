number1=input("Enter first number: ")
number2=input("Enter second number: ")
if number1>number2:
    print(number1,"is greater than",number2)
elif number2>number1:
    print(number2,"is greater than",number1)
else:
    print("Both numbers are equal")
vize=int(input("Enter your midterm score: "))
vize2=int(input("Enter your second midterm score: "))
final=int(input("Enter your final score: "))
result = (((vize+vize2) / 2)*0.6) + (final*0.4)
if result>=50:
    print("You passed the course with a score of",result)
else:
    print("You failed the course.")
number3=int(input("Enter number: "))
if number3%2==0:
    print(number3,"is an even number.")
else:
    print(number3,"is an odd number.")
email=input("Enter your email address: ")
emailt="abcd@gmail.com"
password=input("Enter your password: ")
passwordt="1234"
if email==emailt and password==passwordt:
    print("Login successful.")
else:
    print("Login failed. Please check your email and password.")
number4=int(input("Enter a number: "))
if number4>0:
    print(number4,"is a positive number.")
elif number4<0:
    print(number4,"is a negative number.")
else:
    print(number4,"is zero.")