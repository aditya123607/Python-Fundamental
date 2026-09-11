a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
if a > b and a > c:
    print ("the largest number is",a)
elif b > a and b >c:
    print("the largest number is",b)
else:
    print("the largest number is",c)
    