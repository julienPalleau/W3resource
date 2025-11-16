# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
22. Count 4 in List

Write a Python program to count the number 4 in a given list.
"""
# Solution with method count()
liste=[1,2,3,4,5,6,4,7,4]
print(liste.count(4))

# Solution 2 with lib collections
from collections import Counter
count = Counter(liste)
print(count[4])