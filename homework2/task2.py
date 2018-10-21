string = input("Please enter string:")
print(string)
if string[::-1] == string:
    print("True, the string is palindrome")
else:
    print("False, the string isn't palindrome")
