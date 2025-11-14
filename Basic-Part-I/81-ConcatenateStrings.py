# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
81. Concatenate Strings

Write a Python program to concatenate N strings.
"""
def concatenate_string(*args):
    result = "-".join(args)
    return result

print(concatenate_string('Red', 'White', 'Black'))