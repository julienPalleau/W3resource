# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
60-TriangleHypotenuseCalculator.py

Write a Python program to calculate the hypotenuse of a right angled triangle.
"""
import pyinputplus as pyip

base = pyip.inputFloat("Veuillez saisir la base du triangle:")
hauteur = pyip.inputFloat("Veuillez saisir la hauteur du triangle:")
print(f"L'hypothenuse du triangle est: {(base**2+hauteur**2)**(1/2)}")