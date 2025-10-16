# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
52-PrintToSTDERR.py

Write a Python program to print to STDERR.
"""
# Import the 'print_function' feature from the '__future__' module to enable Python 3-style print function.
from __future__ import print_function

# Import the 'sys' module, which provides access to some variables used or maintained by the interpreter.
import sys

# Define a custom 'eprint' function that prints to the standard error stream.
def eprint(*args, **kwargs):
    # Call the 'print' function with the provided arguments and keyword arguments.
    # Use 'file=sys.stderr' to print to the standard error stream (stderr).
    print(*args, file=sys.stderr, **kwargs)

# Call the 'eprint' function with the specified arguments and separator.
eprint("abc", "efg", "xyz", sep="--")

"""
Explanation:

__future__ is a real module, and serves three purposes:

    To avoid confusing existing tools that analyze import statements and expect to find the modules they’re importing.
    To ensure that future statements run under releases prior to 2.1 at least yield runtime exceptions 
    (the import of __future__ will fail, because there was no module of that name prior to 2.1).
    To document when incompatible changes were introduced, and when they will be — or were — made mandatory. 
    This is a form of executable documentation, and can be inspected programmatically via importing __future__ and examining its contents.

Sys module - This module provides access to some variables used or maintained by the interpreter and to functions 
that interact strongly with the interpreter. It is always available.

In the above Python exercise the eprint() function takes any number of arguments and prints them to the 
standard error stream (stderr) using the print() function. The file parameter is set to sys.stderr, 
which redirects the output to the standard error stream instead of the standard output stream.

Finally, the eprint() function is called with the arguments "abc", "efg", and "xyz", separated by the string "--". 
This causes the string "abc--efg--xyz" to be printed to the standard error stream.
"""