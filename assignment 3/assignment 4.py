''''
write a program to get the following output:
str1 = 'TELEVISION'
output = "TE_EV_SI_N"
'''


str1 = 'TELEVISION'
output = ''
for i, c in enumerate(str1):
    if i % 2 == 0:
        output += c
    else:
        output += '_'
print(output)