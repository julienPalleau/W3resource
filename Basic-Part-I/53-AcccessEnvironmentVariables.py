# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to access environment variables.
"""
# Import the 'os' module to access operating system-related functionality, including environment variables.
import os

print(os.system('cls'))

# W3resource Solution-1:
print("# W3resource Solution-1:")

# Print a separator for clarity.
print('*----------------------------------*')

# Print all environment variables.
print(f"environment: {os.environ}")

# Print a separator for clarity.
print('*----------------------------------*')

# Access and print the 'HOME' environment variable.
print(f"username: {os.environ['USERNAME']}")

# Print a separator for clarity.
print('*----------------------------------*')

# Access and print the 'PATH' environment variable.
print(f"windows directory: {os.environ['WINDIR']}")

# Print a separator for clarity.
print('*----------------------------------*')


# W3resource Solution-2:
print()
print("# W3resource Solution-2:")
# Import the 'os' module to access operating system-related functionality, including environment variables.
import os

# Iterate through all environment variables in the 'os.environ' dictionary.
for data in os.environ:
    # Print the name of the environment variable.
    print(data)
    # Print a separator for clarity.
    print('-' * 15)
    # Print the value of the environment variable.
    print(os.environ[data])
    # Print a line of '=' characters as an additional separator.
    print('=' * 30)