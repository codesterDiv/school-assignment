# accept a numner and check weather it is prime number or not.


# Input from the user
number = int(input("Enter a number: "))

# Check if the number is prime
prime = True  # Assume number is prime initially

if number <= 1:
    prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            prime = False
            break

# Print the result
if prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
