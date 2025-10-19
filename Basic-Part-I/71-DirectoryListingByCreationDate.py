# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
71-DirectoryListingByCreationDate.py

Write a Python program to get a directory listing, sorted by creation date.
"""

# Solution 1
# Import necessary modules: 'stat' for file status, 'os' for operating system interactions,
# 'sys' for command-line arguments, and 'time' for time-related functions.
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

print("Solution 1: ")
# Determine the directory path based on command-line arguments. If there are two arguments, use the second one as the path;
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

# Generate a generator expression that yields the full path for eaach file in the specified directory.
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))

# Generate a generator expression that pairs the file's status information and its path.
data = ((os.stat(path), path) for path in data)

# Filter the files to keep only regular files (S_ISREG) and extract their creation times (ST_CTIME).
data = ((stat[ST_CTIME], path) for stat, path in data if S_ISREG(stat[ST_MODE]))

# Sort the files based on their creation times and then pring the sorted list, including the creation time and the file name.
for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))


# Solution 2
# Import the required modules: 'os' for operating system interactions and 'time' for time-related functions.
# Import the required modules: 'os' for operating system interactions and 'time' for time-related functions.
import os
import time

print()
print("Solution 2:")
# Create a list 'paths' by iterating through files in the current directory and formatting their creation time and file name.
# The list comprehension generates tuples with the creation time and file name for each file.
paths = ["%s %s" % (time.ctime(t), f) for t, f in sorted([(os.path.getctime(x), x) for x in os.listdir(".")])]

# Print a header for the directory listing.
print("Directory listing, sorted by creation date:")

# Iterate through the list 'paths' and print each entry.
for x in range(len(paths)):
    print(paths[x],)
