'''
write a program to get the following output:

str2 = ' we are in school'
output = 'w*e* *a*r*e* *i*n* *s*c*h*o*o*l'
'''

str2 = ' we are in school'
output = '*'.join(str2.strip())
print(output)