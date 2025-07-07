'''
output : 

1)  1 1 1
    2 2 2
    3 3 3


2)  1 2 3
    1 2 3
    1 2 3


3)  1 2 3
    4 5 6
    7 8 9
'''


print()
print()


# output - 1
for r in range(1,4):
    for c in range(1,4):
        print(r, end=" ")
    print()


print()
print()


# output - 2
for r in range(1,4):
    for c in range(1,4):
        print(c, end=" ")
    print()


print()
print()


# output - 3
a = 1
for r in range(1,4):
    for c in range(1,4):
        print(a, end=' ')
        a += 1
    print()