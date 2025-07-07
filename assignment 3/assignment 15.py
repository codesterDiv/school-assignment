'''
write a program to accept a string:
1) display the string
2) display the digits in the string
3) find the sum the the digits and display
'''

s = input("Enter a string: ")
print("The string is:", s)

digits = [int(ch) for ch in s if ch.isdigit()]
print("Digits in the string:", digits)

print("Sum of digits:", sum(digits))