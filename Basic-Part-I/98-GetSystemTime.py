# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
98. Get System Time

Write a Python program to get system time.

Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.
"""
# W3resource 
# Sotion 1:
# Import the 'time' module to work with time-related functions.
import time

# Print an empty line for formatting.
print()

# Get and print the current time using 'time.ctime()'.
print(time.ctime())

# Print an empty line for formatting.
print()


# W3resource 
# Sotion 2:
import datetime
print(datetime.datetime.now())