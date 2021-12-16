# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
num = [1500, 2701]

a = int(input("enter any number between 1500 to 2700: "))

b = 7

c = 5

for i in num:

    if a % b == 0 and a % c == 0:
        print("it is both divisible and multiply")

else:

    print("error")
