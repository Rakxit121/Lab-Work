time_passed_min = int(input("Enter the minute passed: "))
time_passed_hr = 0
rem_min = 0
if time_passed_min > 60:
    time_passed_hr = time_passed_min / 60
    rem_min = time_passed_min % 60
if time_passed_hr > 24:
    time_passed_hr = time_passed_hr - 24
print("The time passed since midnight is ", int(time_passed_hr), ":", int(rem_min))

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
else:
    if minute_second > minute_first:
        diff_min = minute_second - minute_first
        diff_hour = hour_second - hour_first
    else:
        hour_second = hour_second - 1
        minute_second = minute_second + 60
        diff_min = minute_second - minute_first
        diff_hour = hour_second - hour_first
print(" The difference is ", diff_hour, " hour and", diff_min, " minute")
