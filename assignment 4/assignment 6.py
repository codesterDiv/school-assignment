#   1!, 2!, ... , n!

# Factorial of a number n is the product of all positive integers up to n.

n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("The factorial of numbers upto", n, "is :", factorial)