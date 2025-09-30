# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""
# Solution 1
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(set(color_list_1).difference(set(color_list_2)))

# Solution 2
print(color_list_1 - color_list_2)