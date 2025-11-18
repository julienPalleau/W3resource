# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
89. Conditional Action

Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
"""
import pyinputplus as pyip

value = pyip.inputInt("Please provide an integer: ")

print("First day of a Month") if value == 1 else None