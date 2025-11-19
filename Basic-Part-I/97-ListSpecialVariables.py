# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
97. List Special Variables

Write a Python program to list the special variables used in the language.
"""

# Import the necessary modules.

# Create a set 's_var_names' containing unique variable names in the global namespace.
s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))

# Print an empty line for formatting.
print()

# Join variable names in groups of 8 and print them for better readability.
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )

# Print an empty line for formatting.
print()