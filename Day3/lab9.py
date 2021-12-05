u_name = "random"
passwd = "pass"
j = 1

for i in range(1):
    e_u_name = input("Enter the username: ")
    e_passwd = input("Enter the password: ")
    j = j + 1
    if e_u_name == u_name and e_passwd == passwd:
        print(" Logged in Successfully ")
        break
else:

    print("Error !!! Try again !!!")
    e_u_name = input("Username: ")
    e_passwd = input("Password: ")
    j = j + 1
    for i in range(2):
        if e_u_name == u_name or e_passwd == passwd:
            print(" Logged in Successfully ")
            break
        elif j > 3:
            print("You have tried more than 3 times and cannot try again")
            break
        else:
            print("Error !!! Try again !!!")
            e_u_name = input("Username: ")
            e_passwd = input("Password: ")
            j = j + 1
            continue
