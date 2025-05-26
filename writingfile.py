# 26/05/2025
# Writing and appending to a file

# employee_file = open("employess.txt", "a") # Open the file in append mode
# employee_file.write("\nKelly - Customer Service")  # Write a new line to the file

#employee_file = open("employess.txt", "w")  # Open the file in write mode
#employee_file.write("\nKelly - Customer Service") # Overwrite the file with new content
#employee_file.close()

# 'w' can also be used to create a new file if it does not exist

employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()