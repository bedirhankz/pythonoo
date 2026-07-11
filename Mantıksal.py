Number=int(input("Enter a number: "))
if Number>=0 and Number<=100:
    print("The number is between 0 and 100.")
else:
    print("The number is not between 0 and 100.")
Number1=int(input("Enter a number: "))
if Number1>0 and Number1%2==0:
    print("The number is positive and even.")
else:
    print("The number is not positive or even.")
email=input("Enter your email: ")
password=input("Enter your password: ")
if email=="abc@gmail.com" and password=="123":
    print("Login successful.")
else:
    print("Login failed Check your email and password.")
number2=int(input("Enter a number: "))
number3=int(input("Enter another number: "))
number4=int(input("Enter one more number: "))
check={number2, number3, number4}
check2=sorted(check)
print(check2[0],"<",check2[1],"<",check2[2])
midterm=int(input("Enter your midterm score: "))
midterm2=int(input("Enter your midterm score: "))
final=int(input("Enter your final score: "))
result=(midterm+midterm2*0.6/2)+(final*0.4)
if result>=50 and final>=50:
    print("You passed the course.")
elif final>=70:
    print("You passed the course with a high final score.")
else:
    print("You failed the course.")
your_weight=float(input("Enter your weight in kg: "))
your_height=float(input("Enter your height in cm: "))
bmi= your_weight / (your_height*your_height)
if bmi<=18.4:
    print("You are underweight.")
elif bmi>=18.5 and bmi<=24.9:
    print("You have a normal weight.")
elif bmi>=25.0 and bmi<=29.9:
    print("You are overweight.")
else:
    print("You are obese.")