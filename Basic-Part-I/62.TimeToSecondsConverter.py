# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to convert all units of time into seconds.
"""
import pyinputplus as pyip
# Prompt the user to input a number of days and store it in the variable 'days'.
days = pyip.inputInt("Input days: ")
hours = pyip.inputInt("Input hours:")
minutes = pyip.inputInt("Input minutes:")
seconds = pyip.inputInt("Input seconds:")

# Method 1: Using Total Seconds with timedelta
"""
ython’s datetime.timedelta object represents a duration, which contains days, 
seconds, and microseconds by default. To convert a timedelta to seconds, 
you can use its total_seconds() method, which will give a total count of seconds encapsulating the entire duration. 
This is practical when you’re already operating with timedelta instances in your code.
"""

from datetime import timedelta
duration = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
print(f"Method 1: Using Total Seconds with timedelta: Total: {round(duration.total_seconds())} seconds")


# Method 2: Manually Calculating seconds
"""
When you’re dealing with individual time components (hours, minutes, and seconds), 
you can calculate the total time in seconds by manually multiplying and adding the respective components: 
hours by 3600, minutes by 60, and summing them with seconds. 
This method does not require any additional libraries and is straightforward to use.
"""
duration = days*3600*24 + hours*3600 + minutes*60 + seconds
print(f"Method 2: Manually Calculating seconds: Total: {duration} seconds")


# Method 3: Using List Comprehension and sum()
"""
With Python list comprehension and sum() function, you can compress the manual calculation of seconds into a one-liner. 
This is useful for quick conversions and reduces the code size significantly.
"""
time_parts = [4, 5, 20, 10]
seconds = sum(x * int(y) for x, y in zip([24*3600, 3600, 60, 1], time_parts))
print(f"Method 3: Using List Comprehension and sum() {seconds} seconds")