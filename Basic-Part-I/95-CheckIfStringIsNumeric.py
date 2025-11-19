# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
95. Check if String is Numeric

Write a Python program to check whether a string is numeric.
"""
# W3resource 
# Sotion 1:

# Define a string named str containing the value 'a123'.
str = 'a123'

# Uncomment the line below to test a different string (e.g., '123').
# str = '123'

# Try to convert the string str to a float.
try:
    i = float(str)
except (ValueError, TypeError):
    # If a ValueError or TypeError occurs during conversion, print 'Not numeric.'
    print('\nNot numeric')

# Print a newline character to format the output.
print()


# W3resource 
# Sotion 2:

# Doesn't work for floats
# Prompt the user for input and store it in the 'text' variable.
text = input("Input a word or numbers: ")

# Check if the input consists of digits only using the 'isdigit' method.
if text.isdigit():
    # If the input contains only digits, print "The input value is numbers."
    print("The input value is numbers.")
else:
    # If the input contains characters other than digits, print "The input value is string."
    print("The input value is string.")