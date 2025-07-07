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

# output - 1
n = 5
for i in range(1,5):
    for j in range(1,5):
        if (
            i == 0 or i == n-1 or j == 0 or j == n-1 or
            (i == 1 and j == 1) or
            (i == 1 and j == n-2) or
            (i == 2 and j == 2) or
            (i == n-2 and j == 1) or
            (i == n-2 and j == n-2)
        ):














# hello
print()