# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
73-LineMidpointCalculator.py

Write a Python program to calculate the midpoints of a line.
"""

class LineMidPointCalculator:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def midpoint(self):
        return (((self.x2 + self.x1)/2), ((self.y2 + self.y1)/2))
    

linepointcalculator = LineMidPointCalculator(2,2,4,4)
print(linepointcalculator.midpoint())