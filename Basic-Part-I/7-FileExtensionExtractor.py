# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""
import pathlib

# Ma Solution
print(f"extension: {pathlib.Path("abc.java").suffix}")
print(f"name: {pathlib.Path("abc.java").stem}")
test = "abc.java".split(".")
print(f"extension: {test[-1]}")

# W3resource Solution
"""
File Extension Extractor

Write a Python program that accepts a filename from the user and prints the extension of the file.

Sample filename: abc.java

Python str.rsplit(sep=None, maxsplit=-1) function:

str.split(sep=None, maxsplit=-1)

Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are 
done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the 
number of splits (all possible splits are made).

    If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings 
    (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters 
    (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].
    If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are 
    regarded as a single separator, and the result will contain no empty strings at the start or end if the string has 
    leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace 
    with a None separator returns [].

For example, ' 1 2 3 '.split() returns ['1', '2', '3'], and ' 1 2 3 '.split(None, 1) returns ['1', '2 3 '].

The function returns a list of the words of a given string using a separator as the delimiter string.

    If maxsplit is given, the list will have at most maxsplit+1 elements.
    If maxsplit is not specified or -1, then there is no limit on the number of splits.
    If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.
    The sep argument may consist of multiple characters.
    Splitting an empty string with a specified separator returns [''].

"""
# Prompt the user to input a filename and store it in the 'filename' variable
filename = input("Input the Filename: ")

# Split the 'filename' string into a list using the period (.) as a separator and store it in the 'f_extns' variable
f_extns = filename.split(".")

# Print the extension of the file, which is the last element in the 'f_extns' list
print("The extension of the file is : " + repr(f_extns[-1]))