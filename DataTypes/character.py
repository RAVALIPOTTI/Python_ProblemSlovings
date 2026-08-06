a = input("enter a string ")

if len(a) > 0:
    first_char = a[0]
    last_char = a[-1]
    print("first character:", first_char) 
    print("last character:", last_char) 
else:
    print("please enter a string")