word = input("Enter word: ").lower()

vowels = 0
consonants = 0
for ch in word:
    if ch.isalpha():
        if ch in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")