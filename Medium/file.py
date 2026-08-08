filename = input("Enter file name: ")

if filename.endswith('.py'):
    print("Python File")
elif filename.endswith('.txt'):
    print("Text File")
elif filename.endswith('.pdf'):
    print("PDF File")
elif filename.endswith('.jpg'):
    print("JPG Image")
else:
    print("Unknown File Type")