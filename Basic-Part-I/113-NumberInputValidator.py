# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
113. Number Input Validator

Write a Python program that inputs a number and generates an error message if it is not a number.
"""
# Ma solution
while True:
    user_input = input("Entrer un nombre (ou 'q' pour quitter): ")
    if user_input.lower() == 'q':
        break
    try:
        number = float(user_input)
    except ValueError:
        print("Ce n'est pas un nombre valide.")
    else:
        print(f"Vous avez entré le nombre {number}")