import tkinter as tk
import random
from tkinter import Label, Radiobutton, Button, StringVar
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

# Couleurs possibles pour les pions
couleurs = ["bleu", "vert", "jaune", "orange", "jaune", "marron"]


# Fonction pour vérifier la combinaison proposée par le joueur
def verification(essai, code_bon):
    bonne_place = 0
    mauvaise_place = 0
    
    for i in range(4):
        if essai[i]==code_bon[i]:
            bonne_place+=1
        elif essai[i] in code_bon:
            mauvaise_place+=1
            
    return bonne_place, mauvaise_place



# Fonction qui génère le code aléatoire pour le mode 1 joueur
def code_aleatoire():
    couleurs = ["bleu", "vert", "jaune", "orange", "jaune", "marron"]
    code_alea = ""
    
    for i in range(4):
        code_alea += (random.choice(couleurs)+" ")
        
    return code_alea
#(code_aleatoire())




# joueur 1 donne une combinaison 
#joueur1 = input("donner un combinaision"), input("donner un combinaision"), input("donner un combinaision"), input("donner un combinaision")

#joueur 2 donne une combinaison 
#joueur2 = input("donner un combinaision"), input("donner un combinaision"), input("donner un combinaision"), input("donner un combinaision")

# début du programme 
#if joueur2 == joueur1:
#    print("bien joué")
#else :
#    print("essai encore")


#code_joueur1=input("Choissisez 4 couleurs parmi les suivantes en respectant la syntaxe: bleu, vert, jaune, orange, jaune, marron")


racine.mainloop()