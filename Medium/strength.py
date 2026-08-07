pws=input("enter the password:")
ha_upper=has_lower=has_digit=False
for ch in pws:
    if ch.isupper():
        has_upper=True
    elif ch.islower():
        has_lower=True
    elif ch.isdigit():
        has_digit=True
if len(pws)>=8 and has_upper and has_lower and has_digit:
    print("Strong password")
else:
    print("weak password")