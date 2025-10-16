# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
49-DirectoryFilesLister.py

Write a Python program to list all files in a directory.
"""

# Flash Qwant
# Méthode 1 : Utilisation de os.listdir et récursion

import os

# Solution 1
print("Solution 1: Utilisation de os.listdir()")
def list_files(directory_path):
    files = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            files.append(item_path)
    return files

directory_path = './'
print(list_files(directory_path))


# Solution 2
import os

print()
print("Solution2: Utilisation de os.scandir()")

def list_files(directory_path):
    files = []
    with os.scandir(directory_path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.path)
    return files

# Exemple d'utilisation
directory_path = '.'  # Répertoire courant
files = list_files(directory_path)
for file in files:
    print(file)

# Solution 3
from pathlib import Path
import os
 
print()
print("Solution3: Utilisation de pathlib.Path()")

def list_files(directory):
    path = Path(os.getcwd()) # or Path('./')
    return [file for file in path.iterdir() if file.is_file()]

print(list_files('Basic-Part-I'))

# Solution 4
import glob

print()
print("Solution4: Utilisation de glob.glob()")

def list_files(directory_path):
    return glob.glob(os.path.join(directory_path, '*'))

directory_path = '.'
files = list_files(directory_path)
for file in files:
    print(file)

# W3resource Solution
print()
print("W3resource Solution")
# Import necessary functions and modules from the 'os' library.
from os import listdir
from os.path import isfile, join

# Create a list 'files_list' that contains the names of files in the '/home/students' directory.
# It uses a list comprehension to filter files using 'isfile' and 'join' functions.
files_list = [f for f in listdir('./') if isfile(join('./', f))]

# Print the list of file names.
print(files_list)