# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to get the volume of a sphere with radius six.
"""
from math import pi
r = float(input("Entrer le rayon de votre sphere: "))
print(f"Le volume de la sphere est de: {(4/3) * pi * r**3}")