# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to check whether a file exists.
"""

from pathlib import Path

# File path
a = Path("Basic-Part-I/myfile41.txt")

# Check if the file exists
if a.exists():
    print("File exists")
else:
    print("File does not exist")