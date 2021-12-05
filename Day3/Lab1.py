nat = [1, 2, 3, 4, 5]
a = 0
for j in range(1,6):
    if nat(j) == 1 or nat(j) == 2 or nat(j) == 3 or nat(j) == 4 or nat(j) == 5:
        a = a + 1

if a == 5:
    print("All the numbers fall in the first five natural numbers.")
    print(nat)
elif a == 0:
    print("None of the numbers fall in the first five natural numbers")
else:
    print("Not all of the numbers fall in the first five natural numbers")
