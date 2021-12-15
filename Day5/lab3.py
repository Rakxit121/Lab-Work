import random

a = random.randint(1, 9)
print("Guess the number game")
num = int(input("Enter the number from 1 to 9 : "))
if a == num:
    print("Well guessed!! , the number is :", num)
else:
    print("Sorry you guessed wrong!")
    while a != num:
        num = int(input("Please Enter the number from 1 to 9 :"))
        if a == num:
            print("Well guessed!! , the number is :", num)
            break
        else:
            continue
