


import random
import tkinter as tk
import json 
chemin = "data.json"



"""Mise en page de la première fenêtre du jeu"""
racine = tk.Tk()
racine.title("MASTERMIND")
racine.config(bg='peachpuff')
racine.geometry("800x800")
def accueil():
    bienvenue= tk.Label(racine,text="BIENVENUE DANS LE JEU MASTERMIND ", bg="lightsalmon", font=('Helvetica bold ', 22))
    bienvenue.pack()
    fenetre =tk.Frame(racine, width=600, height=200, bg="lightsalmon")
    fenetre.place(x=100,y=200)
    bouton_un_joueur = tk.Button(fenetre, text="1 joueur", command=un_joueur,bg='peachpuff',font=('Helvetica bold ', 22))
    bouton_un_joueur.place(x=100, y=100)
    bouton_deux_joueur = tk.Button(fenetre, text="2 joueurs", command=deux_joueurs,bg='peachpuff',font=('Helvetica bold ', 22))
    bouton_deux_joueur.place(x=390, y=100)
    choix= tk.Label(racine,text="VEUILLEZ CHOISIR UN MODE DE JEU : ", bg="lightsalmon", font=('Helvetica bold ', 22))
    choix.pack()
    
    
"""Longueur de la combinaison"""
taille_code = 4
combi = []
    
    

"""Couleurs possibles pour les pions"""
couleurs_pions = ["lightskyblue", "palegreen", "yellow", "darkorange", "red","mediumorchid"]
couleurs_verif= ['black','white']  



"""Selection de la position du rond a colorer"""    
def position_rond(position_couleur):
    cnv.itemconfig(position_couleur, width=5)
    
"""Déselection de la couleur"""
def deselect(position_couleur):
    cnv.itemconfig(position_couleur, width=0)



"""Coloratiion du rond"""
def coloration_rond(position_couleur,couleur):
    cnv.itemconfig(position_couleur, fill=couleur)


"""Nombres de chances du joueurs"""   
nb_tentatives = 11
temporaire = nb_tentatives



"""Dimensions du plateau et des places des pions"""
largeur_plateau = 400
hauteur_plateau = 700
taille_rond1 = 50
taille_rond2 = 60
couleur_fond_pions = "silver"



choix_joueur = [[-1 for i in range(taille_code)] for j in range(nb_tentatives)]
indice = [[-1 for i in range(taille_code)] for j in range(nb_tentatives)]



"""Fonctions associées aux touches du clavier"""
def touches_clavier():
    cnv.unbind('<space>')
    cnv.bind('<Up>', lambda _: change_couleur(1))
    cnv.bind('<Right>', lambda _: decale_couleur(1))
    cnv.bind('<Down>', lambda _: change_couleur(-1))
    cnv.bind('<Left>', lambda _: decale_couleur(-1))
    cnv.bind('<Return>', lambda _: verif())
def stop_touches_clavier():
    cnv.unbind("<Up>")
    cnv.unbind("<Right>")
    cnv.unbind("<Down>")
    cnv.unbind("<Left>")
    cnv.unbind("<Return>")
    
    

"""Changer de couleur grace aux fleches"""
def change_couleur(increment):
    choix_joueur[row][cpos] += increment
    if choix_joueur[row][cpos] > len(couleurs_pions)-1:
        choix_joueur[row][cpos] = 0
    if choix_joueur[row][cpos] < 0:
        choix_joueur[row][cpos] = len(couleurs_pions)-1
    cnv.itemconfig(grille[row][cpos], fill=couleurs_pions[choix_joueur[row][cpos]])
    
    
    
"""Change de rond pour modifier la couleur suivante"""
def decale_couleur(increment):
    global cpos
    cnv.itemconfig(grille[row][cpos],width=0)
    cpos += increment
    if cpos < 0:
        cpos = taille_code-1
    if cpos >= taille_code:
        cpos = 0
    cnv.itemconfig(grille[row][cpos],width=1)



