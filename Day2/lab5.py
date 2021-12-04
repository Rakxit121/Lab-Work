num_stu_a = int(input("Enter the number of students in class a: "))
num_stu_b = int(input("Enter the number of students in class b: "))
num_stu_c = int(input("Enter the number of students in class c: "))
a = 0
b = 0
c = 0

div_a = num_stu_a // 2
div_b = num_stu_b // 2
div_c = num_stu_c // 2

if div_a % 2 != 0 or num_stu_b % 2 != 0 or num_stu_c % 2 != 0:
    a = div_a + 1
    b = div_b + 1
    c = div_c + 1
else:
    a = div_a
    b = div_b
    c = div_c
print()
print("The minimum number of desks needed in class a are: ", int(a))
print("The minimum number of desks needed in class b are: ", int(b))
print("The minimum number of desks needed in class b are: ", int(c))
