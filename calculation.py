
a=6
b=7
print("\nchoice the opetaor")
print("Addition: +")
print("substraction: -")
print("multiplication: *")
print("division: /")
choice = input("Enter your choice +, -, *, /, % : ")
sum=a+b
sub=a-b
mul=a*b
div=a/b
if choice=="+":
    print("result:",sum)
elif choice=="-":
    print("result:",sub)
elif choice=="*":
    print("result:",mul)
else: 
    print("result:",div)