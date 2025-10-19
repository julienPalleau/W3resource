# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
70-SortFilesByDate.py

Write a Python program to sort files by date.
"""
# W3resource
# Solution 1
# Import the necessary libraries to work with file operations and globbing.
import glob
import os
from pathlib import Path
import pathlib

print("Solution 1")
# # Change the current working directory to 'Basic-Part-I'
# os.chdir('Basic-Part-I')

# # Use the glob module to find all files in the current directory with a ".txt" extension.
# files = glob.glob("*.txt")

files = pathlib.Path('Basic-Part-I').glob('*.txt')
print('\n'.join(str(file) for file in files))
print()
files = pathlib.Path('.').glob('*/*.txt')
print('\n'.join(str(file) for file in files))

# # Sort the list of file names based on the modification time (getmtime) of each file.
# files.sort(key=os.path.getmtime)

# # Print the sorted list of file names, one per line.
# print("\n".join(files))

# current_directory = Path.cwd()
# print(current_directory)


# Solution 2
print("\nSolution 2")
# Import the 'os' module for interacting with the operating system.

# Change the current working directory to 'Basic-Part-I'
os.chdir('Basic-Part-I')

# List files in the current directory, filter for .txt files (not directories).
file_list = filter(os.path.isfile, [file for file in os.listdir('.') if file.endswith('.txt')])

# Sort the list of files based on their modification time.
sorted_files = sorted(file_list, key=os.path.getmtime)

# Print the sorted list of file names, one per line.
print('\n'.join(map(str, sorted_files)))