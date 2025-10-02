# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to find the least common multiple (LCM) of two positive integers.
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


# Solution 1: Utilisation d'une boucle
@benchmark_decorator
def lcm_loop(x: int, y: int) -> int:
    if x > y:
        z = x
    else:
        z = y
    while True:
        if (z % x == 0) and (z % y == 0):
            return z
        z += 1


# Solution 2: Utilisation de la fonction GCD(PGCD)
import math
from functools import reduce
@benchmark_decorator
def lcm_relation(x: int, y: int) -> int:
    return reduce((lambda x, y: int(x * y / math.gcd(x, y))), [x, y])


# Solution 3: Utilisation de la fonction intégrée math.lcm
from math import lcm
@benchmark_decorator
def builtin_lcm(x:int, y:int) -> int:
    return lcm(x, y)


print(lcm_loop(4, 6))
print(lcm_relation(4, 6))
print(builtin_lcm(4, 6))
print()

print(lcm_loop(15, 17))
print(lcm_relation(15, 17))
print(builtin_lcm(15, 17))
