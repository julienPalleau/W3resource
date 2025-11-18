# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
82. Sum of Container Items

Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).
"""

# tuple
container = (1, 2, 3, 4, 5)
result = sum(container)
print(f'sum of a tuple: {result}')

# list
container = [1, 2, 3, 4, 5]
result = sum(container)
print(f'sum of a list: {result}')

# set
container = {1, 2, 3, 4, 5}
result = sum(container)
print(f'sum of a set: {result}')

# dictionary
# solution 1 using sum()
container={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
result = sum(container.values())
print(f'Solution1, sum of a dictionary: {result}')

# solution 2 using list comprehension and sum()
result = sum(container[key] for key in container)
print(f'Solution2, sum of a dictionary: {result}')

# solution 3 using map
res = sum(map(lambda key: container[key], container))
print(f'Solution3, sum of map: {result}')