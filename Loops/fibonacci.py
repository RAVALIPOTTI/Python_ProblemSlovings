n=int(input("enter the number:"))
a=1
b=2
count=0
while count <n:
    print(a,end="")
    c=a+b
    a=b
    b=c
    count=count+1
    