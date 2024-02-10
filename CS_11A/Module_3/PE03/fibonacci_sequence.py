# Function creates an array with fibonacci sequence numbers.
# Input is an integer num.
# Output is an array containing fibonacci sequence numbers up to num numbers.
def createFibonacciSeq(num):
    # Return None if num is less than 1. 
    if num < 1:
        return None
    # Return [0] if only wanting to generate one fibonacci sequence number
    if num == 1:
        return [0]
    
    fibonacci_seq = [0, 1]

    # Continue adding numbers until the length of the fibonacci sequence equals num
    while len(fibonacci_seq) < num:
        last_idx = len(fibonacci_seq)-1
        fibonacci_seq.append(fibonacci_seq[last_idx] + fibonacci_seq[last_idx-1])
    
    return fibonacci_seq

# Code below prints output revealing which number in the fibonacci sequence is at the 
# pos_numth position. Index begins at 1, not 0.
pos_num = int(input("Enter which position in the fibonacci sequence you would like to see.Index starts at 1, not 0. Index must be greater than or equal to 1: "))
if pos_num < 1:
    print("The number you entered is not greater than or equal to 1.")
else:
    fibonacci_seq = createFibonacciSeq(pos_num)
    print(fibonacci_seq[-1])




    


