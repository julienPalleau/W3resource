# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to find out what version of Python you are using.

Python Version Checker

Write a Python program to find out what version of Python you are using.

A string containing the version number of the Python interpreter plus additional information on the build number and compiler used. This string is displayed when the interactive interpreter is started.

Version info:

A tuple containing the five components of the version number: major, minor, micro, releaselevel, and serial. All values except releaselevel are integers; the release level is 'alpha', 'beta', 'candidate', or 'final'. The version_info value corresponding to the Python version 2.0 is (2, 0, 0, 'final', 0). The components can also be accessed by name, so sys.version_info[0] is equivalent to sys.version_info.major and so on.

Note : 'sys' module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

"""

# Solution 1
"""
Explanation:

The said code imports the "sys" module and then uses it to print the version of Python currently being used, 
as well as additional version information.

    The first line imports the "sys" module provides access to some variables used or maintained by the interpreter and to functions 
    that interact strongly with the interpreter. It is always available.
    The second line prints the string "Python version".
    The third line prints the version of Python currently being used to the console.
    The fourth line prints the string "Version info.".
    The fifth line prints version information of the current Python interpreter. 
    It returns a named tuple (version_info) containing the five components of the version number: 
    major, minor, micro, releaselevel, and serial.

"""
print("Solution 1:")
import sys  # Import the sys module to access system-specific parameters and functions

# Print the Python version to the console
print("Python version:")

# Use the sys.version attribute to get the Python version and print it
print(sys.version)

# Print information about the Python version
print("\nVersion info:")

# Use the sys.version_info attribute to get detailed version information and print it
print(sys.version_info)


# Solution 2
"""
Explanation:

The said code imports the platform module and then uses it to print the version of Python currently being used.

    The first line import platform imports the platform module, which provides various services that interact with the host platform.
    The second line print(platform.python_version()) uses the python_version() function from the platform module 
    to get the version of Python currently being used and prints it to the console.

This is a simpler and more efficient way to get the version of python that you are running, as it does not need 
to import any other modules like sys.

Output:

3.10.6
"""
print("\n\nSolution 2.1:")
import platform
print(platform.python_version())


"""
Explanation:

The said code imports the platform module and then uses it to print the version of Python currently being used as a tuple.

    The first line import platform imports the platform module, which provides various services 
    that interact with the host platform.
    The second line print(platform.python_version_tuple()) uses the python_version_tuple() 
    function from the platform module to get the version of Python currently being used as a tuple 
    of integers (major, minor, micro) and prints it to the console.

This is a way to get the version of python that you are running in a more structured way, as it 
provides the version details in the form of a tuple. For example, if the python version is 3.8.7, 
the function will return (3,8,7) as a tuple.
"""
print("Solution 2.2:")
import platform
print(platform.python_version_tuple())