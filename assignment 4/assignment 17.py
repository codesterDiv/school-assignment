# sum of digits of any given number

n = int(input("Enter a number: "))
sum_of_digits = 0
while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n //= 10
print("The sum of the digits is:", sum_of_digits)