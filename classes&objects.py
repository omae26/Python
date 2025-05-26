# 26/05/2025
# Classes and Objects
# They allow us to model multiple real world objects in a single file.
# Classes are blueprints for creating objects. Objects are instances of classes.

# Creating an actual student (from student.py) - Object
# In order to use the student class, we need to import it first.
# from(file) import (class)

from student import Student

student1 = Student("Jim", "Business", 3.1, False)  # Creating an object of the Student class
student2 = Student("Pam", "Art", "2.5", "True")
print(student1.name)  # Accessing the name attribute of the student object
print(student1.major)  # Accessing the major attribute of the student object
print(student2.is_on_probation)