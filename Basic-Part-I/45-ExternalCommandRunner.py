# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that calls an external command.
"""
# Linux
# # Import the 'call' function from the 'subprocess' module.
# from subprocess import call

# # Use the 'call' function to execute the "ls -l" command.
# # This command lists the files and directories in the current directory with details.
# call(["dir"])

# Windows
"""
https://www.tutorialsteacher.com/articles/how-to-call-external-command-in-python
"""

"""
subprocess.run() function

This function runs the command in the string argument, waits for the process to complete, and object of CompletedProcess class. 
Following use case of run() function displays .ipynb files in the current directory on the Python shell and returns 
CompletedProcess instance with returncode=0 indicating successful execution.
"""
import subprocess
print("subprocess library:")
subprocess.run("dir *", shell=True)

print()

"""
os.popen() function

This function opens a pipe stream for communication with a file like object created by the first argument command. This function has 
the following signature:

os.popen(cmd, mode, buffering)

    cmd: A string representing command to be called
    mode: Either 'r' or 'w' decides direction of pipe.
    buffering: system's buffering policy

The following command opens an input pipe to read line by line output of given dir command. Output is displayed on console of Python shell.


The subprocess module of Python's standard library has two functions meant for calling external commands. The purpose of functions in this module is to spawn a new process and connect to IO pipes.

As per PEP 324, it is recommended to use the run() function to invoke a new process. 
"""
import os 
print("os library:")
pipe=os.popen("dir *") 
print(pipe.read())


# Import the 'os' module to work with the operating system.
import os

# Use 'os.system(command)' to execute the 'ls -l' command in the system's shell.
# This command lists the files and directories in the current directory and prints the result.
print("test")
print(os.system('dir'))