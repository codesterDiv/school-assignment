'''
write a program to count the frequency of a character.
'''

text = input("Enter a string: ")
char = input("Enter a character to count: ")
count = text.count(char)
print(f"The frequency of '{char}' is: {count}")