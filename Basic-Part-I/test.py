import tkinter as tk
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.title("Afficheur de message")
fenetre.geometry("400x200")


def afficher_message():
    text=entree.get()
    label_resultat.config(text=f"Bonjour {text}  !")


def run_automation():
    # Imagine your complex automation logic here
    messagebox.showinfo("Status", "Process Started!")

bouton = tk.Button(fenetre, text="Afficher", command=afficher_message)
bouton.pack(pady=5)

bouton2 = tk.Button(fenetre, text="Fenêtre Status", command=run_automation)
bouton2.pack(pady=20)

entree = tk.Entry(fenetre, width=20)
entree.pack(pady=10)

label_resultat = tk.Label(fenetre, text="Bonjour !", font=("Arial", 16))
label_resultat.pack()

valeur=entree.get()

fenetre.mainloop()