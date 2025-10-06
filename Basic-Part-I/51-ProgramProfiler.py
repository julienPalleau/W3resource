# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to determine the profiling of Python programs.
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. 
These statistics can be formatted into reports via the pstats module.
"""
import cProfile
import random
import time

# Flash Qwant Solution
print("Flash Qwant Solution")
def charger_donnees(n):
    donnees = [random.randint(0, 1000) for _ in range(n)]
    time.sleep(0.1)  # Simulation d'un délai d'E/S
    return donnees

def traiter_donnees(donnees):
    total = 0
    for element in donnees:
        total += element
    time.sleep(0.2)  # Simulation d'un délai de traitement
    return total

def main():
    donnees = charger_donnees(10000)  # Charger les données
    resultat = traiter_donnees(donnees)  # Traiter les données
    print(f'Total: {resultat}')  # Afficher le résultat

if __name__ == '__main__':
    cProfile.run('main()')

# W3resource 
print()
print('W3resource Solution')
# Import the cProfile module, which provides a way to profile Python code.
import cProfile
# Define a function named 'sum'.
def sum():
   # Print the result of adding 1 and 2 to the console.
   print(1 + 2)
# Use cProfile to profile the 'sum' function.
cProfile.run('sum()')