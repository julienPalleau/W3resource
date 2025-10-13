# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
21-EvenOrOddChecker.py

Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
and prints an appropriate message to the user.
"""
def evenOrOdd(n: int) -> str :
    return "number is even" if n % 2 == 0 else "Number is odd"

print(evenOrOdd(3))
print(evenOrOdd(4))