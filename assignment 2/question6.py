'''
output:

1)  * * * * *
    *       *
    *       *
    *       *
    *       *
    * * * * *

2)  *  *  *  *  *
    *  *     *  *
    *     *     *
    *  *     *  *
    *  *  *  *  *
'''






# Pattern 1

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print()
print()


n = 5
for i in range(n):
    for j in range(n):
        if (
            i == 0 or i == n-1 or j == 0 or j == n-1 or
            (i == 1 and j == 1) or
            (i == 1 and j == n-2) or
            (i == 2 and j == 2) or
            (i == n-2 and j == 1) or
            (i == n-2 and j == n-2)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()