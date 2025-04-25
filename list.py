# 20/04/2025
# Lists in  Python
# Lists are mutable, ordered collections of items
# Lists can contain items of different types; strings, integers, floats, booleans, etc.
# Lists are defined using square brackets []
# Lists can be empty or contain multiple items
# Lists are indexed starting from 0; The index are used to access items in the list
# The differenc between a list and variable is that a list can contain multiple items, a variable can only contain one item
# Lists can be nested, meaning that a list can contain other lists as items
# Lists can be sliced, meaning that you can get a sublist from a list using the colon operator [:]

friends = ["Ross", "Rachel", "Monica", "Chandler", "Joey", "Phoebe"]
print(friends)
print(friends[0]) # Ross
print(friends[-1])  # Accessing the last item in the list, which is Phoebe
print(friends[1:]) # Accessing all items in the list starting from index 1, which is Rachel, Monica, Chandler, Joey, Phoebe
print(friends[:3]) # Accessing all items in the list up to index 3, which is Ross, Rachel, Monica
print(friends[0:3])

# Modifying items in a list
friends[2] = "Monica Geller"
print(friends[2])
print(friends)
