'''
WAP to acccept a string and display the following:
s = 'HIMALAYA'
output: s1 = 'HI_AL_YA'
'''

s = input("Enter a string: ")
s1 = s[:2] + '_' + s[2:4] + '_' + s[4:6] + '_' + s[6:]
print("s1 =", s1)