# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
59-HeightToCentimeters.py

Write a Python program to convert height (in feet and inches) to centimeters.
"""
import pyinputplus as pyip

# Prompt the user to input their height.
print("Input your height")

# Read the feet part of the height and convert it to an integer.
h_ft = pyip.inputInt("Feet: ")

# Read the inches part of the height and convert it to an integer.
h_inch = pyip.inputInt("Inches: ")

# Convert the height from feet and inches to inches.
h_inch += h_ft * 12

# Calculate the height in centimeters by multiplying by the conversion factor (2.54).
h_cm = round(h_inch *2.54, 1)

# Print the calculated height in centimeters.
print(f"Your height is {int(h_cm)} cm")
    
