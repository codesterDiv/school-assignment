'''
output:

1)  A A A
    B B B
    C C C

2)  A B C
    A B C
    A B C

3)  A B C
    D E F
    G H I
'''


# 1)
for i in range(3):
    print(chr(65 + i), chr(65 + i), chr(65 + i))
print()

# 2)
for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=' ')
    print()
print()

# 3)
count = 0
for i in range(3):
    for j in range(3):
        print(chr(65 + count), end=' ')
        count += 1
    print()