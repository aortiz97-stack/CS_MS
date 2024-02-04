#Assigning list1 to variable
list1 = ['physics', 'chemistry', 1997, 2000]

#Assigning list2 to variable
list2 = [1, 2, 3, 4, 5, 6, 7]

#accessing
print("list1[0]: ", list1[0]) #prints value at index 0 of list 1
print("list2[1:5]: ", list2[1:5]) #prints values in indices 1-4 of list 2

#updating
print("Value available at index 2 : ")
print(list1[2]) #prints value at index 2 of list1
list1[2] = 2001 #assign new value 2001 at index 2 of list1
print("New value available at index 2: ")
print(list1[2]) #print new valu at index 2 of list1

#Adding
list1.append(2020)
print("New List:", list1)
