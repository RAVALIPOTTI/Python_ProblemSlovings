name = input("Enter name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Total characters excluding spaces:", len(name.replace(" ", "")))
if len(name.replace(" ", "")) > 10:
    print("Length exceeds 10")
else:
    print("Length does not exceed 10")