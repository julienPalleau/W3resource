# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
77-EndianessChecker.py

Write a Python program to test whether the system is a big-endian platform or a little-endian platform.

sys.byteorder: An indicator of the native byte order. This will have the value 'big' on big-endian 
(most-significant byte first) platforms, and 'little' on little-endian (least-significant byte first) platforms.
"""
# Import the sys module to access system-specific information.
import sys

# Display a blank line for clarity.
print()

# Check if the byte order of the platform is "little" (e.g., Intel, Alpha) and display a corresponding message.
if sys.byteorder == "little":
    print("Little-endian platform.")
else:
    # If the byte order is not "little," assume it's "big" (e.g., Motorola, SPARC) and display a corresponding message.
    print("Big-endian platform.")

# Display another blank line for clarity.
print()