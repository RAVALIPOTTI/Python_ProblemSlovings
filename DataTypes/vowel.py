a=input("enter the string:")
a=a.lower()
count=0
for char in a:
    if char in "aeiou":
        count=count+1
print("total vowels:",count)