#19/04/2025
# Getting input from users
# input() function is used to get input from users
# Inside the parenthesis, you can add a string to prompt the user for input
# The input function returns a string, so we have to convert it to a number if we want to perform arithmetic operations on it
# The input function is a blocking function, meaning it will wait for the user to enter a value before continuing with the program
# The input function is a built-in function in Python, so we don't need to import it

#The examples below show how the input obtained from the user is stored in a variable,then printed out
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + " years old.")

school = input("Enter name of your school")
print("Hello! I am in " + name + ".")

#Examples
project = input("Enter project name: ")
group_leader = input("Enter group leader name: ")
group_members = input("Enter the number of group members: ")
print("Hi all!, this is group 5. Our project is called " + project_name + "." "My name is " + group_leader + " together with my group members we are " + group_members + " in total.")
