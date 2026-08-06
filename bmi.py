
height=float(input("enter the height:"))
weight=float(input("enter the weight:"))
bmi=weight/(height**2)
print("BMI:",round(bmi,2))
if bmi<18.5:
    print("category:under weight")
elif 18.5<=bmi<24.9:
    print("category:normal:")
elif 25<=bmi<29.9:
    print("category:overweight:")
else:
    print("category:obese")

