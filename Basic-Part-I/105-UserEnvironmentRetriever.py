# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
105. User Environment Retriever

Write a Python program to get the users environment.
"""
# Solution 1
import os

print("Solution 1:")
path = os.environ["PATH"]
db_host = os.getenv('HOSTNAME')
db_user = os.environ.get('DB_USER', 'user_name_set_by_this_pgm') # we set DB_USER with default_user 
username = os.getlogin()

print(f"path: {path}")
print(f"host: {db_host}")
print(f"user: {db_user}")
print(f"username: {username}")

print(os.getenv)

# All os methods: https://www.w3schools.com/python/module_os.asp

# W3resource 
# Solution 2

#  Import the 'os' module for operating system-related functions.
# import is made at the begining of this file

# Import the 'pprint' module for pretty-printing data structures.
print()
print("Solution 2:")
import pprint

# Access and store the user's environment variables.
u_env_var = os.environ

# Print a message indicating the user's environment variables.
print("User's Environment variable:")

# Pretty-print the environment variable in a more readable format.
# pprint.pprint(dict(u_env_var), width=1)