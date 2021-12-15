enter = input("enter conversion celsius (c) or fahrenheit (f)")
temp = int(input("enter the temperature in fahrenheit"))

if enter == "c":
    temp = int(input("enter the temperature in fahrenheit"))
    temp_cel = (5 / 9) * (temp - 32)
    print("The temperature in celsius is : ", temp_cel)
elif enter == "f":
    temp = int(input("enter the temperature in fahrenheit"))
    temp_fehr = (temp * (9 / 5)) + 32
    print("The temperature in fahrenheit is : ", temp_fehr)
