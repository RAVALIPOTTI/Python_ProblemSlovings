
username = input("Enter username: ")
age = int(input("Enter age: "))

# Check 1: length must be 6
if len(username) != 6:
    print("Registration Not Allowed: Username must be exactly 6 characters")

# Check 2: only letters and digits
elif not username.isalnum():
    print("Registration Not Allowed: Username must contain only letters and digits")

# Check 3: age >= 18
elif age < 18:
    print("Registration Not Allowed: Age must be at least 18")

else:
    print("Registration Allowed")