secert=8
guess=0
while guess !=secert:
    guess=int(input("guess the number:"))
    if guess>secert:
        print("Too high")
    elif guess<secert:
        print("Too low")
    else:
        print("correct guess!")