second = int(input("Enter the seconds: "))
minute = second / 60
sec_rem = second % 60
hour = minute / 60
min_rem = minute % 60
day = hour / 24
hour_rem = hour % 24
print(second, " is ", int(day), " day", int(min_rem), " minute and ", int(sec_rem), " second")

