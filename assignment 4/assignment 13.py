# x/1! + x/2! + x/3! + ... + x/n!

n = int(input("Enter a number: "))
x = float(input("Enter the value of x: "))
factorial_sum = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    factorial_sum += x / factorial