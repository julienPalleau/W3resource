# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
10-NumberExpansionCalculator.py

Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""
a = int(input("input an integer: "))
n1 = int(f"{a}")
n2 = int(f"{a}{a}")
n3 = int(f"{a}{a}{a}")
print(n1 + n2 + n3)