a=input("enter a single character:")
if a.isupper():
    print(a,"is a upper letter")
elif a.islower():
    print(a,"is a lower letter ")
elif a.isdigit():
    print(a,"is a digit")
else:
    print(a,"is a special character")