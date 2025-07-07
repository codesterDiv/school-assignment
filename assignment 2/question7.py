'''
output:
1)  * * * * *
        *
        *
        *
        *
    * * * * *

2)  *       *
    *       *
    * * * * *
    *       *
    *       *

3). * * * * *
    *       *
    * * * * *
    *       *
    *       *
'''

# Pattern 1
for i in range(6):
    if i == 0 or i == 5:
        print("* " * 5)
    else:
        print("    *")

print()

# Pattern 2
for i in range(5):
    if i == 2:
        print("* " * 5)
    else:
        print("*       *")

print()

# Pattern 3
for i in range(5):
    if i == 0 or i == 2:
        print("* " * 5)
    else:
        print("*       *")