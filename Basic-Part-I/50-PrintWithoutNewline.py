# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to print without a newline or space.
"""

# W3resource 
# Solution 1
# Iterate through a range of numbers from 0 to 9 (inclusive).
print("Solution 1: Iteratation.")
for i in range(0, 10):
    # Print an asterisk '*' character on the same line using the 'end' parameter.
    print('*', end="")
# Print a newline character to move to the next line.
print("\n")

# Solution 2
print("Solution 2: functools.")
# Import the functools module to use the 'partial' function.
import functools

# Create a partial function 'printf' based on the 'print' function with 'end' parameter set to an empty string.
printf = functools.partial(print, end="")

# Iterate through a range of numbers from 0 to 9 (inclusive).
for _ in range(0, 10):
    # Use the 'printf' function to print an asterisk '*' character to the same line.
    printf('*')

# Solution 3
print()
print()
print("Solution 3: Loo[]")
# Initialize the variable 'i' with the value 0.
i = 0

# Start a while loop that continues as long as 'i' is less than 10.
while i < 10:
    # Print an asterisk '*' to the same line without moving to the next line.
    print('*', end='')

    # Increment the value of 'i' by 1 in each iteration.
    i = i + 1

