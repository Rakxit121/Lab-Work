# reverse word


word = input("Enter a word to reverse : ")
print("Input word: ",word)

a = ""
for ch in word:
    a = word + a

print()
print("Reversed word: ",a)

