# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""
def check_value(n: int, liste: list) -> bool:
    return True if n in liste else False

print(check_value(3, [1, 5, 8, 3]))
print(check_value(-1, [1, 5, 8, 3]))