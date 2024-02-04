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

