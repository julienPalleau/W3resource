# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
84. Character Frequency Counter

Write a Python program to count the number of occurrences of a specific character in a string.
"""
# Solution 1 using count()
my_string="The quick brown fox jumps over the lazy dog."
print(f'Solution 1: {my_string.count('o')}')

# Solution 2 using Counter from collections
from collections import Counter
print(f'Solution 2: {str(Counter(my_string)['o'])}')

# Solution 3 using lambda functions:
print(f'Solution 3: {sum(map(lambda x: 1 if 'o' in x else 0, my_string))}')

# Solution 4 using a regular expression
import re
print(f'Solution 4: {len(re.findall("o", my_string))}')