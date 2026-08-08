pre_user = "admin"
pre_pass = "1234"

user = input("Enter username: ")
password = input("Enter password: ")

if user!= pre_user:
    print("Invalid Username")
elif password!= pre_pass:
    print("Invalid Password")
else:
    print("Login Successful")