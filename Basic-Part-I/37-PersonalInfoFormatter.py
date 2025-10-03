# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that displays your name, age, and address on three different lines.
"""
def personal_details():
    # Define variables 'name' and 'age' and assign values to them.
    name, age = "Simon", 19

    # Define a variable 'address' and assign a value to it.
    address = "California , San Francisco, United States Of America"

    # Print the personal details using string formatting.
    print(f"Name: {name}\nAge: {age}\nAddress: {address}")

personal_details()