"""Vérification de la réponse de l'utilisateur et mise à jour l'interface graphique en conséquence"""
def verif():
    global combi_secrete,row,bien_place,mal_place, choix_joueur, indice
    bien_place, mal_place = 0, 0
    utilise = []
    compteur = 0
    if nb_tentatives == 1:
            combi_secrete = choix_joueur.copy()[0]
            choix_joueur[0] = [-1 for i in range(taille_code)]
            fr.destroy()
            un_joueur()
            return
        
    for i in range(taille_code):
        if choix_joueur[row][i] == -1:
            print(f"Colors not set {row},{i}:")
            return False
        
        if (combi_secrete[i]==choix_joueur[row][i]): 
            indice[row][compteur] = 0
            compteur += 1
            bien_place += 1
            utilise.append(i)
            
    for i in range(taille_code):
        for j in range(taille_code):
            if (j!=i and combi_secrete[j]==choix_joueur[row][i] and j not in utilise):
                indice[row][compteur] = 1
                compteur += 1
                mal_place += 1
                utilise.append(j)
                break
        
    if bien_place < taille_code and row < nb_tentatives-2:
        print(f"bien_place:{bien_place}, mal_place:{mal_place}")
        
        for i in range(bien_place):
            cnv.itemconfig(rep_joueur[row][i], fill="black")
            
        for i in range(mal_place):
            cnv.itemconfig(rep_joueur[row][i+bien_place], fill="white")
            
        cnv.itemconfig(grille[row][cpos],width=0)
        row += 1
        cnv.itemconfig(grille[row][cpos],width=1)
        initialisation_ligne()
        return False
    
    else:
        print(f"Row{row} bien_place{bien_place} and mal_place{mal_place}")
        print(rep_joueur, combi_secrete, choix_joueur)
        output = True
        
        if row == nb_tentatives-2:
            output = False
            
        for i in range(bien_place):
            print(row, i)
            cnv.itemconfig(rep_joueur[row][i], fill="black")
            
        for i in range(taille_code):
            cnv.itemconfig(grille[nb_tentatives-1][i], fill=couleurs_pions[combi_secrete[i]])
            
        stop_touches_clavier()
        cnv.bind("<space>", lambda _: jeu1joueur(grille, rep_joueur))
        return output
    
    
    
"""Sauvegarde de la partie dans un fichier Json afin de sauvegarder l'état du jeu pour une reprise ultérieure"""
def sauvegarder():
    global choix_joueur, combi_secrete, indice, row
    sauv = {}
    with open(chemin, 'w') as f:
        sauv['essai_joueur'] = choix_joueur
        sauv["combinaison"] = combi_secrete
        sauv["index"] = indice
        sauv["ligne"] = row
        json.dump(sauv, f)



"""Suppression du dernier coup du joueur qui va pouvoir reprendre à partir de la ligne précédente"""
def supp():
    global board, rep_joueur, row, cnv, choix_joueur, indice
    if row == 0:
        return
    for i in range(taille_code):
        cnv.itemconfig(grille[row][i], fill=couleur_fond_pions, width=0)
        cnv.itemconfig(rep_joueur[row][i], fill=couleur_fond_pions)
        choix_joueur[row][i] = -1
        indice[row][i] = -1
    row -= 1
    for i in range(taille_code):
        cnv.itemconfig(grille[row][i], fill=couleur_fond_pions)
        cnv.itemconfig(rep_joueur[row][i], fill=couleur_fond_pions)
        choix_joueur[row][i] = -1
        indice[row][i] = -1
        
        
        
"""Initialiser la partie de Mastermind dans un jeu à un seul joueur"""
nb_joueurs = 1
def jeu1joueur(grille, rep_joueur):
    global row, cpos, choix_joueur, combi_secrete, nb_joueurs
    cnv.itemconfig(grille[row][cpos],width=1)
    touches_clavier()
    if nb_joueurs == 1:
        combi_secrete = mode1joueur()
    initialisation_ligne()
    
    
    
"""Mode 1 joueur"""
nb_joueurs=1
def un_joueur():
    global fr, grille,cnv,  rep_joueur,  temporaire, hauteur_plateau,nb_tentatives, nb_joueurs
    nb_joueurs=1
    nb_tentatives = temporaire
    hauteur_plateau = 700
    fr = tk.Toplevel(racine)
    cnv = tk.Canvas(fr, width=largeur_plateau, height=hauteur_plateau, highlightthickness=0,highlightbackground="black", relief=tk.FLAT,bg="peachpuff",bd=0)
    cnv.pack()
    grille, rep_joueur =gille_jeu()
    cnv.focus_set()
    touches_clavier()
    cnv.bind("<space>", lambda _: jeu1joueur(grille, rep_joueur))
    
    
    
