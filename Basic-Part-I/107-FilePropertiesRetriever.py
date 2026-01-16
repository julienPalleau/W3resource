# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
107. File Properties Retriever

Why a Python program to retrieve file properties.
"""
# W3resource
# Solution 1:
# Import the 'os.path' and 'time' modules for working with file paths and time-related functions.
# import os.path

# Iterate through a list of example file paths.
# for path in ['myfile1.txt', 'myfile2.txt', 'myfile3.txt', '/Users/jpall/Documents/GitHub/W3resource/Basic-Part-I', '/', '']:
#     # Print the file path and its corresponding file extension using 'os.path.splitext().'
#     print(f"{path} {os.path.splitext(path)}")


# Qwant 
# Solution 2:
# https://www.qwant.com/?client=ext-firefox-sb&q=python+files+properties+retriever&t=web
import os
import os.path
import time
import stat

print("En Utilisant la bibliothèque os")
# Chemin du fichier
file_path = '/Users/jpall/Documents/GitHub/W3resource/Basic-Part-I/myfile1.txt'

# Nom du fichier
print(f'File name: {os.path.basename(file_path)}')

# Chemin absolu du fichier
print(f'Absolute path:, {os.path.abspath(file_path)}')

# Taille du fichier en octets
print(f'File size {os.path.getsize(file_path)}, bytes')

# Date de la dernière modification
mod_time = os.path.getmtime(file_path)
print(f'Last modified : {time.ctime(mod_time)}')

# Date de dernière accès
access_time = os.path.getatime(file_path)
print('Last access:', time.ctime(access_time))

# Date de création (windows uniquement)
if os.name == 'nt':
    creation_time = os.path.getctime(file_path)
    print(f'Creation time {time.ctime(creation_time)}')



# Récupération des attributs de fichier
file_stats = os.stat(file_path)

# Vérification des attributs
print(f'Read-only: {bool(file_stats.st_mode & stat.S_IREAD)}')
print(f'Hidden: {bool(file_stats.st_mode & stat.UF_HIDDEN)}')



# Utilisation de la bibliothèque pathlib
from pathlib import Path
import datetime

# Propriété du fichier
print()
print("En utilisant la bibliothèque pathlib")
file_path = Path('/Users/jpall/Documents/GitHub/W3resource/Basic-Part-I/myfile1.txt')
print(f'File name: {file_path.name}')
print(f'Absolute path: {file_path.absolute()}')
print(f'File size: {file_path.stat().st_size}, bytes')
print(f'Last modified: {datetime.datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")}')
print(f'Last access: {datetime.datetime.fromtimestamp(file_path.stat().st_atime).strftime("%Y-%m-%d %H:%M:%S")}')
print(f'Creation time: {datetime.datetime.fromtimestamp(file_path.stat().st_ctime).strftime("%Y-%m-%d %H:%M:%S")}')
