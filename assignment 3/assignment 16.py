'''
write a program to accept a string a display the longest string.
'''

strings = input("Enter strings separated by spaces: ").split()
longest = max(strings, key=len)
print("The longest string is:", longest)