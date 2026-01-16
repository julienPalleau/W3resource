# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
112. Remove First List Item

Write a Python program to remove the first item from a specific list.
"""
# W3resource
# Solution 1
# Create a list of color names
print("Solution 1:")
color = ["Red", "Black", "Green", "White", "Orange"]

# Print the original list elements
print("Original list elements:")
print(color)

print()
# Remove the first element (element at index 0) from the list
del color[0]

# Print the list after moving the first color
print("After removing the first color:")
print(color)
print()


# W3resource
# Solution 2
# Create a list of color names 
print()
print("Solution 2:")
color = ["Red", "Black", "Green", "White", "Orange"]

# Print the original list elements
print("Original list elements:")
print(color)

# Print a message indicating the operation that will be performed
print("\nAfter removing the first element from the said list:")

# Create a new list 'new_color' by slicing the original list from the second element (index 1) to the end
new_color = color[1:]

# Print the modified list after removing the first element
print(new_color)
print()


# W3resource
# Solution 3
# Create a list of color names
print()
print("Solution 3:")
color = ["Red", "Black", "Green", "White", "Orange"]
 # Print a message indicating the original list elements
print("Original list elements:")

# Print the original list elements
print(color)

# Print a message indicating the operation that will be performed
print("\nAfter moving the first element from the said list:")

# Remove the element "Red" from the list
color.remove("Red")

# Print the modified list after removing the element
print(color)


# W3resource
# Solution 4
# Create a list of color names
print()
print("Solution 4:")
# Define a function named "tail" that takes a list "lst" as input.
def tail(lst):
    # Check if the length of the list is greater than 1.
    if len(lst) > 1:
        # If the list has more than one element, return a new list containing all elements except the first one.
        return lst[1:]
    else:
        # If the list has only one element or is empty, return the original list.
        return lst
    
# Call the "tail" function with different lists and print the results.
print(tail([1, 2, 3, 4])) # Should print [2, 3, 4]
print(tail([1])) # Should print [1] (no change)
print(tail(["Red", "Black", "Green", "White", "Orange"])) # Should print ["Black", "Green", "White", "Orange"]

# W3resource
# Solution 5
# Pour supprimer le premier élément d'une liste en Python, vous pouvez utiliser a.pop(0), a.remove(a[0]) ou a = a[1:].
'''
Supprimer le premier élément d’une liste en Python
Méthode	        Syntaxe	            Retour	            Modification de la liste	        Particularités
pop	            elem = lst.pop(0)	L’élément           Oui (in‑place)	                    Lève IndexError si 
                                    retiré	                                                la liste est vide.

del	            del lst[0]	        Aucun	            Oui (in‑place)	                    Lève IndexError si la
                                                                                            liste est vide.

remove	        lst.remove(lst[0])	Aucun	            Oui (in‑place)	                    Recherche 
                                                                                            l’élément puis le 
                                                                                            supprime ;
                                                                                            inutilement 
                                                                                            coûteux pour le 
                                                                                            premier élément.

Slicing	        lst = lst[1:]	    Nouveau 	Non (crée une nouvelle	                    Utile quand on 
                                    tableau     liste)                                      veut garder 
                                                                                            l’ancienne liste 
                                                                                            intacte.

                                                                                            
1. list.pop(0)

python
>>> fruits = ['pomme', 'banane', 'cerise']
>>> premier = fruits.pop(0)
>>> premier
'pomme'
>>> fruits
['banane', 'cerise']

    Retourne l’élément retiré, ce qui peut être pratique.
    Opération O(n) car tous les éléments doivent être décalés.

2. del (suppression par indice)

python
>>> nombres = [10, 20, 30, 40]
>>> del nombres,[0],
>>> nombres
[20, 30, 40]

    Aucun retour, uniquement la modification de la liste.
    Même complexité que pop(0) (déplacement des éléments).

3. list.remove(value)

python
>>> items = ['a', 'b', 'c']
>>> items.remove(items,[0],)   # supprime la première occurrence de 'a'
>>> items
['b', 'c']

    Recherche l’élément puis le supprime; pour le premier élément, c’est redondant.
    Utilisez‑le seulement si vous avez déjà la valeur et que vous ne connaissez pas son indice.

4. Slicing (création d’une nouvelle liste)

python
>>> data = [1, 2, 3, 4]
>>> data = data[1:]          # crée une nouvelle liste sans le premier élément
>>> data
[2, 3, 4]

    Ne modifie pas la liste d’origine (sauf si vous réaffectez la variable).
    Opération O(n) car une nouvelle liste est construite.

5. Considérations de performance
Taille de la liste	pop(0) / del	Slicing (lst[1:])
Petite (< 100)	Négligeable	Négligeable
Grande (> 10 000)	Décalage de tous les éléments → coût notable	Copie complète → coût similaire, mais crée un nouvel objet

    Si vous devez souvent retirer le premier élément, envisagez collections.deque, qui offre popleft() en O(1) :

python
from collections import deque

dq = deque([1, 2, 3, 4])
first = dq.popleft()   # 1
print(dq)              # deque([2, 3, 4])

6. Gestion des listes vides

python
lst = []
# pop
try:
    lst.pop(0)
except IndexError:
    print("Liste vide – rien à retirer")
# del
if lst:
    del lst,[0],   # sinon, rien à faire

7. Résumé des bonnes pratiques

    pop(0) : quand vous avez besoin de l’élément retiré.
    del lst[0] : quand vous ne voulez pas le retour et que vous modifiez la liste en place.
    Slicing : quand vous préférez travailler avec une nouvelle liste (ex. fonction pure).
    deque.popleft() : pour des files d’attente fréquentes ou de très grandes listes.

    Situation	                        Méthode recommandée	                Pourquoi
    Vous voulez modifier la liste 	    1️⃣ (indice + pop) ou 2️⃣ 	         Moins de copies, 
    en place                            (remove deux fois)                  plus rapide pour de grandes 
                                                                            listes

    Vous avez besoin d’une 	3️⃣          (compréhension)	                 Aucun effet de bord
    nouvelle liste (liste d’origine 
    intacte)

    Vous devez gérer l’absence de 	    1️⃣ ou 3️⃣ (elles testent le 	      remove deux fois nécessite 
    deux occurrences sans lever         compteur)                            un try/except
    d’exception                                                                         


8. Gestion des cas particuliers

    Valeurs non hashables (ex. listes imbriquées) : les mêmes techniques fonctionnent tant que l’opérateur == est défini.
    Listes très longues : la recherche linéaire (O(n)) est inévitable, car il faut parcourir les éléments jusqu’à la deuxième occurrence.
    Multithreading : si plusieurs threads modifient la même liste, protégez‑la avec un verrou (threading.Lock) pour éviter des comportements indéterminés.

En résumé
remove ne suffit pas pour la deuxième occurrence ; il faut d’abord identifier où se trouve cette occurrence 
(avec un compteur ou en appelant remove une première fois) puis la supprimer avec pop, del ou un second remove. 
Choisissez la variante qui correspond le mieux à votre besoin de mutabilité et de gestion d’erreurs.   
'''
