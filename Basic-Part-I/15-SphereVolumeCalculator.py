# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to get the volume of a sphere with radius six.
"""
from math import pi
import pyinputplus as pyip

# old input solution
r = float(input("Entrer le rayon de votre sphere: "))
print(f"Le volume de la sphere est de: {(4/3) * pi * r**3}")

# new input with no need to cast
s = pyip.inputInt("Entrer le rayon de votre sphere: ")
print(f"Le volume de la sphere est de: {(4/3) * pi * s**3}")