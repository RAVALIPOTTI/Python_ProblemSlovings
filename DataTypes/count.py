a=input("enter string:")
upper=lower=digit=special=0
for char in a:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1
    elif chra.isdigit():
        digit+=1
    else:
        special+=1
print("uppercase:",upper)
print("lowercase:",lower)
print("digit:",digit)
print("special characters:",special)