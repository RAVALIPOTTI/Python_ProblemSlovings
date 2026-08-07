email=input("enter the email")
if email.count('@')==1 and email.count('-')>=1:
    parts=email.split('@')
    if len(parts)==2 and'-' in parts[1]:
        print("vaild email")
    else:
        print("invaild email") 
else:
    print("invaild email")   