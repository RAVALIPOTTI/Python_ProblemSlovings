uid = input("Enter User ID: ")

if len(uid) >= 6 and uid[0].isalpha() and uid[-1].isdigit() :
    print("Valid User ID")
else:
    print("Invalid User ID")