# https://www.w3resource.com/python-exercises/python-basic-exercises.php
# https://www.geeksforgeeks.org/python/python-program-to-convert-seconds-into-hours-minutes-and-seconds/ (solutions)
"""
65-SecondsToDHMSConverter.py

Write a Python program that converts seconds into days, hours, minutes, and seconds.
"""
# 1-Naive Approach
"""
This approach uses simple mathematical calculations to get the hours, minutes, and seconds.
"""
print("Solution 1: Naive Approach")
def convert1(seconds):
    day = seconds // (24 * 3600)
    seconds %= 3600
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{day:1} jour(s) {hour:1} heure(s) {minutes:2} minute(s) {seconds:2} seconde(s)"

print(convert1(88660))
"""
Explanation:

    seconds % (24 * 3600) ensures that seconds fit within a 24-hour range.
    seconds // 3600 calculates how many hours are in the given seconds.
    seconds % 3600 calculates the remaining seconds after extracting hours.
    seconds // 60 calculates how many minutes are in the remaining seconds.
    seconds % 60 gives the remaining seconds after extracting minutes.
"""


# 2-Using divmod()
"""
Using the divmod() function allows for a more efficient solution by performing the division and modulus operations in one step.
"""
print("Solution 2: Using divmod()")
def convert2(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    day, hour= divmod(hour, 24)
    return f'{day} jours {hour} heures {min} minutes {sec} secondes'

print(convert2(88660))
"""
Explanation:

    divmod(seconds, 60) returns a tuple containing minutes and remaining seconds.
    divmod(min, 60) returns a tuple containing hours and remaining minutes.
    The result is formatted as 'hours:minutes:seconds' using string formatting
"""


# 3-Using timedelta (from datetime modulte)
"""
The datetime module provides a timedelta object which can represent durations, making it easy to convert seconds into a human-readable format.
"""
print("Solution 3: Using timedelta(from datetime module)")
import datetime
def convert3(n):
    return str(datetime.timedelta(seconds = n))

print(convert3(88660))
"""
Explanation: timedelta(seconds=n) function automatically converts the given seconds into the format hours:minutes:seconds.
"""

