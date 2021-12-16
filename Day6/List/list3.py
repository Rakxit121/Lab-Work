num = [1, 4, 3, 5, 7, 8, 9, 11, 44, 14, 15, 25]
largest = num[0]
for i in range(1, len(num)):
    if num[i] > largest:
        largest = num[i]
print('The list elements are: ', num)
print('The largest element in list are: ', largest)

# Or

print(max(num))
