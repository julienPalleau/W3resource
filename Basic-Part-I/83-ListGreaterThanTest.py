# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
83. List Greater-Than Test

Write a Python program to test whether all numbers in a list are greater than a certain number.
"""
# Solution 1 using all()
a = [10, 16, 15, 11, 12]
b = 9
result = all(x > b for x in a)
print(result)

# Solution 2 using filter()
res = len(list(filter(lambda x: x > b, a))) == len(a)
print(res)

# Solution 3 using numpy
import numpy as np
res = np.all(np.array(a) > b)
print(res) 