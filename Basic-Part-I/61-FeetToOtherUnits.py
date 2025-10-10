# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
"""
import pyinputplus as pyip

def convert()->float:
    feets=pyip.inputFloat("Please provide a distance in feet: ")
    inches = feets * 12
    yards = feets / 3
    miles = feets / 5280
    return(feets, inches, yards, miles)

feets, inches, yards, miles = convert()
print(f"{feets} feets is equal to {inches} inches, {yards} yards, {miles} miles")