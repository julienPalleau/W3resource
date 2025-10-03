# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
"""
def equality_or_5_rule_checker(value1: int, value2: int)->bool:
    return True if value1 == value2 or value1 + value2 == 5 or abs(value1 - value2) == 5 else False

print(equality_or_5_rule_checker(7, 2))
print(equality_or_5_rule_checker(3, 2))
print(equality_or_5_rule_checker(2, 2))
print(equality_or_5_rule_checker(7, 3))
print(equality_or_5_rule_checker(27, 53))