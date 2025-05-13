# 24/04/2025
# A collection of python codes that perform a specific task

# This code is a simple example of using a return statement in a function.
# A function that cubes a number and returns the result.
def cube(num):
    num*num*num
cube(3) 
# This will not return anything, as there is no return statement in the function.
# To fix this, we need to add a return statement to the function.
print(cube(3)) # This will print None, as the function does not return anything.

def cube(num):
    return num*num*num
print(cube(3))
# This will print 27, as the function now returns the result of the calculation.
# The return statement is used to exit a function and return a value to the caller.

result = cube(3)
print(result) 
# This will print 27, as the result of the function is stored in the variable result.
