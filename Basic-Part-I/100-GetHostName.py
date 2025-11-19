# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
100. Get Host Name

Write a Python program to get the name of the host on which the routine is running.
"""
# W3resource 
# Sotion 1:
# Import the 'socket' module to work with networking functionalities.

import socket
# Use 'socket.gethostname()' to retrieve the name of the current host or machine.
host_name = socket.gethostname()

# Print the host name to the console.
print("Host name:", host_name)


# W3resource 
# Sotion 2:
# Import the 'platform' module to retrieve system-related information.
import platform
# Use 'platform.uname()' to obtain a tuple of information about the system, including the host name.
host_name = platform.uname()[1]

# Print the host name to the console.
print("Host name:", host_name)


# W3resource (specific to linux)
# Sotion 2:
# Import the 'os' module to access operating system-related functionality.
import os, sys

if sys.platform == 'linux':
    # Use 'os.uname().nodename' to retrieve the host name of the current system.
    host_name = os.uname().nodename
    # Print the host name to the console.
    print("Host name:", host_name)