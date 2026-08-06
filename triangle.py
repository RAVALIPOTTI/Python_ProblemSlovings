
a= float(input("enter the side 1:"))
b=float(input("enter the side 2:"))
c=float(input("enter the side 3:"))
if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print("equilateral triangle")
    elif a==b or b==c or c==a:
        print("isoscelar triangle")
    else:
        print("scalene triangle")
else:
    print("not a vaild triangle")
