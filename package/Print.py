

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
    o--------------------------------------------o''')




def endOfRound():
    print('''
   o-----------------------------------o
   | FIN DE MANCHE -- VERIF DES CARTES |
   o-----------------------------------o
    ''')


def printFlop():
    print('''
	o-----------------------------------o
	|               FLOP                |
	o-----------------------------------o
	''')


def printTurn():
    print('''
	o-----------------------------------o
	|               TURN                |
	o-----------------------------------o
	''')


def printRiver():
    print('''
	o-----------------------------------o
	|               RIVER               |
	o-----------------------------------o
	''')

def printTableVide():
	print('''
	o-----------------------------------o
	|  La table est actuellement vide   |
	o-----------------------------------o
	''')

def printTable(cardsOnTable):
	cards = cardsOnTable
	phrase = "La table actuelle est "
	for x in cards:
		phrase += f"{x} "
	print(f'''
    o--------------------------------------------o
    {phrase}
    o--------------------------------------------o
    ''')