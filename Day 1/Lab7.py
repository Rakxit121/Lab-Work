# 7) Add odd numbers of first 10 integer
ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for i in range(1, 10):
    if ten[i] % 2 != 0:
        total = total + ten[i]
print("The sum of odd number is: ", total)