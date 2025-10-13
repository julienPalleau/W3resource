# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
20-StringCopyGenerator.py

Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
"""
def repeat(n: int, phrase: str) -> str:
    return phrase*n

print(repeat(2, 'julien'))