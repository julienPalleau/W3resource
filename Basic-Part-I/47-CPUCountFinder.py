# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to find out the number of CPUs used.
"""
# Solution W3resource 1:
"""
Explanation:

multiprocessing is a package that supports spawning processes using an API similar to the threading module. 
The multiprocessing package offers both local and remote concurrency, 
effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, 
the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. 
It runs on both Unix and Windows.

cpu_count() function returns the number of CPUs in the system.

The above Python code imports the multiprocessing module and then calls its cpu_count() 
function to get the number of CPU cores on the current system. 
The code then calls print() function to print the number of CPU cores on the system to the console output.
"""
# Import the 'multiprocessing' module to work with multi-processing features.
import multiprocessing

# Use 'multiprocessing.cpu_count()' to determine the number of available CPU cores.
cpu_count = multiprocessing.cpu_count()

# Print the number of CPU cores available on the system.
print(cpu_count)


# Solution W3resource 2:
"""
Explanation:

The 'OS' module provides a portable way of using operating system dependent functionality. 
cpu_count() function returns the number of CPUs in the system. Returns None if undetermined.

The above Python code imports the multiprocessing module and then calls its cpu_count() 
function to get the number of CPU cores on the current system.

When the cpu_count() function is called, it returns the number of CPU cores on the system. 
The code then calls print() function to output the number of CPU cores on the system to the console output.
"""
# Import the 'os' module to access system-related functions.
import os

# Use 'os.cpu_count()' to determine the number of available CPU cores.
cpu_count = os.cpu_count()

# Print the number of CPU cores available on the system.
print(cpu_count)