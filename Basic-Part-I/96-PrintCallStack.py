# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
96. Print Call Stack

Write a Python program to print the current call stack.
"""

# Import the 'traceback' module.
import traceback

# Print an empty line for formatting.
print()

# Define a function 'f1' that calls the 'abc' function.
def f1():
    return abc()

# Define the 'abc' function that prints the current stack using 'traceback.print_stack()'.
def abc():
    traceback.print_stack()

# Call the 'f1' function, which, in turn, calls the 'abc' function.
f1()

# Print an empty line for formatting.
print()