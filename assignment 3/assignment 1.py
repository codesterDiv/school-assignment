'''
output:

write a proram to accept a string and count the number of vowels in it.

'''

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print("Number of vowels:", count)