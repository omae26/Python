# 26/05/2025
# Class functions are functions that are defined inside a class.

from student import Student
student1 = Student("Oscar",  "Accounting", "3.1", False)
student2 = Student("Phyllis", "Business", "3,8", True)

print(student2.on_honor_roll())  # This will call the on_honor_roll method for student1

