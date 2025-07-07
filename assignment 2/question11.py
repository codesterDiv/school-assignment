'''
output:
1)  Z Z Z
    Y Y Y
    X X X

2)  10 11 12
    13 14 15
    16 17 18

3)  10 20 30
    40 50 60
    70 80 90

4)  1
    4  4
    9  9  9
    16 16 16 16
'''


# 1)
for ch in ['Z', 'Y', 'X']:
    print((ch + ' ') * 3)

print()

# 2)
num = 10
for _ in range(3):
    for _ in range(3):
        print(num, end=' ')
        num += 1
    print()

print()

# 3)
for i in range(10, 100, 30):
    for j in range(i, i + 30, 10):
        print(j, end=' ')
    print()

print()

# 4)
for i in range(1, 5):
    for _ in range(i):
        print(i * i, end=' ')
    print()