# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
33-TripleSumEqualityRule.py

Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""
def sum_three_integers(value1: int, value2: int, value3: int)->int:
    return 0 if value1==value2 or value1==value3 or value2==value3 else value1 + value2 + value3

print(sum_three_integers(2,1,2))
print(sum_three_integers(3,2,2))
print(sum_three_integers(2,2,2))
print(sum_three_integers(1,2,3))        