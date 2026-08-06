sentence = input("enter a string: ")  # ← step 1: save input in 'sentence'
old = input("enter word to replace: ")
new = input("enter new word: ")

update = sentence.replace(old, new)  # ← step 2: use .replace on sentence

print("Updated sentence:", update)