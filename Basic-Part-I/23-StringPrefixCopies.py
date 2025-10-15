# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
23-StringPrefixCopies.py

Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
Return n copies of the whole string if the length is less than 2.
"""
def string_prefix_copies(n:int, word:str):
    return word[:2]*2 if len(word) >=2 else word*n
    

print(string_prefix_copies(5, "test"))
print(string_prefix_copies(5, "t"))
