# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
63-AbsoluteFilePathFinder.py

Write a Python program to get an absolute file path.
"""
# Solution 1
# Define a function named absolute_file_path that takes a parameter 'path_fname'.
print("Solution 1: using os module")
def absolute_file_path(path_fname):
    # Import the 'os' module for working with file paths and directories.
    import os
    
    # Use 'os.path.abspath()' to get the absolute file path by providing 'path_fname'.
    return os.path.abspath(path_fname)

# Call the function and print the result, passing "test.txt" as the argument.
print(f"Absolute file path: {absolute_file_path("test.txt")}")



# Solution 2
print("Solution 1: using pathlib from Path module")
# Import the 'Path' class from the 'pathlib' module, which provides an object-oriented interface to file system paths.
from pathlib import Path

# Create a Path object 'p' by providing the file path "main.py" and resolving it to its absolute path.
p = Path("main.py").resolve()

# Print the absolute path of the file.
print(f"Absolute file path: {p}")