# 16/04/2025
# Working with strings 
# Strings are a sequence of characters enclosed in quotes
# Strings can be enclosed in single quotes or double quotes
# Strings are immutable, meaning they cannot be changed after they are created
# To change a string, you must create a new string

print("Giraffe Academy")

#\n is used to create a new line in the string
print("Giraffe\nAcademy")

#\ is used as an escape character to allow the use of quotes in a string
print("Giraffe\"Academy")

#\t is used to create a tab space in the string
print("Giraffe\tAcademy")

# Variables in strings
phrase = "Giraffe Academy"
print(phrase)
# Concatenation is used to combine two strings together
print(phrase + " is cool")

# Functions in strings are used to modify strings, to get information about strings
# They are used to perform operations on strings
phrase ="Giraffe Academy"

print(phrase.lower())
print(phrase.upper())
# This prints the string in lower case and upper case

# A function to check if the string is upper or lower case
print(phrase.isupper())

#  Combination of functions
# A function to check if the string is upper case after converting it to upper case
print(phrase.upper().isupper())

# A function to determine the length of the string
print(len(phrase))

# A function to get individual characters in a string
print(phrase[0]) # This prints the first character of the string
print(phrase[3]) # This prints the second character of the string
print(phrase[0:3]) # This prints the first three characters of the string
print(phrase[0:]) # This prints the first four characters of the string

# The Index function is used to find the index of a character in a string
print(phrase.index("a")) # This prints the index of the first occurrence of the character "a" in the string

# The replace function is used to replace a character in a string with another character
print(phrase.replace("Giraffe", "Elephant")) # This replaces the word "Giraffe" with "Elephant" in the string