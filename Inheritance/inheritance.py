# 26/05/2025
# Inheritance is basically allows us to create a new class that is based on an existing class.
# The new class bears the properties and methods of the existing class, 
# but can also have additional properties and methods of its own.

from chef import Chef
from chinesechef import ChineseChef

myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()
