def select_un_joueur():
    global FRAME, CANVAS, board, response, NB_OF_GUESS, TMP, HEIGHT, NB_PLAYER
    NB_OF_GUESS = TMP
    HEIGHT = NB_OF_GUESS*55+70
    FRAME = tk.Toplevel(ROOT)
    instruction =tk.Label(FRAME, text="Essayer de trouver la combinaison choisie !",fg="brown")
    instruction_2 = tk.Label(FRAME, text=" Pion blanc = bonne couleur, Pion noir = bien placé ET bonne couleur",fg="brown")
    instruction.pack()
    instruction_2.pack()
    CANVAS = tk.Canvas(FRAME, width=WIDTH, height=HEIGHT, highlightthickness=0,highlightbackground="black", relief=tk.FLAT,bg='#8c582d',bd=0)
    CANVAS.pack()
    
    board, response = drawBoard()
    CANVAS.focus_set()
    userAction()
    CANVAS.bind("<space>", lambda _: initGame(board, response))




#Voici le menu pour les deux joueurs , à l'inverse de celui pour un seul joueur     
def select_deux_joueur():
    global FRAME, CANVAS, board, response, NB_OF_GUESS, HEIGHT, NB_PLAYER
    NB_PLAYER = 2
    NB_OF_GUESS = 1
    HEIGHT = NB_OF_GUESS*55+70
    FRAME = tk.Toplevel(ROOT)
    CANVAS = tk.Canvas(FRAME, width=WIDTH, height=HEIGHT, highlightthickness=0,highlightbackground="black", relief=tk.FLAT,bg='#8c582d',bd=0)
    CANVAS.pack()
    board, response = drawBoard()
    CANVAS.focus_set()
    userAction()
    choix_joueur = tk.Label(FRAME, text="Choisser la combinaison",fg='brown')
    choix_joueur.pack()
ROOT = tk.Tk()
selection_joueur()
ROOT.mainloop()