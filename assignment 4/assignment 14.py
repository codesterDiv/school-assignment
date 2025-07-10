#   1 + (1+2) + (1+2+3) + ... + (1+2+...+n)

n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += sum(range(1, i + 1))
print("The sum of series is:", total)