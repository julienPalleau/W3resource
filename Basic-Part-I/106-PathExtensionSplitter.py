# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
106. Path Extension Splitter

Write a Python program to divide a path by the extension separator.
"""
# W3resource
# Solution 1:

# Import the 'os.path' module for working with file paths.
import os.path
# Iterate through a list of example file paths.
for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
    # Print the file path and its corresponding file extension using 'os.path.splitext()'.
    print(f"{path} : {os.path.splitext(path)}")