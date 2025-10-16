# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
57-MethodExecutionTime.py

Write a Python program to get the execution time of a Python method.
"""
# Import the 'time' module to work with time-related functions.
import time

# Define a function named 'sum_of_n_numbers' that calculates the sum of the first 'n' natural numbers.
def sum_of_n_numbers(n):
    # Record the current time before the calculation.
    start_time = time.time()

    # Initialize a variable 's' to store the sum.
    s = 0

    # Loop through numbers from 1 to 'n' and accumulate the sum.
    for i in range(1, n + 1):
        s = s + i

    # Record the current time after the calculation.
    end_time = time.time()

    # Return both the calculated sum and the time taken for the calculation.
    return s, end_time - start_time

# Define the value of 'n' as 5.
n = 5

# Print the result, including the time taken to calculate the sum.
print("\nTime to sum of 1 to", n, "and required time to calculate is:", sum_of_n_numbers(n))

"""
Explanation:

The above Python code defines a function sum_of_n_numbers() that calculates the sum of the first n positive integers, 
and returns the sum and the time it took to calculate the sum.

time module - This module provides various time-related functions.

The sum_of_n_numbers() function uses a for loop to add up the first n positive integers and calculates 
the time it takes to do so using the time.time() function to get the start and end times of the operation. 
The function returns a tuple containing the sum of the first n positive integers and the time taken to calculate the sum.

Finally the code then calls the sum_of_n_numbers() function with an argument of n=5, and prints the result 
to the console using the print() function. The output displays the time it took to calculate the sum of the 
first 5 positive integers and the calculated sum.
"""