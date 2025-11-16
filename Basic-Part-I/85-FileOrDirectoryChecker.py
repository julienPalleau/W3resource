# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
85. File or Directory Checker

Write a Python program to check whether a file path is a file or a directory.
"""
# Solution 1 with os
import os
path = "Basic-Part-I"

print("Solution 1 using os:")
if os.path.isfile(path):
    print("Il s'agit d'un fichier.")
elif os.path.isdir(path):
    print("Il s'agit d'un répertoire.")
else:
    print("Le chemin n'existe pas ou n'est ni un fichier ni un répertoire.")

# Solution 2 with pathlib
from pathlib import Path

path = Path("Basic-Part-I/myfile1.txt")

print("\nSolution 2 using path:")
if path.is_file():
    print("Il s'agit d'un fichier.")
elif path.is_dir():
    print("Il s'agit d'un répertoire.")
else:
    print("Le chemin n'existe pas ou n'est ni un fichier ni un répertoire.")