# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""
def equation(x: int, y: int)->int:
    return (x + y)**2

print(equation(4, 3))