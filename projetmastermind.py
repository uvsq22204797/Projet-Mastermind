import tkinter as tk
import random
from tkinter import Label, Button
from tkinter import BOTH, X, Y
import tkinter.font as font

racine=tk.Tk()
racine.title("MASTERMIND")
racine.geometry('700x620')
racine.config(bg='blue')

# Définir le style: type de la police, taille et gras
style_A = font.Font(family='Times New Roman', size=20, weight="bold")

# Définir les titres (Label) et les boutons (Button)
Bienvenue_Acceuil_1 = Label(racine, text='Bienvenue dans le jeu MASTERMIND', bg= 'turquoise', font=30).pack(fill=X)
Bienvenue_Acceuil_2 = Label(racine, text='Choisissez un mode de jeu', bg = 'dark green', font=20).pack(fill=Y)
bouton_1_joueur = Button(racine, text='1 joueur', bg = 'dark green', fg ='pink', command = lambda: mode_1_joueur)
bouton_2_joueurs = Button(racine, text='2 joueurs', bg = 'dark green', fg ='pink', command = lambda: mode_2_joueurs)
bouton_1_joueur.place(x=180, y=200)
bouton_1_joueur['font'] = style_A
bouton_2_joueurs.place(x=400, y=200)
bouton_2_joueurs['font'] = style_A

# l'activation du "bouton_1_joueur" appelle la fonction "mode_1_joueur"
def mode_1_joueur():  
    racine.configure(bg='white')
    command = bouton_1_joueur.destroy()
    command = bouton_2_joueurs.destroy()

# l'activation du "bouton_2_joueurs" appelle la fonction "mode_2_joueurs"
def mode_2_joueurs():
    racine.config(bg='grey')
    command = bouton_1_joueur.destroy()
    command = bouton_2_joueurs.destroy()

racine.mainloop()
