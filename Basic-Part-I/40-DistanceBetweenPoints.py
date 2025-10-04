# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""
# Import the math module to use the square root function.
import math

# Ma Solution
print(math.dist([4, 0], [6, 6]))

# W3resource Solution

# Define the coordinates of the first point (p1) as a list.
p1 = [4, 0]

# Define the coordinates of the second point (p2) as a list.
p2 = [6, 6]

# Calculate the distance between the two points using the distance formula.
# The formula computes the Euclidian distance in 2D space.
distance = math.sqrt(((p1[0] - p2[0])**2 + ((p1[1] - p2[1])**2)))

# Pprint the calculated distance.
print(distance)