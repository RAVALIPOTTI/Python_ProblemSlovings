price = float(input("Enter product price: "))

if price >= 1000:
    discount = 0.2
elif price >= 500:
    discount = 0.1
else:
    discount = 0

final_price = price - (price * discount)
print("Final Price:", final_price)