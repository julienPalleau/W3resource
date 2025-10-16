# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
58-SumOfFirstnPositives.py

Write a Python program to sum the first n positive integers.
"""
import pyinputplus as pyip
# Prompt the user for input and convert it to an integer.

n = pyip.inputInt("Input a number: ")
print(f"Sum of the first {n} positive integers: {(n*(n+1))/2}")