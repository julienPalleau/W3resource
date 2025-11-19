# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
94. String Bytes to Integers

Write a Python program to convert the bytes in a given string to a list of integers.
"""

# W3resource 
# Sotion 1:
# Create a bytes object containing the bytes 'Abc'.
# Write a Python program to convert the bytes in a given string to a list of integers.

x = b'Abc'

# Print an empty line for clarity.
print()

# Convert the bytes of the said string to a list of integers and print the result.
print("Convert bytes of the said string to a list of integers:")
print(list(x))

# Print an empty line for clarity.
print()


# W3resource 
# Solution 2:

# Define a string named S.
S = "The quick brown fox jumps over the lazy dog."

# Print a message indicating the original string.
print("Original string:")

# Print the original string.
print(S)

# Create an empty list named nums.
nums = []

# Print a message to indicate the conversion of bytes to a list of integers.
print("\nConvert bytes of the said string to a list of integers:")

# Iterate through each character (byte) in the string S and append its ASCII value to the nums list.
for chr in S:
    nums.append(ord(chr))

# Print the list of integers.
print(nums)

print(list(b'The quick brown fox jumps over the lazy dog.'))