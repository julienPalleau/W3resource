# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
116. Print Unicode Characters

Write a Python program to print Unicode characters.
"""

# Create a Unicode string by specifying each character's Unicode escape sequence.
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'

# Print a blank line for separation.
print()

# Print the Unicode string, which will be displayed as "Python Exercises - w3resource".
print(str)

# Print another blank line for separation.
print()

print(u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065')

print()

extra_symbols_string = str.encode("utf-8")
print(extra_symbols_string)


print(str.encode("utf-8").decode("utf-8"))
