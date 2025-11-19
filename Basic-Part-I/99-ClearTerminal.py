# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
99. Clear Terminal

Write a Python program to clear the screen or terminal.
"""
# Import the 'os' and 'time' modules to work with system commands and time-related functions, respectively.

import os
import time

# Execute the 'ls' command to list the contents of the current directory.
os.system("dir")

# Pause the program's execution for 2 seconds.
time.sleep(2)

# Clear the terminal screen. (This comment is not entirely accurate; 'os.system('clear')' is used to clear the terminal screen.)
os.system('cls')