# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
19-PrefixIsStringModifier.py

Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
Return the string unchanged if the given string already begins with "Is".
"""
def newlyGeneratedString(astring: str)->str:
    return astring if astring.startswith('Is') else 'Is'+astring
    
print(newlyGeneratedString('IsHello'))
print(newlyGeneratedString('Hello'))