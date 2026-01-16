# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
110.Divisible by 15 Finder

Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
"""
numbers = [1, 15, 35, 40, 60, 90, 102]
number = list(filter(lambda x: x % 15 == 0 , numbers))
print(number)