# Reading external files(text files, csvs etc) in python
# 25/05/2025
# We can use various commands to access the external files
# Some of the commands are:

open('employes.txt', 'r')  # Opens the file in read mode. not modifying it, just reading
open("employess.txt", "w")  # Opens the file in write mode. Allows the user to modify the file. 
open("employess.txt","a") # Opens the file in append mode. Allows the user to add new content to the end of the file without modifying existing content.
open("employess.txt","r+") # Opens the file in read and write mode. Allows the user to read and modify the file.
open("employess.txt","a+") # Opens the file in append and read mode. Allows the user to read and add new content to the end of the file.
open("employess.txt","x") # Opens the file in exclusive creation mode. If the file already exists, it raises an error. If it does not exist, it creates a new file.

# We can read the contents of the file using the read() method.
# We can also use the with statement to open files, which automatically closes the file after the block of code is executed.

employee_file = open('employess.txt', 'r')
employee_file.close()  # Closes the file after reading