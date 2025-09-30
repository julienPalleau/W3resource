# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that concatenates all elements in a list into a string and returns it.
"""
def concatenate_list(values: list)->str:
    return "".join(str(n) for n in values)

print(concatenate_list(['a','b','c','d']))
print(concatenate_list([1,5,12,2]))