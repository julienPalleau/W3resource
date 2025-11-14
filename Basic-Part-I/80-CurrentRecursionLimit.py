# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
80. Current Recursion Limit

Write a Python program to get the current value of the recursion limit.
"""
import sys  # Import the sys module to access system-related information

print()  # Print a blank line for spacing
print("Current value of the recursion limit:")  # Display a message about the recursion limit
print(sys.getrecursionlimit())  # Retrieve and print the current recursion limit
print()  # Print a blank line for spacing