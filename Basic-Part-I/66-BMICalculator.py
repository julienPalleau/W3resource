# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to calculate the body mass index.
"""
import pyinputplus as pyip
def bmi():
    weight = pyip.inputFloat('Veuillez saisir votre poid: ')
    height = pyip.inputFloat('Veuillez saisir votre taille: ')
    return weight/height**2

print(f"Your body mass index is: {bmi()}")