'''
accept 2 string and disply the string which is larger than the other.
'''

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) > len(str2):
    print("Larger string:", str1)
elif len(str2) > len(str1):
    print("Larger string:", str2)
else:
    print("Both strings are of equal length.")