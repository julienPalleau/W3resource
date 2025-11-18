# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
93. Object Identity and Type

Write a Python program to get the Identity, Type, and Value of an object.
"""
# W3resource 
# Sotion 1:
# Define a variable 'x' and assign the value 34 to it.
print("Solution 1:")
x = 34

# Print the variable name.
print(f"Variable name and assigned value: {x = }")

# Print the identity of the variable 'x'.
print("Identity: ", x)

# Print the data type of the variable 'x'.
print("Type: ", type(x))

# Print the memory address (value) of the variable 'x'.
print("Memory adress of x: ", id(x))


# W3resource 
# Solution 2:
# Check whether two objects are the same!
# Define two variables 'a' and 'b' with some values.
print("\nSolution 2: ")
a = 34
b = 33
# Print the values of 'a' and 'b'.
print(f"{a = }")
print(f"{b = }")
# Define another variable 'c' and assign the value of 'a' to it.
print(f'c = {a = }')
c = a
# Compare the values of 'a' and 'b' for identity.
print("Compare a and b:")
print(a is b)
# Print the memory address of variable 'a'.
print("\nMemory address of a:")
print(id(a))
# Print the memory address of variable 'b'.
print("Memory address of b:")
print(id(b))
print("Memory address of c:")
print(id(c))
# Compare the memory addresses of 'a' and 'b'.
print("\nCompare the said memory address of 'a' and 'b':")
print(id(a) == id(b))
# Compare the memory addresses of 'a' and 'c'.
print("Compare the said memory address of 'a' and 'c':")
print(id(a) == id(c))
# Compare the values of 'a' and 'c' for identity.
print("\nCompare a and c:")
print(a is c)
# Compare the values of 'a' and 'c' for identity.
print("Compare b and c:")
print(b is c)
