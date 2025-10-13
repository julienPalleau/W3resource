# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
3. PythonPrintCurrentTimeAndDate.py

Write a Python program to display the current date and time.

Python datetime:

The datetime module supplies classes for manipulating dates and times in both simple and complex ways. 
datetime.now(tz=None) returns the current local date and time. If optional argument tz is None or not specified, this is like today().

Python date time

date.strftime(format) returns a string representing the date, controlled by an explicit format string. 
Format codes referring to hours, minutes or seconds will see 0 values.

Pre-Knowledge (Before you start!)

    Basic Python Syntax: Familiarity with how to write and run Python scripts.
    Importing Modules: Understanding of how to import modules in Python using the import statement.
    Datetime Module:
        The datetime module provides classes for manipulating dates and times.
        datetime.now() function returns the current local date and time.
    String Formatting:
        Knowledge of string formatting, especially using the strftime() method.
        Understanding format codes like %Y, %m, %d, %H, %M, and %S.
    Output Functions: Familiarity with the print() function to display output in Python.

Hints (Try before looking at the solution!)

    Import the Datetime Module: Begin by importing the datetime module to access date and time functionalities.
    Get Current Date and Time: Use datetime.datetime.now() to create a datetime object representing the current date and time.
    Display Information: Use the print() function to display a message indicating what is being printed.
    Format the Output: Use the strftime() method to format the datetime object into a readable string.
        Format String Example: "%Y-%m-%d %H:%M:%S" translates to "Year-Month-Day Hour:Minute:Second".
    Common Format Codes:
        %Y: Year with century (e.g., 2023).
        %m: Month as a zero-padded decimal number (01-12).
        %d: Day of the month as a zero-padded decimal number (01-31).
        %H: Hour (24-hour clock) as a zero-padded decimal number (00-23).
        %M: Minute as a zero-padded decimal number (00-59).
        %S: Second as a zero-padded decimal number (00-59).
    Check Your Output: Ensure that the formatted date and time appear correctly in the console when you run your script.

"""


"""
Explanation:

The said code imports the "datetime" module, gets the current date and time, and finally prints it in a formatted string.

    The first line import datetime imports the datetime module which supplies classes for manipulating dates and times.
    The second line now = datetime.datetime.now() creates a datetime object for the current date and time.
    The third line print ("Current date and time : ") prints the string "Current date and time : " to the console.
    The fourth line print (now.strftime("%Y-%m-%d %H:%M:%S")) uses the strftime() method of the datetime object 
    to format the date and time as a string in the format "YYYY-MM-DD HH:MM:SS" and prints it to the console.

The strftime() method returns a string representing the date, controlled by an explicit format string. 
The format codes used in this example are:

    %Y: year with century as a decimal number.
    %m: month as a zero-padded decimal number.
    %d: day of the month as a zero-padded decimal number.
    %H: hour (24-hour clock) as a zero-padded decimal number.
    %M: minute as a zero-padded decimal number.
    %S: second as a zero-padded decimal number.

This code can be useful for logging or timestamping events in a program, or for displaying the current date and time in a user interface.
"""
# Import the 'datetime' module to work with date and time
from datetime import datetime, timezone

# Get the current date and time
now_utc = datetime.now(timezone.utc)
now = datetime.now()
# Create a datetime object representing the current date and time

# Display a message indicating what is being printed
print("Current date and time : ")

# Print the current date and time in a specific format
print(f"local time: {now.strftime("%Y-%m-%d %H:%M:%S")}")
print(f"UTC time: {now_utc.strftime("%Y-%m-%d %H:%M:%S")}")

# Use the 'strftime' method to format the datetime object as a string with the desired format
