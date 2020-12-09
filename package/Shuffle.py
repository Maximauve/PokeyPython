import random

# *                                                                                    Définition du packet
signes = ("coeur", "carreau", "pique", "trefle")
deck = []

for signe in signes:
    for valeur in range(1, 14):
        deck.append((valeur, signe))

def Hand():  # *                                                                       Définition de la main
    main = ["", ""]
    y = 0
    while y < 2:
        x = random.randrange(len(deck)-1)
        main[y] = deck[x]
        deck.pop(x)
        y += 1
    hand = f"{main[0]} et {main[1]}"
    return hand
    # print(hand)
    # print(f"Votre main est : {main}")
    # print('\n')

table = ["", "", "", "", ""]

def Flop():
    y = 0
    while y < 3:
        x = random.randrange(len(deck)-1)
        table[y] = deck[x]
        deck.pop(x)
        y += 1

    print(
        f"les tois premières carte tirées sont : {table[0]}, {table[1]}, {table[2]}")
    print('\n')

def Turn():
    x = random.randrange(len(deck)-1)
    table[3] = deck[x]
    deck.pop(x)
    print(
        f"Les cartes présentes sur la table sont : {table[0]}, {table[1]}, {table[2]}, {table[3]}")
    print('\n')

def River():
    x = random.randrange(len(deck)-1)
    table[4] = deck[x]
    deck.pop(x)
    print(f"Les cartes présentes sur la table sont : {table}")
    print('\n')
