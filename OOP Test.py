name=input("Enter Name:  ")
number=int(input("Enter Number:  "))
year=int(input("Enter Age:  "))
class Person:
    def __init__(self,name,year,number):
        self.name=name
        self.year=year
        self.number=number
test1=Person(name,year,number)
print(f"Name:{test1.name} Number:{test1.number} Age:{test1.year}")
