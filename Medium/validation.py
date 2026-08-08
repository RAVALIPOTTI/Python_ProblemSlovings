a=input("enter a character:")
b=int(input("enter the number:"))
if len(a)>=6 and " " not in a:
    print("Registration allow")
else:
    print("not allow")
if b<18:
    print("Registration allow")
else:
    print("not allow")    

