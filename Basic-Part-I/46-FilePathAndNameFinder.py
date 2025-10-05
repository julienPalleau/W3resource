# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to retrieve the path and name of the file currently being executed.
"""
import sys
import os


# W3resource Solution
# Use the 'os.path.realpath(__file__)' to get the full path of the current Python script.
# This will print the path of the current file.
print("Méthode : W3resource Solution Use the 'os.path.realpath(__file__)'")
print("Current File Name: ", os.path.realpath(__file__))

print()

# Qwant assistant

print("Méthode 1 : Utilisation de l'attribut __file__")
# Méthode 1 : Utilisation de l'attribut __file__
# Récupérer le chemin du fichier courant
current_path = os.path.abspath(sys.argv[0])
file_name = os.path.basename(current_path)
file_path = os.path.dirname(current_path)

print("Fichier courant :", current_path)
print("Nom du fichier :", file_name)
print("Chemin du fichier :", file_path)

print()

print("Méthode 2 : Utilisation du module inspect")
# Méthode 2 : Utilisation du module inspect
import inspect
import os

current_frame = inspect.currentframe()
current_path = inspect.getframeinfo(current_frame).filename
current_file = os.path.basename(current_path)
current_dir = os.path.dirname(current_path)

print("Chemin courant :", current_path)
print("Fichier courant :", current_file)
print("Répertoire courant :", current_dir)