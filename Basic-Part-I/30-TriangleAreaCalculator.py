# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that will accept the base and height of a triangle and compute its area.
"""
def triangle_area(base:float, height:float)->float:
    return (0.5)*base*height

print(triangle_area(20, 40))