# 21/04.2025
# Using functions with lists in python

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ross", "Rachel", "Monica", "Chandler", "Joey", "Phoebe"]

# List functions
# extend() - adds elements of a list to another list i.e allows you to take a listand append another list onto the end of it
friends.extend(lucky_numbers)

# append() - adds a single element to the end of a list
friends.append("Gunther")

#insert() - adds a single element at a specific index in a list e.g.in the middle of the list
#It holds 2 parameters, first the index where you want to insert the element and second the element itself
friends.insert(2, "Janice")

#remove() - removes a specified element from a list
#It holds 1 parameter, the element you want to remove from the list
friends.remove("Janice")
print(friends)