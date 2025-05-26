# Manipulating a file

# How to check if a file is readable

employee_file = open("employess.txt", "r")
# print(employee_file.readable())  # Returns True if the file is readable, False otherwise
# print(employee_file.read()) # Reads the content of the file if it is readable
# print(employee_file.readline())  # Reads the first line of the file
# print(employee_file.readline()) # Reads the second line of the file
# print(employee_file.readlines())  # Takes all the lines in the file and puts them inside a list
# print(employee_file.readlines()[1])  # Accesses specific elements in the list via their respective index

# We cana also use a for loop to iterate through the lines in the file
for employee in employee_file.readlines():
    print(employee)
    #print(employee.strip())  # Removes any leading/trailing whitespace characters including newlines
employee_file.close()            # Closes the file after checking readability