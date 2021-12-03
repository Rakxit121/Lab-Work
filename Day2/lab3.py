time_passed_min = int(input("Enter the minute passed: "))
time_passed_hr = 0
rem_min = 0
if time_passed_min > 60:
    time_passed_hr = time_passed_min / 60
    rem_min = time_passed_min % 60
if time_passed_hr > 24:
    time_passed_hr = time_passed_hr - 24
print("The time passed since midnight is ", int(time_passed_hr), ":", int(rem_min))
