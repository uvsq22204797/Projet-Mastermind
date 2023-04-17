from math import *

def master_minde(nb = 10) : # le nombre d'essais est de 10 
    for i in range (4):
        code = input("choix couleur") # le premier joueur choisi sa combinaison de couleur 
    for i in range (nb) :
        joueur_2 = [int(i) for i in input('choix_code')] # le joueur 2 essaie de trouver la combinaison 
        bien = sum([code[i] == joueur_2[i] for i in range (4) ]) # définir si les pions sont bien placés
        if bien == 4 :
           return('bravo ', code)
        mal = len(set(code) & set (joueur_2)) - bien 
        print ("bien placé:",bien,",mal placé:",mal)
    return ('perdu', code)