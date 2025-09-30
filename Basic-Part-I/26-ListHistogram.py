# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to create a histogram from a given list of integers.
"""
def histogram(n: list[int])->str:
    return ['*'*number for number in n]
   
        

print("\n".join(histogram([1,2,3])))