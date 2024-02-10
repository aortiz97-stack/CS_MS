def prime_number_problem():
    # Function takes an integer input, n
    # Function returns a boolean to see if n is a prime number or not
    def isPrimeNumber(n):
        if n <= 1:                              # Any number less than or equal to 1 is NOT a prime number
            return False
        for factor in range(2, abs(n//2) + 1):  # Loop through factors.
            if n % factor == 0:
                return False                    # If n is divisible by any factors, it is not a prime number
        return True                             # Else, n is a prime number

    # Get user input for number, print if it is prime or not based on response.
    num = int(input("Please enter an integer to see if it is prime or not: "))
    if isPrimeNumber(num):
        print(f"{num} is a prime number.\n")
    else:
        print(f"{num} is not a prime number.\n")


def fibonacci_sequence_problem():
    # Function creates an array with fibonacci sequence numbers.
    # Input is an integer num.
    # Output is an array containing fibonacci sequence numbers up to num numbers.
    def createFibonacciSeq(num):
        if num < 1:
            return None
        if num == 1:
            return [0]
        fibonacci_seq = [0, 1]
        while len(fibonacci_seq) < num:
            last_idx = len(fibonacci_seq)-1
            fibonacci_seq.append(fibonacci_seq[last_idx] + fibonacci_seq[last_idx-1])
        return fibonacci_seq

    # Obtain user input for position number, print number in that position number
    pos_num = int(input("Enter which position in the fibonacci sequence you would like to see. Index starts at 1, not 0. Index must be greater than or equal to 1: "))
    if pos_num < 1:
        print("The number you entered is not greater than or equal to 1.\n")
    else:
        fibonacci_seq = createFibonacciSeq(pos_num)
        print(f"{fibonacci_seq[-1]}\n")


def if_elif_else_age_problem():
    age = int(input("Please input an age in years to see which lifestage the person belongs to: "))

    # Use if-elif chain to categorize age by lifestage.
    if age < 2:
        print("This person is a baby.\n")
    elif age < 4:
        print("This person is a toddler.\n")
    elif age < 13:
        print("This person is a kid.\n")
    elif age < 20:
        print("This person is a teenager.\n")
    elif age < 65:
        print("This person is an adult.\n")
    elif age >= 65:
        print("This person is an elder.\n")


def movie_ticket_cost_problem():
    user_input = input("Please enter your age so I can provide accurate movie ticket prices: ")
    age = int(user_input)
   
    # Use if-elif-else chain to determine price of movies by age
    if age < 3:
        print("The movie ticket is free!\n")
    elif age < 13:
        print("The movie ticket price is $10.\n")
    else:
        print("The movie ticket price is $15.\n")
        


def asterisk_pattern_problem():
    asterisk_string = "*"
    space_number = 4 # number of spaces to add before asterisk_string
    count = 0 # variable to track how many iterations to go through while loop
    while count < 5:
        string_to_print = " "*space_number + asterisk_string
        print(string_to_print)

        # Update variables
        asterisk_string += ' *'
        space_number -= 1
        count += 1

# Execute functions to solve problems
prime_number_problem()
fibonacci_sequence_problem()
if_elif_else_age_problem()
movie_ticket_cost_problem()
asterisk_pattern_problem()




            







            




