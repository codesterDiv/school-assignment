# Define the range
start = 10
end = 20

print(f"Prime numbers between {start} and {end}:")

# Check each number in the range
for number in range(start, end + 1):
    # Skip numbers less than 2
    if number <= 1:
        continue
    
    # Check for prime
    prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            prime = False
            break
    
    # Print if prime
    if prime:
        print(number, end=' ')
