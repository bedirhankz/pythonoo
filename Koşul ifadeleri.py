name=input("Enter your name: ")
age=int(input("Enter your age: "))
print("(1)Primary school")
print("(2)Secondary school")
print("(3)High school")
print("(4)University")
education=int(input("Enter your education level: "))
if education==3 or education==4 and age>=18:
    print("You can get a driving license.")
else:
    print("You are not eligible for a driving license.")
exam_score=int(input("Enter your exam score: "))
exam_score2=int(input("Enter your second exam score: "))
oral_score=int(input("Enter your oral score: "))
average_score=(exam_score+exam_score2+oral_score)/3
if 0<=average_score<=24:
    print(average_score,"Result:0")
elif 25<=average_score<=44:
    print(average_score,"Result:1")
elif 45<=average_score<=54:
    print(average_score,"Result:2")
elif 55<=average_score<=69:
    print(average_score,"Result:3")
elif 70<=average_score<=84:
    print(average_score,"Result:4")
elif 85<=average_score<=100:
    print(average_score,"Result:5")
else:
    print("Invalid score entered.")
traffic_time=int(input("How many days has your vehicle been on the road?: "))
if traffic_time<365:
    print("1. Maintenance time")
elif 365<=traffic_time<730:
    print("2. Maintenance time")
elif 730<=traffic_time<1095:
    print("3. Maintenance time")
else:
    print("You can not get a Maintenance time.")
