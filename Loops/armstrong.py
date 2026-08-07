n=int(input("enter a number:"))
original=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
    if sum==original:
        print(original,"is an armstrong number")
    else:
        print(original,"is not an armstrong number")