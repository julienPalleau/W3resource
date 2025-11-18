# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
90. Self-replicating Program
Write a Python program to create a copy of its own source code.
"""
# Define a function named file_copy that takes two arguments: src (source file) and dest (destination file).
def file_copy(src, dest):
    # Use the 'with' statement to open the source file for reading ('r') and the destination file for writing ('w').
    with open(src) as f, open(dest, 'w') as d:
        for line in f:
            d.write(line)

# Call the file_copy function with the source file "untitled0.py" and the destination file "z.py".
file_copy("Basic-Part-I/90-Self-replicatingProgram.py", "CopyOfTheFile-90-Self-replicatingProgram.py")

# Use the 'with' statement to open the 'z.py' file for reading ('r').
with open('CopyOfTheFile-90-Self-replicatingProgram.py', 'r') as filehandle:
    # Iterate through the lines in the 'z.py' file.
    for line in filehandle:
        # Print each line, and specify 'end' as an empty string to avoid extra line breaks.
        print(line, end = '')