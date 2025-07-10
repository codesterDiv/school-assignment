#    1 + 4 + 9 + ... + n^2

n = int(input("Enter a number: "))
total = sum(i**2 for i in range(1, n + 1))
print("The sum of squares from 1 to", n, "is:", total)