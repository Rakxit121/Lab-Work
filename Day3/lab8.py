# Given a n-digit number. Find the sum of its digits.
number = int(input("enter a number"))
sum_of_digit = 0
for digit in str(number):
    sum_of_digit += int(digit)
print(sum_of_digit)
