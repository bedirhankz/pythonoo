x,y,z=2,5,107
numbers=1,5,7,10,6
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
g=a*b
u=x+y+z
h=g-u
print("The product of the two numbers is:", abs(h))
bolum=y//x
print("The division of y by x is:", bolum)
print("Modulus of y by x is:",u%3)
print("exponent of x to the power of y is:",y**x)
x,*y,z=numbers
print("The values of x, y, z are:", x, y, z)
print(sum(y))
print(z*z*z)