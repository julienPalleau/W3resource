# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
"""
def sum_thrice(x: int, y: int, z:int ):
    return 3*(x+y+z) if x==y==z else x+y+z

print(sum_thrice(1, 1, 1))
print(sum_thrice(1, 2, 3))