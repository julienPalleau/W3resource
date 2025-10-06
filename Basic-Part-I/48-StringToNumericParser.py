# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to parse a string to float or integer.
"""

# Ma Solution
print('Ma Solution')
def parse_string_to_float_or_integer(value: str)->float|int:
    return float(value) if "." in value else int(value)

print(parse_string_to_float_or_integer('12'))
print(parse_string_to_float_or_integer('233.12'))

# W3resource Solution
# Define a function 'test' that takes a string 's' as input.
print()
print('W3resource Solution')
def test(s):
    try:
        # try to convert the input string to an integer.
        return int(s)
    except ValueError:
        # If the conversion to an integer raises a ValueError (i.e., it's not an integer),
        # then try to convert the string to a floating-point number (float).
        return float(s)
    
# Call the 'test' function with different input values and print the results.
print(test('12')) # Try to convert '12' to an integer.
print(test('233.12')) # Try to convert '233.12' to a float.