"""Mode 2 joueurs"""
def deux_joueurs():
    global fr, grille,cnv,rep_joueur,  hauteur_plateau, nb_joueurs,nb_tentatives
    fenetre =tk.Frame(racine, width=600, height=200, bg="lightsalmon")
    fenetre.place(x=100,y=200)
    hauteur_plateau = 700
    nb_joueurs = 2
    nb_tentatives = 1
    fr = tk.Toplevel(racine)
    cnv = tk.Canvas(fr, width=largeur_plateau, height=hauteur_plateau, highlightthickness=0,highlightbackground="black", relief=tk.FLAT,bg="peachpuff",bd=0)
    cnv.pack()
    grille, rep_joueur = gille_jeu()
    cnv.focus_set()
    touches_clavier() 
    
    
      
"""Préparation la grille pour la prochaine supposition du joueur"""
def initialisation_ligne():
    global combi,bien_place, mal_place
    combi = [i for i in range(len(couleurs_pions))]
    bien_place = 0
    mal_place = 0
    
    
    
"""Génère aléatoirement une combinaison secrète dans le cas où il n'y a qu'un seul joueur"""
def mode1joueur():
    fenetre =tk.Frame(racine, width=600, height=200, bg="lightsalmon")
    fenetre.place(x=100,y=200)
    ind_couleur = [i for i in range(len(couleurs_pions))]
    code = []
    for e in range(taille_code):
        codeIndex = random.randint(0,len(ind_couleur)-1)
        code.append(ind_couleur[codeIndex])
        ind_couleur.pop(codeIndex)
        choix_joueur = tk.Label(fenetre, text="Choisser la combinaison",fg='brown')
        choix_joueur.pack()
    return code






"""Création et affichage de la grille de jeu"""
def gille_jeu():
    global couleurs_pions, indice
    print(indice)
    rep_joueur= []
    grille = []
    bouton_supp = tk.Button(fr, text="Supprimer", command=supp, bg="lightsalmon", font=("Helvetica bold ", 22))
    button_sauvegarde = tk.Button(fr, text="Sauvegarder", command=sauvegarder, bg="lightsalmon", font=("Helvetica bold ", 22))
    bouton_supp.pack()
    button_sauvegarde.pack()
    
    for i in range(nb_tentatives):
        newRow = []
        newResponse = []
        
        for j in range(taille_code):
            x = taille_rond2*j+5
            y = hauteur_plateau - taille_rond2*i - taille_rond1 - 5
            
            if choix_joueur[i][j] == -1:
                newRow.append(cnv.create_oval(x,y,x+taille_rond1,y+taille_rond1,fill=couleur_fond_pions,outline='black',width=0))
                
            else:
                print(couleurs_pions[choix_joueur[i][j]])
                newRow.append(cnv.create_oval(x,y,x+taille_rond1,y+taille_rond1,fill=couleurs_pions[choix_joueur[i][j]],outline='black',width=0))
                
            if i < nb_tentatives-1:
                x = taille_rond2/2*j+taille_code*taille_rond2+20
                y += taille_rond1/8
                
                if indice[i][j] == -1:
                    newResponse.append(cnv.create_oval(x+ taille_rond1/4, y+ taille_rond1/4, x + taille_rond1/2, y + taille_rond1/2, fill=couleur_fond_pions, outline='black', width=0))
                    
                else:
                    newResponse.append(cnv.create_oval(x+ taille_rond1/4, y+ taille_rond1/4, x + taille_rond1/2, y + taille_rond1/2, fill=couleurs_verif[indice[i][j]], outline='black', width=0))
        grille.append(newRow)
        
        if i < nb_tentatives - 1:
            rep_joueur.append(newResponse)
            
    jeu1joueur(grille, rep_joueur)
    cnv.itemconfig(grille[row][cpos],width=1)
    return grille, rep_joueur


    

accueil()
racine.mainloop()