'''
output : 
1)      *
       * *
      * * *
     * * * *

2)      *
       * *
      * * *
     * * * *
      * * *
       * *
        *
'''


# Pattern 1
n = 4
for i in range(1, n+1):
    print(' ' * (n - i) + '* ' * i)

print()


print()
print()


# Pattern 2
for i in range(1, n+1):
    print(' ' * (n - i) + '* ' * i)
for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '* ' * i)