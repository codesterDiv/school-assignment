#   0 1 1 2 3 5 8 ... n

n = int(input("Enter a number: "))
a, b = 0, 1
print("Fibonacci series up to", n, "is:", end=' ')
while a <= n:
    print(a, end=' ')
    a, b = b, a + b
print()  # For a new line after the series output