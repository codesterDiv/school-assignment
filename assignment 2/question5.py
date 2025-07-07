''''
output:
1)      1
       2 2
      3 3 3
     4 4 4 4

2)      1
       1 2
      1 2 3
     1 2 3 4

3)      1
       2 3
      4 5 6
     7 8 9 10
'''

# output - 1

for r in range(1,5):
    print(" " * (4 - r), end=" ")
    for c in range(r):
        print(r, end=" ")
    print()


print()
print()


# output - 2

for r in range(1, 5):
    print(" " * (5 - r), end="")
    for c in range(1, r + 1):
        print(c, end=" ")
    print()


print()
print()


# output - 3

num = 1
for r in range(1, 5):
    print(" " * (5 - r), end="")
    for c in range(1, r + 1):
        print(num, end=" ")
        num += 1
    print()