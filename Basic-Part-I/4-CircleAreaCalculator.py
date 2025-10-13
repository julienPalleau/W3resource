# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
4. CircleAreaCalculator.py

Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504

Circle Area Calculator

Write a Python program that calculates the area of a circle based on the radius entered by the user.

Python: Area of a Circle

In geometry, the area enclosed by a circle of radius r is πr2. Here the Greek letter π represents a constant, 
approximately equal to 3.14159, which is equal to the ratio of the circumference of any circle to its diameter.

Python: Area of a circle

Pre-Knowledge (Before you start!)

    Basic Python Syntax: Familiarity with writing and running Python scripts.
    User Input: Understanding how to use the input() function to take input from the user.
    Type Conversion: Knowledge of converting strings to float using float().
    Math Module: Familiarity with importing constants like pi from the math module.
    Arithmetic Operations: Understanding basic arithmetic operations, especially exponentiation (**) for squaring the radius.
    String Concatenation: Ability to concatenate strings and variables using the + operator.
    Area Formula: Knowledge of the formula for calculating the area of a circle: π * r^2.

Hints (Try before looking at the solution!)

    Import the Math Module: Start by importing the pi constant from the math module.
    Take User Input: Use the input() function to prompt the user to enter the radius of the circle.
    Convert Input to Float: Ensure the input is converted to a float so that decimal values can be handled.
    Calculate the Area: Use the formula area = pi * r ** 2 to calculate the area of the circle.
    Display the Result: Use the print() function to display the calculated area along with the radius.
        Format the output string properly by concatenating the radius and area values.
    Test with Different Values: Try entering different radius values (e.g., integers and decimals) to ensure your program works correctly.
    Common Errors to Avoid:
        Forgetting to convert the input to a float, which may result in a TypeError.
        Misplacing parentheses or operators in the formula, leading to incorrect calculations.

"""


"""
Explanation:

The said code calculates the area of a circle based on the radius entered by the user. 
The code uses the "math" module's pi constant and the "input" function to get the radius from the user, 
then it uses the formula to calculate the area of the circle.

    The first line from math import pi imports the pi constant from the math module, which is the mathematical constant. 
    It represents the ratio of a circle's circumference to its diameter (approximately equal to 3.14).
    The second line r = float(input ("Input the radius of the circle : ")) gets the radius of the circle from the user using the input() function. 
    input() function assigns it to the variable r, it's then cast to float, so the user can input decimal number also.
    The third line print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2)) 
    uses the formula to calculate the area of the circle (pi*r**2) . 
    Then it concatenates the string and the value of the radius and area using the + operator and prints the final string.

This code is useful to calculate the area of a circle when the radius is known, it can be used in physics and 
mathematical calculations or in applications that require the area of a circle to be calculated. 
"""
# Import the 'pi' constant from the 'math' module to calculate the area of a circle
from math import pi

# Prompt the user to input the radius of the circle
r = float(input("Input the radius of the circle : "))

# Calculate the area of the circle using the formula: area = π * r^2
area = pi * r ** 2

# Display the result, including the radius and calculated area
print("The area of the circle with radius " + str(r) + " is: " + str(area))

