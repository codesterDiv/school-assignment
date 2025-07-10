# find armstrong number of a given number

n = int(input("Enter a number: "))
armstrong_sum = 0
temp = n
num_digits = len(str(n))
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp //= 10
if armstrong_sum == n:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")