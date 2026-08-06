
marks=float(input("enter the marks"))
if 90<=marks<=100:
    grade="A"
elif 75<=marks<=89:
    grade="B"
elif 60<=marks<=74:
    grade="C"
elif 35<=marks<=59:
    grade="D"
elif marks<35:
    grade="F"
else:
    grade="invaild marks"
print("Grade:",grade)