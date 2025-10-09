# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
NOT WORKING ON WINDOWS!
Write a Python program to get the height and width of the console window.
"""

# Import necessary modules for working with the terminal size.
import fcntl
import termios
import struct

# Define a function named 'terminal_size' to retrieve the terminal size.
def terminal_size():
    # Use 'fcntl' and 'termios' to fetch terminal-related information, including size.
    # This code queries the terminal's width (columns) and height (rows).
    # It uses the 'TIOCGWINSZ' ioctl command to get window size information.

    # 1. Open file descriptor 0 (stdin).
    # 2. Call 'fcntl.ioctl' with 'TIOCGWINSZ' to fetch window size information.
    # 3. Unpack the received information into 'th' (height), 'tw' (width), 'hp' (horizontal pixel size), and 'wp' (vertical pixel size).
    th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))

    # Return the terminal width and height.
    return tw, th

# Call the 'terminal_size' function to get the terminal size and print the result.
print('Number of columns and Rows: ', terminal_size())