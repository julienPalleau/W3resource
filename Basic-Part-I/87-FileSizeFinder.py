# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
87. File Size Finder

Write a Python program to get the size of a file.
"""

# Solution 1 using os
import os

# Open the file 'Basic-Part-I/87-FileSizeFinder.py' in default read.mode.
file = open('Basic-Part-I/87-FileSizeFinder.py')
print(file)

# Move the file cursor to the end of the file using file.seek()
print(file.seek(0, os.SEEK_END))

# Print the current position of the file cursor, which represents the size of the file.
print("The size of main.py is:", file.tell(), "bytes")