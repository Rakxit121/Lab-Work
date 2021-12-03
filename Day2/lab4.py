hour_first = int(input("Enter first hour:"))
minute_first = int(input("Enter first minute:"))

hour_second = int(input("Enter second hour:"))
minute_second = int(input("Enter second minute:"))

diff_hour = 0
diff_min = 0
if hour_first > hour_second:
    if minute_first > minute_second:
        diff_min = minute_first - minute_second
        diff_hour = hour_first - hour_second
    else:
        hour_first = hour_first - 1
        minute_first = minute_first + 60
        diff_min = minute_first - minute_second
        diff_hour = hour_first - hour_second

print(" The difference is ", diff_hour, " hour and", diff_min, " minute")
