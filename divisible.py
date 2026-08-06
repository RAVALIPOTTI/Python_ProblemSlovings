
num=int(input("enter the number:"))
if num%3==0 and num%5==0:
    print("divisible by 3 and 5")
elif num%3==0:
    print("divisible by 3")
elif num%5==0:
    print(" divisible by 5")
else:
    print("not divisible by 3 and 5")