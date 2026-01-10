# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
103. Extract Filename

Write a Python program to extract the filename from a given path.
"""
# Solution 1 using os.path
import os
print("Solution 1 using os.path")
file_path = r"C:\Users\jpall\Documents\GitHub\W3resource\Basic-Part-I\103-ExtractFilename.py"
file_name = os.path.basename(file_path)
print(file_name)

# Solution 2 using os.path
print()
print("Solution 2 using os.path")
file_path = r"C:\Users\jpall\Documents\GitHub\W3resource\Basic-Part-I\103-ExtractFilename.py"
file_name = os.path.split(file_path)[1]
print(file_name)

# Solution 3 using pathlib
print()
from pathlib import Path
print("Solution 3 using pathlib")
file_path = Path(r"C:\Users\jpall\Documents\GitHub\W3resource\Basic-Part-I\103-ExtractFilename.py")
file_name = file_path.name
print(file_name)