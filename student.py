# Creaing our student data type by defining a bunch of attributes
# We can use strings, integers etc

class Student:
    def __init__(self, name, major, gpa, is_on_probation):   #This is a student data type
        self.name = name  # The object's name is equal to the actual name passed in
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):    # This is a method(a defined functn) that checks if the student is on the honor roll
        if self.gpa >= 3.5:
            return True
        else:
            return False