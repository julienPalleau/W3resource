# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
14-DaysBetweenDates.py

Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
import arrow
from datetime import date

# Ma solution with arrow
print((arrow.get(2014,7,11) - arrow.get(2014,7,2)).days)


# Solution w3resource with datetime

# Define a start date as July 2, 2014
f_date = date(2014, 7, 2)

# Define an end date as July 11, 2014
l_date = date(2014, 7, 11)

# Calculate the difference between the end date and start date
delta = l_date - f_date

# Print the number of days in the time difference
print(delta.days)