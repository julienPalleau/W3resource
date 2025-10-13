# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
17-NumberRangeTester.py

Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""
# Define a function named "near_thousand" that takes an integer parameter "n"
def near_thousand(n: int) -> bool:
    # Check if the absolute difference between 1000 and n is less than or equal to 100
    # OR check if the absolute difference between 2000 and n is less than or equal to 100
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

# Call the "near_thousand" function with the argument 1000 and print the result
print(near_thousand(1000))

# Call the "near_thousand" function with the argument 900 and print the result
print(near_thousand(900))

# Call the "near_thousand" function with the argument 800 and print the result
print(near_thousand(800))

# Call the "near_thousand" function with the argument 2200 and print the result
print(near_thousand(2200))
