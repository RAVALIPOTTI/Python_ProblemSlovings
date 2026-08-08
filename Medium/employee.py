name = input("Enter employee name: ")
salary = float(input("Enter salary: "))

if salary >= 50000:
    bonus = salary * 0.1
elif salary >= 30000:
    bonus = salary * 0.07
else:
    bonus = salary * 0.05

print("Employee:", name.upper())
print("Bonus:", bonus)