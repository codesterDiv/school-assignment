'''
output:

write a program to accept a string and replace the vowels with '*'.
'''

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""
for char in s:
    if char in vowels:
        result += "*"
    else:
        result += char
print("Output:", result)