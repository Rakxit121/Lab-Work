u_name="random"
passwd="pass"


for i= 1  3:
    e_u_name = input("Enter the username: ")
    e_passwd = input("Enter the password: ")
    if e_u_name==u_name and e_passwd== passwd:
        print(" Logged in Successfully ")
        break
else:
    print("Try again!!")
    e_u_name=input("")
    e_passwd=input("")
    continue


