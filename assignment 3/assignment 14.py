'''
write a program to accept a string and check weather it is a palindrome or not.
'''


s = input("Enter a string: ")
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")