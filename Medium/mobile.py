num = input("Enter mobile number: ")

if len(num) == 10 and num.isdigit() and num[0] in '6789':
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
