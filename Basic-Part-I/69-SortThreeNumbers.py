# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to sort three integers without using conditional statements and loops.
"""
# ma solution
import pyinputplus as pyip
print("ma solution")
numbers=[]
def sortThreeNumbers():
    print("Write a Python program to sort three integers without using conditional statements and loops.")
    numbers = [pyip.inputInt('Entrez un premier entier: ') for i in range(3)]
    
    numbers.sort()
    return numbers

print(sortThreeNumbers())

# W3resource
print("W3 resource")

# Prompt the user to input three integers and convert them to variables x, y, and z.
x = pyip.inputInt("Input first number: ")
y = pyip.inputInt("Input first number: ")
z = pyip.inputInt("Input first number: ")

# Find the minimum value among x, y and z and store it in variable a1.
a1 = min(x, y, z)

# Find the maximum value among x, y, and z and store it in variable a3.
a3 = max(x, y, z)

# Calculate the middle value (not the minimum or maximum) by subtracting a1 and a3 from the sum of x, y and z.
a2 = (x + y + z) - a1 - a3

# Print the numbers in sorted order (a1, a2, a3)
print(f"Numbers in sorted order: {a1}, {a2}, {a3}")