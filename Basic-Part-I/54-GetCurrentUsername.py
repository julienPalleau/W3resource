# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
54-GetCurrentUsername.py

Write a Python program to get the current username.
"""
import os

print('w3resource Solution1:')
print(os.environ['USERNAME'])

print()
import getpass
print('w3resource Solution2')
print(getpass.getuser())

"""
Explanation:

The above Python code imports the ‘getpass’ module and uses it to print the username of the current user to the console output.

The ‘getpass’ module provides a way to get the username of the current user, 
as well as prompt the user to enter a password without echoing the input to the console.

getpass.getuser() - This function checks the environment variables LOGNAME, USER, LNAME and USERNAME, 
in order, and returns the value of the first one which is set to a non-empty string. If none are set, 
the login name from the password database is returned on systems which support the pwd module, otherwise, an exception is raised.

The output of the code will be the username of the current user, which is retrieved from the operating system.
"""