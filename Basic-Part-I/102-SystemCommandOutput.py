# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
102. System Command Output

Write a Python program to get system command output.
"""
# Import the subprocess module to run shell commands.
import subprocess

# Use the 'sbuprocess.check_output' function to execute the 'dir' command in the shell.
# 'universal_newlines=True' ensures text mode for cross-platform compatibility.
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)

# Print a message indicating the purpose of running the 'dir' command.
print("dir command to list files and directories")

# Print the output (list of files and directories) returned by the 'dir' command.
print(returned_text)
