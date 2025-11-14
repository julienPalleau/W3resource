# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
76-Command-lineArguments.py

Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
"""
# Import the sys module to access command-line arguments and other system-specific functionality.
import sys

# Display the message "This is the name/path of the script:" and print the script's name or path.
print(f"This is the name/path of the script: {sys.argv[0]}")

# Display the message "Argument List:" and print the list of command-line arguments passed to the script.
print(f"Argument List: {sys.argv}")