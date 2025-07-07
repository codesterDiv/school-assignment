'''
output :

1)  + + + +
    + + + +
    + + + +


2)  A A A
    A A A
    A A A


3)  1 1 1
    1 1 1
    1 1 1
    1 1 1
'''



# output - 1:
for r in range(1,4):
    for c in range(1,5):
        print("+", end=" ")
    print()


print()
print()


#  output - 2:
for r in range(1,4):
    for c in range(1,4):
        print("A", end=" ")
    print()


print()
print()


# output - 3:
for r in range(1,5):
    for c in range(1,4):
        print("1", end=" ")
    print()