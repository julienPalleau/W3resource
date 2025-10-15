# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
34-ConditionalSumTo20.py

Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""
def check_age(value1: int, value2: int)->int:
    match value1, value2:
        case value1, value2 if 15 < value1 + value2 < 20:
            return 20
        case _:
            return value1 + value2

print(check_age(15, 3))
print(check_age(2, 3))

