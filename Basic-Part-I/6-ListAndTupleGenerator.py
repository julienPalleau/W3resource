# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
6.ListAndTupleGenerator.py

Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
my_list = input("Provide a sequence of comma-separated numbers: ").split(",")
print(my_list)
print(tuple(my_list))
