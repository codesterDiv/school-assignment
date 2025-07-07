'''
write a program to accept a string and count the number of alphabets, digits, spaces, and special characters and display the count.
'''


s = input("Enter a string: ")
alphabets = digits = spaces = special = 0

for char in s:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)