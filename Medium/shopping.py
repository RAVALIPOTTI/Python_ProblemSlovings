amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = 0.2
elif amount >= 2000:
    discount = 0.1
elif amount >= 1000:
    discount = 0.05
else:
    discount = 0

final_bill = amount - (amount * discount)
print("Discount:", amount * discount)
print("Final Bill:", final_bill)