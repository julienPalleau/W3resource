# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""
from time import perf_counter
from functools import wraps
# Ma Solution
def benchmark_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Record start time
        time_start = perf_counter()
        # Call the target function
        result = func(*args, **kwargs)
        # Record end time
        time_end = perf_counter()
        # Calculate the duration
        time_duration = time_end - time_start
        # Report the duration
        print(f"Took {time_duration:.3f} seconds")
        # Return the result
        return result
    return wrapper

@benchmark_decorator
def GCD(num1: int, num2: int)->int:
    if num1 < num2:
        for i in range(num1,1,-1):
            if num1%i==0 and num2%i==0:
                return i
    else:
        for i in range(num2,1,-1):
            if num1%i==0 and num2%i==0:
                return i
    return 1

# W3resource Solution
# Define a function to calculate the greatest common divisor (GCD) of two numbers.
@benchmark_decorator
def gcd(x, y):
    # Initialize gcd to 1.
    gcd = 1
    
    # Check if y is a divisor of x (x is divisible by y).
    if x % y == 0:
        return y
    
    # Iterate from half of y down to 1.
    for k in range(int(y / 2), 0, -1):
        # Check if both x and y are divisible by k.
        if x % k == 0 and y % k == 0:
            # Update the GCD to the current value of k and exit the loop.
            gcd = k
            break
    
    # Return the calculated GCD.
    return gcd

# Most efficient solution
@benchmark_decorator
def pgcd_euclide(a, b):
    while b:
        a, b = b, a % b
    return a
    
print(GCD(3960, 18900))
print(gcd(3960, 18900))
print(pgcd_euclide(12, 4))