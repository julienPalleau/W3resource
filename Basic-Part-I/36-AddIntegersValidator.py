# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to add two objects if both objects are integers.
"""
def add_numbers(obj1, obj2)->int:
    return obj1 + obj2 if isinstance(obj1, int) and isinstance(obj2, int) else "Inputs must be integers!"

print(add_numbers(10, 20))     # Valid: Both inputs are integers, and it returns the sum.
print(add_numbers(10, 20.23))  # Invalid: One of the inputs is a float, so it returns an error message.
print(add_numbers('5', 6))     # Invalid: One of the inputs is a string, so it returns an error message.
print(add_numbers('5', '6'))