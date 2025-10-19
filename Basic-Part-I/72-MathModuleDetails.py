# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
72-MathModuleDetails.py

Write a Python program to get the details of the math module.
"""
# Solution 1
print("Solution 1:")

# Imports the math module
import math

# Use the 'dir' function to get a list of names in the 'math' module, including functions and constants.
# Store this list in the 'math_ls' variable.
math_ls = dir(math)

# Print the list of names in the 'math' module, which includes mathematical functions and constants.
print(math_ls)

# Solution 2
print()
print('Solution 2:')

# Import the 'math' module to access mathematical functions and constants.
import math

# Print a message to provide details about the 'math' module.
print('Details of math module:\n')
# Use the 'help' functions to display the documentation and details of the 'math' module.
# The 'help' function will show information about available functions, constants, and how to use them.
help(math)