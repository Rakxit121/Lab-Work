# Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else
# print ‘COMMON YEAR’.
year = int(input("Enter a Year: "))
a = year % 4
b = year % 100
c = year % 400
if a == 0:
    if b == 0 and c != 0:
        print(f"{year} is a Common Year.")
    else:
        print(f"{year} is a Leap Year.")
else:
    print(f"{year} is a Common Year.")
