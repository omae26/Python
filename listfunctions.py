# 21/04.2025
# Using functions with lists in python

lucky_numbers = [4, 8, 15, 16, 23, 2]
friends = ["Ross", "Rachel", "Monica", "Chandler", "Joey", "Joey", "Phoebe"]

# List functions
#sort() - sorts the elements of a list in ascending order
friends.sort() # alphabetically
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

# copy() - creates a copy of a list
friends2 = friends.copy()
print(friends2)

# reverse() - reverses the order of the elements in a list
friends.reverse() # reverses the order of the elements in the list
lucky_numbers.reverse() # reverses the order of the elements in the list
print(friends)
print(lucky_numbers)

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

#index() - returns the index of  a specified element in a list
#It holds 1 parameter, the element you want to find the index of in the list
#It returns the index of the first occurrence of the element in the list
print(friends.index("Rachel"))

#count() - returns the number of occurrences of a specified element in a list
#It holds 1 parameter, the element you want to count in the list
print(friends.count("Joey"))



#pop() - removes the last element from a list and returns it
#It holds 1 parameter, the index of the element you want to remove from the list
print(friends.pop()) #removes the last element from the list and returns it


#clear() - removes all elements from a list
#It holds no parameters
friends.clear()
lucky_numbers.clear()
print(lucky_numbers)





print(friends)

