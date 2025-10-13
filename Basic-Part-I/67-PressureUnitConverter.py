# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
"""
import pyinputplus as pyip
def convert1():
    kPa = pyip.inputFloat("Veuillez saisir une pression en kilopascals: ")
    mmHg = pyip.inputFloat("Veuillez saisir une pression en millimètre de mercure: ")
    return f"{round(kPa * 0.14503773800722, 3)} psi\n{round(mmHg * 0.0013158, 3)} atmp"

print(convert1())