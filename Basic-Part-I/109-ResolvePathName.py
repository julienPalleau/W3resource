# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
109. Resolve Path Name

Write a Python program to check if a number is positive, negative or zero.

Positive Numbers: Any number above zero is known as a positive number. 
Positive numbers are written without any signs or a '+' sign in front of them and
they are counted up from zero, i.e 1, +2, 3, +4 etc.
Negative numbers: Any number below zero is known as a negative number. 
Negative numbers are always written with a '-' sign in fron of them and they
are counted down from zero, i.e -1, -2, -3, -4 etc.
Always look at the sign in front of a number to check if it is positive or negative.
Zero, 0, is neither positive or negative.
"""
import re
num = float(input("Input a number: "))

print("the number is positive" if num > 0 else "the number is negative" if num < 0 else "the number is null")
