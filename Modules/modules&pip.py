# 26/05/2025
# A module is essentially a python file that we can import into our current pyhton file.
# We have built in and external modules, but we can also create our own.
# It is also great to use modules written by other dvelopers.
# The other file we're using is useful.py
# The import keyword is used to import a module

import Modules.useful as useful

print(useful.roll_dice(10))

# How to use external modules:
# 1. Install the module using pip
# 2. Import the module in your code
# 3. Use the module's functions or classes

# pip
# pip is a package manager for Python that allows you to install and manage external libraries and modules.
# To install a module, you can use the command: # pip install module_name
# To uninstall a module, you can use the command: # pip uninstall module_name
# Externally downloaded modules are stored in the site-packages directory of your Python installation.
