import cProfile
import pstats
def slow_function():
    total = 0
    for i in range(10**6):
        total += i
    return total
with cProfile.Profile() as pr:
    slow_function()
stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats(5)