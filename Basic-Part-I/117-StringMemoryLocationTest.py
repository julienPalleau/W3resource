# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
117. String Memory Location Test

Write a Python program to prove that two string variables of the same value point to the same memory location.
"""
import copy
test_string = "hello"
test_string_2 = copy.deepcopy(test_string)
print(f"test_string's variable memory address {id(test_string)}")
print(f"test_string_2's variable memory address {id(test_string_2)}")