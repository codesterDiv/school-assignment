#   max digit of a number

n = int(input("Enter a number: "))
max_digit = 0
while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n //= 10
print("The maximum digit is:", max_digit)