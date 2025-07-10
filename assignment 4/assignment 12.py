#    1/1! + 1/2! + 1/3! + ... + 1/n!

n = int(input("Enter a number: "))
factorial_sum = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    factorial_sum += 1 / factorial