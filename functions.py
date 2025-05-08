# 22/04/2025
# A function is a collection of statements which perform a specific task.
# Functions are used to break down a program into smaller, more manageable pieces.
# Functions can take inputs (arguments) and return outputs (results).

# Functions can be defined using the def keyword, followed by the function name and parentheses.

# A function that says hello to the user
def say_hi(): # After the colons, all the code that comes after is going to be part of the function. We therefore have to indent it.
    print("Hello user!")

# For us to execute the function, we have to call it. 
# This is done by writing the function name followed by parentheses.

say_hi() # Output: Hello user!

# Naming functions in python has to be done in lowercase letters.
# If the function name has more than one word, we separate them with underscores.

# A parameter,is a piece of informatioon that we give to a fucntion when we call it. 
# We can pass any type of data to a function as a parameter, including strings, integers, booleans and lists.
# Example of a function with a parameter:
def say_hi(name):
    print("Hello " + name + "!" )
say_hi("John")
say_hi("James")

# A function can have multiple parameters.
# Example of a function with multiple parameters:
def say_hi(name, age):
    print("Hello " + name + "! You are " + age + " years old.")

say_hi("Mike", "25")
say_hi("Sarah", "30")

def project_name():
    print("Lift controller mechanism")
project_name()
    
