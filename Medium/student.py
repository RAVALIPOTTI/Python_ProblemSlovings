name=input("enter student name:")
marks=float(input("enter the marks"))
print("name:",name.upper())
if marks>=90:
    grade="A"
elif marks>=75:
    grade="B"
elif marks>=60:
    grade="C"
elif marks>40:
    grade="D"
else:
    grade="F"
print("grade:",grade)
if marks>=40:
    print("pass")
else:
    print("fail")