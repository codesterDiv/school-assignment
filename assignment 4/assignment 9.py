#   1 + 2 + 3 + ... + n

n = int(input("Enter a number: "))
total = sum(range(1, n + 1))
print("The sum of numbers from 1 to", n, "is:", total)