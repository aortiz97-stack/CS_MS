# Function takes an integer input, n
# Function returns a boolean to see if n is a prime number or not
def isPrimeNumber(n):
    if n <= 1:                              # Any number less than or equal to 1 is NOT a prime number
        return False
    for factor in range(2, abs(n//2) + 1):  # Loop through factors.
        if n % factor == 0:
            return False                    # If n is divisible by any factors, it is not a prime number
    return True                             # Else, n is a prime number


num = int(input("Please enter an integer:"))
if isPrimeNumber(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")