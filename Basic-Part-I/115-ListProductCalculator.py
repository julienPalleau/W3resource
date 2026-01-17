# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
115. List Product Calculator

Write a Python program to compute the product of a list of integers (without using a for loop).
"""
import functools
import operator

numbers = [1, 2, 3, 4, 5]
print(functools.reduce(operator.mul, numbers))
