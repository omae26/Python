# 2/05/2025
# Dictionaries allow us to store infromation in key-value pairs.
# They are mutable, unordered, and indexed by keys.

# Example: Converting a 3-digit month name into a full-month name.
# The month name (data) is the key and the full- month name is the value.
# Keys can be numbers, strings, or tuples.

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
# How to access the values in the dictionary, we have 2 meothods that we cam use
# We refer to the key in the dictionary to get the value.
print(monthConversions["Nov"]) # November
print(monthConversions.get("Dec")) # December)

# print(monthConversions.get("Luv")) # This will return None, since the key is not in the dictionary.
# We can also set a default value to be returned if the key is not found in the dictionary.
print(monthConversions.get("Luv", "Not a valid key"))