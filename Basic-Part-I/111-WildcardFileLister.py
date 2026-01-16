# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
111.Wilcard File Lister

Write a Python program to make file lists from the current directory using a wildcard.
"""
# W3resource
# Solution 1
import glob
print("W3resource solution 1:")

# Use the glob module to get a list of all files in the current directory
file_list = glob.glob('*.*')

# Print the list of all files in the current directory
print(f'Liste de tous les fichiers: {file_list}')

# Specific files
# Use a wildcard pattern to search for python (.py) files in the current directory
print(f"Liste des fichiers Python (.py): {glob.glob('*.py')}")

# Use a more specific pattern to search for files with names starting with a digit and any extension
print(f"Liste des fichiers commençant par un chiffre: {glob.glob('./[0-9].*')}")

# Qwant
# Solution 2
import glob
from pathlib import Path

print()
print("Qwant solution 2:")

def list_files_with_wildcard(pattern):
    """
    Liste les fichiers du répertoire courant correspondant à un motif avec caractères génériques.
    
    :param pattern: Motif de recherche avec caractère génériques (ex: '*.txt', 'data_*.csv')
    """
    # Utilisation de glob pour obtenir la liste des fichiers
    file_list = glob.glob(pattern)
    print(f"Fichiers correspondant au motif '{pattern}':")
    for file in file_list:
        print(file)

    # Utilisation de pathlib pour une approche alternative
    print("\nApproche avec pathlib:")
    for path in Path('.').glob(pattern):
        print(path)

# Exemples d'utilisation
if __name__ == "__main__":
    print("Liste de tous les fichiers:")
    list_files_with_wildcard('*.*')

    print("\nListe des fichiers Python (.py):")
    list_files_with_wildcard('*.py')

    print("\Liste des fichiers commençant par un chiffre:")
    list_files_with_wildcard('[0-9]*.*')
