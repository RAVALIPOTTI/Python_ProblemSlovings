s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 == s2:
    print("Exactly Equal")
elif s1.lower() == s2.lower():
    print("Equal ignoring case")
else:
    print("Different")