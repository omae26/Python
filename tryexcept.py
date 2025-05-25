# catching errors in python
# It mainly prevents the error message from blocking the running of the code
# 25/05/2025

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input!")

# Using except alone is too broad. It is important to specify the type of error