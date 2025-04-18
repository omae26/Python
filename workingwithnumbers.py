# Working with numbers

print(5)
print(2.57)
print(-2.57)
print(3+4)
print(3+4.5)
print(3*4.5)
print(3*(4+5))

# The modulus operator %,it returns the remainder of a division
print(10%3)
print(10//3) # floor division
print(10/3) # normal division

# Storing numbers in a variable
my_num = 5
print(my_num)

# How to conver a number to a string. It helps to concatenate a number with a string or when we want to print a number with a string
print(str(my_num))
print(str(my_num) + " is my favorite number")
# Anytime we want to convert a number to a string or to use a number togetther with a string, we 
# have to use a str() function to convert the number to a string

# Common functions while working with numbers
#asolte value function, abc()
my_num = -5
print(abs(my_num))

#power function, pow()
print(pow(3, 2)) # 3^2 = 9
print(pow(4, 2)) # 4^2 = 16
print(pow(2, 3)) # 2^3 = 8

# max function, max()
# It returns the largest number in a set of numbers
print(max(4, 6)) 

# min function, min()
print(min(4,1)) 

#round function, round(). It rounds a number to the nearest integer
print(round(3.2))
print(round(3.7))
