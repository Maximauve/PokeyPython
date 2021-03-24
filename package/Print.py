def startGame():
    print("""
	o--------------------o
	| DEBUT DE LA PARTIE |
	o--------------------o
	""")


def nbRound(n):
    print(f"""\n
	o------------o
	| MANCHE {n}   |
	o------------o
	""")


def roundPlayer(joueur):
    phrase = ""
    phrase += "| " + joueur.name + ", c'est à vous !" + \
        int(27-len(joueur.name))*' ' + "|"
    print(f'''
    o--------------------------------------------o
    {phrase}
    o--------------------------------------------o
    ''')


def endOfRound():
    print('''
   o---------------------------------o
   | FIN DE TOUR -- VERIF DES CARTES |
   o---------------------------------o
    ''')
