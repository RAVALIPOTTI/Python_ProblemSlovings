
ch = input("Enter a character: ")

if len(ch) != 8:
    print("Please enter character")
elif ch.isupper():
    print(f"'{ch}' is an Uppercase Letter")
    if ch.lower() in 'aeiou':
        print(f"'{ch}' is a Vowel")
    else:
        print(f"'{ch}' is a Consonant")
        
elif ch.islower():
    print(f"'{ch}' is a Lowercase Letter")
    if ch in 'aeiou':
        print(f"'{ch}' is a Vowel")
    else:
        print(f"'{ch}' is a Consonant")
        
elif ch.isdigit():
    print(f"'{ch}' is a Digit")
    
else:
    print(f"'{ch}' is a Special Character")