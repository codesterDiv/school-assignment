'''
output:

1)  A
    B B
    C C C
    D D D D

2)  A
    A B
    A B C
    A B C D

3)      A
       B B
      C C C
     D D D D
'''



print()
print()


# Pattern 1
for i in range(1, 5):
    print(' '.join(chr(64 + i) for _ in range(i)))
print()


print()
print()


# Pattern 2
for i in range(1, 5):
    print(' '.join(chr(64 + j) for j in range(1, i + 1)))
print()


print()
print()


# Pattern 3
for i in range(1, 5):
    print(' ' * (4 - i) + ' '.join(chr(64 + i) for _ in range(i)))