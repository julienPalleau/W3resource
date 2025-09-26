# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""
import calendar
# Obtenir des informations sur le jour et le mois
print(f"Obtenir des informations sur le jour et le mois: {calendar.month(2023,6)}")

# Obtenir le jour de la semaine (0=lundi, 6=dimanche)
print(f"Obtenir le jour de la semaine (0=lundi, 6=dimanche): {calendar.weekday(2023, 6, 21)}")

# Vérifier si une année est bissextile
print(f"Vérifier si une année est bissextile: {calendar.isleap(2024)}")

# Obtenir le nombre de jours dans un mois
print(f"Obtenir le nombre de jours dans un mois: {calendar.monthrange(2025, 9)}")
