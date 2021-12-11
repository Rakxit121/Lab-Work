# Given three integers, print the smallest one. (Three integers should be user input)
a = int(input("enter one int"))
b = int(input("enter two int"))
c = int(input("enter three int"))
if a < b and a < c:
    print("a is small")
elif b < a and b < c:
    print("b is small")
else:
    print("c is small")
