# Solution to subproblem 1
invitees_list = ['Jocelyne', 'Gely', 'Hector']
print("List of invitees:", invitees_list) # print invitees_list

invitees_list.remove('Hector') # remove guest Hector
invitees_list.append('Jose') # append new guest Jose to end of list
print("Revised list of invitees:", invitees_list)

invitees_list.insert(0, "Juanita") # insert a new list at the beginning of the list
invitees_list.insert(2, "Doro") # insert invitee Doro into the middle of the list
invitees_list.append("Martin") # append guest Martin to the end of the list
print("Second revision list of invitees:", invitees_list)

while len(invitees_list) > 2: # use while loop to remove guests one at a time until there are two left
    uninvited_guest = invitees_list.pop()
    print(f"Sorry, {uninvited_guest}, but you are uninvited to dinner") #print an apology for each uninvited guest


# Solution to subproblem 2
animal_list = ['panda', 'racoon', 'giraffe', 'hamster', 'lizard', 'armadillo', 'turtle']
print("The first three items in the list are", animal_list[:3]) # prints list slice from beginning of list to index 2
print("Three items from the middle of the list are", animal_list[2:5]) # prints list slice from index 2 to index 4 
print("The last three items in the list are", animal_list[4:]) # prints list slice from index 4 to end of list


# Solution to subproblem 3
def create_list_of_duplicates(input_list): # function takes a list as input, returns another list with duplicate elements of input list only
    output_list = []
    already_seen = {} # dictionary to keep track of input_list values as keys and their frequencies as value pair
    for item in input_list:
        if item not in already_seen.keys(): # check to see if item is not in keys
            already_seen[item] = 1 # add item to dictionary with a frequency of 1
        else:
            already_seen[item] += 1 # if already in dictionary, add frequency occurrence by 1
    for item in input_list:
        if already_seen[item] > 1 and item not in output_list: # if there was more than one instance of item appearing in input_list, then append item to output list
                                                               # Do not add item to output list if it is already in output list
            output_list.append(item)
    return output_list

# Create list and test create_list_of_duplicates function
test_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(create_list_of_duplicates(test_list)) # print output list


# Solution to subproblem 4
basic_food_tuple = ('pasta', 'rice', 'beans', 'salad', 'boiled eggs')
for food_item in basic_food_tuple:
    print(f"We serve {food_item}.") # print each food_item in basic_food_list

# Code line below commented out so rest of program can execute
# del basic_food_tuple[4] # Python will throw an error because you cannot modify items in a tuple.

basic_food_list = list(basic_food_tuple) # convert tuple to list to edit tuple contents
basic_food_list[0] = "crackers"
basic_food_list[-1] = "gelatin"
new_basic_food_tuple = tuple(basic_food_list) # convert list back to tuple
for food_item in new_basic_food_tuple:
    print(f"We now serve {food_item}.")


# Solution to subproblem 5
def second(n): # function returns the second item of the tuple n
    return n[1]
def sort_tuples_by_second_item(input_list): # function takes a list of tuples as input. Returns a list with tuples sorted by second item
    return sorted(input_list, key=second) # using second item in tuple, sort list of tuples

test_list = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
print(sort_tuples_by_second_item(test_list))










