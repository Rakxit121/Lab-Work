num = [1, 4, 3, 5, 7, 8, 9, 11, 44, 14, 15, 25, 0]
smallest = num[0]
for i in range(1, len(num)):
    if num[i] < smallest:
        smallest = num[i]
print('The list elements are: ', num)
print('The smallest element in list are: ', smallest)

# Or

print(min(num))
