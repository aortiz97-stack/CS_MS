#Subproblem 1: Write a python script to concatenate dictionaries
def concatenate_dictionaries(*dictionaries): #input is a non-keyword argument of dictionaries, output is concatenated dictionary
    output_dict = {}
    for dictionary in dictionaries:
        output_dict.update(dictionary) #update method adds dictionary to output_dict
    return output_dict

#Test function using three dictionary examples
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
concatenated_dict = concatenate_dictionaries(dic1, dic2, dic3)
print(concatenated_dict)


#Subproblem 2: Write a python script that prints dictionary containing a number 1 to n in the form of (x, x*x)
def number_times_number_dictionary(n): #function takes integer n as input, output is dictionary with numbers 1 to n in form of (x, x*x)
    output_dict = {}
    for i in range(1, n + 1):
        output_dict[i] = i*i
    return output_dict

#Test function using n = 5 example
n5_example = number_times_number_dictionary(5)
print(n5_example)


#Subproblem 3: Write a python script combining two dictionary adding values for common keys
#Function takes two dictionaries d1 and d2 as input. For keys in common, function adds values of common keys together.
#Returns output dict with common key value sums paired with original keys
def counter(d1, d2):
    output_dict = {}
    if len(d1.keys()) > len(d2.keys()): #In case dictionaries are not same size, need to find longer one to use for for-loop traversal
        longer_dict = d1
        shorter_dict = d2
    else:
        longer_dict = d2
        shorter_dict = d1
    for k in longer_dict.keys():
        if k in shorter_dict.keys():
            output_dict[k] = longer_dict[k] + shorter_dict[k] #If key is in both dictionaries, add sum of values to output_dict with k as key
        else:
            output_dict[k] = longer_dict[k] #If not, simply add longer_dict key and value pair to output_dict
    
    for k in shorter_dict.keys():
        if k not in output_dict.keys(): #In case there were keys not found in longer_dict, add shorter_dict keys and values pairs to output_dict
            output_dict[k] = shorter_dict[k]
    return output_dict

#Test function using two dictionary test cases
d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}
counter_dict = counter(d1, d2)
print(counter_dict)


#Subproblem 4: Write a function called make_shirt()
def make_shirt(size, message): #function takes string inputs size and message.
    print(f"The size that you requested for the shirt is {size}. The message that will be printed on the shirt is '{message}'.")

#Function call using positional arguments
make_shirt('small', "Awesome Shirt!")

#Function call using keyword arguments
make_shirt(message="I'm hers", size="large")


#Subproblem 5: Modify the function make_shirt() to include a default_message
def make_shirt(size, message="I love Python"):
   print(f"The size that you requested for the shirt is {size}. The message that will be printed on the shirt is '{message}'.")

#Function calls with large and medium shirts that have default messages. Small shirt with a personal message.
make_shirt("large")
make_shirt("medium")
make_shirt("small", "I Love You")

