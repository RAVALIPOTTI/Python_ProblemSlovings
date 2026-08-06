
balance=float(input("enter the balance:"))
amount=float(input("enter the amount:"))
if amount%100!=0:
    print("error:amount should be multiple of 100")
elif amount>balance:
    print("error:insuffient balance")
else:
    balance=balance-amount
    print("with drawal successful")
    print("remaining balance:",balance)