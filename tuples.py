#22/04/2025

# A tuple is a type of data structure. This means that it is a container that can store different values.
# Tuples are similar to list, but they have some key differences. They main one being, once data is added to a tuple it can't be changed, but for lists you can change values.

# How to create a tuple
# A tuple is created by placing all the items (elements) inside parentheses (), separated by commas.
# Tuples are immutable, meaning that you cannot change, add, or remove items once the tuple is created.
# Tuples allow duplicate values.
# Tuples can contain different data types, such as strings, integers, and booleans.
# Tuples can be empty, meaning they can contain no items.

coordinates = (4, 5)
#coordinates[1] = 10  # This will raise a TypeError because tuples are immutable
print(coordinates[0])  # Output: 4
print(coordinates[1])  # Output: 5

color = (ffff, dddd)
print(color[0])
print(color[1])

# Tuples are often used for data that can never change e.g. coordinates, RGB values,radius of the earth etc.
