# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
"""
# My Solution
first_name = input("Enter your first name and last name with a space between them: ").split(" ")
print(f"Hello {first_name[1]} {first_name[0]}")

# w3resource Solution
# Prompt the user to input their first name and store it in the 'fname' variable
fname = input("Input your First Name : ")

# Prompt the user to input their last name and store it in the 'lname' variable
lname = input("Input your Last Name : ")

# Display a greeting message with the last name followed by the first name
print("Hello  " + lname + " " + fname)