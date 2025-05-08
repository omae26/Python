# 1/05/2025
# If statements with comparisons; comparison operators (==, !=, <, >, <=, >=) are used to compare values.

# Example. A function that returns the largest of three numbers
# Comparison of numbers using if statements
def max_num(num1, num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>= num1 and num2>=num3:
        return num2
    else:
        return num3
    
print(max_num(3, 4, 5)) #5

# Comparison of strings using if statements
# We often use == or != to compare strings
# Example. A function that returns the longest of three strings
def longest_string(str1, str2, str3):
    if len(str1) >= len(str2) and len(str1) >= len(str3):
        return str1
    elif len(str2) >= len(str1) and len(str2) >= len(str3):
        return str2
    else:
        return str3
    
print(longest_string("dog", "book", "umbrella")) # umbrella