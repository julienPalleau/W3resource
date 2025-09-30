# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to test whether a passed letter is a vowel or not.
"""
def vowel(letter: str) -> bool:
    return True if letter.lower() in ['a', 'e', 'i', 'o', 'u', 'y'] else False

print(vowel('a'))
print(vowel('A'))
print(vowel('n'))
print(vowel('N'))