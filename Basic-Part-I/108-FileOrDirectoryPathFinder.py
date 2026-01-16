# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
108. File or Directory Path Finder

Write a Python program to find the path to a file or directory when you encounter a path name.
"""
# W3resource
# Solution 1:
# Import the 'os.path' module for working with file paths.

print('W3resource Solution1: ')
import os.path
# Iterate through a list of file paths, including '__file__', the directory of '__file__', '/', and a broken link.
for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
    # Print the full path to the current files.
    print(f'Print the full path to the current File: {file}')

    # Print the name of the current file:
    print(f"File name: {os.path.basename(file)}")

    # Check if the file path is an absolute path using 'os.path.isabs()'.
    print(f'Absolute: {os.path.isabs(file)}')

    # Check if the file path points to an existing file using 'os.path.isfile()'.
    print(f'Is File? : {os.path.isfile(file)}')

    # Check if the file path points to an existing directory using 'os.path.isdir()'.
    print(f'Is Dir? : {os.path.isdir(file)}')
    
    # Check if the file path is a symbolic link using 'os.path.islink()'.
    print(f'Is Link? : {os.path.islink(file)}')

    # Check if the file path exists (regardless of its type) using 'os.path.exists()'.
    print(f'Exists? : {os.path.exists(file)}')

    # Check if the symbolic link exists using 'os.path.lexists()'.
    print('Link Exists?:', os.path.lexists(file))

    print()


# Qwant 
# Solution 2:
# https://www.qwant.com/?q=python+File+or+Directory+Path+Finder&client=ext-firefox-sb&t=web

# print()
# print("Qwant solution2: ")
# from pathlib import Path

# for file in [Path(__file__), '/', './broken_link']:
#     # Print the full path to the file
#     print(f'full path to the file {Path(file)}')
    
#     # Print the name of the current files.
#     print(f'File name: {Path(file).name}')

#     # Check if the file path is an absolute path using 'Path(file).is_absolute()'.
#     print(f'Absolute: {Path(file).is_absolute()}')

    # # Check if the file path points to an existing file using 'os.path.isfile()'.
    # print(f'Is File? : {os.path.isfile(file)}')

    # # Check if the file path points to an existing directory using 'os.path.isdir()'.
    # print(f'Is Dir? : {os.path.isdir(file)}')
    
    # # Check if the file path is a symbolic link using 'os.path.islink()'.
    # print(f'Is Link? : {os.path.islink(file)}')

    # # Check if the file path exists (regardless of its type) using 'os.path.exists()'.
    # print(f'Exists? : {os.path.exists(file)}')

    # # Check if the symbolic link exists using 'os.path.lexists()'.
    # print('Link Exists?:', os.path.lexists(file))

    # print()