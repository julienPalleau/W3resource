# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
64-FileTimestamps.py

Write a Python program that retrieves the date and time of file creation and modification.
"""
import os
import time

# Flash Qwant Solution
print("Flash Qwant Solution")

# Méthode 1 : Utilisation de os.path.getctime()
file_path = 'Basic-Part-I/myfile41.txt'
creation_time = os.path.getctime(file_path)
print(f'Méthode 1: Utilisation de os.path.getctime(), Date de création: {time.ctime(creation_time)}')

# Méthode 2 : Utilisation de os.stat()
import os
import datetime

file_path = 'Basic-Part-I\myfile41.txt'
file_stats = os.stat(file_path)
creation_time = file_stats.st_ctime
creation_date = datetime.datetime.fromtimestamp(creation_time)
print(f"Méthode 2: Utilisation de os.stat(): Date de création: {creation_date}")

# Méthode 3: Utilisation de pathlib
from pathlib import Path
import time

file_path = Path('Basic-Part-I\myfile41.txt')
creation_time = file_path.stat().st_ctime
print(f"Méthode 3: Utilisation de pathlib: Date de création: {time.ctime(creation_time)}")

