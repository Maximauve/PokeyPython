import random

# * Définition du packet
signes = ("coeur", "carreau", "pique", "trefle")
deck = []

for signe in signes:
    for valeur in range(1, 14):
        deck.append((valeur, signe))

random.shuffle(deck)


def Hand():  # * Définition de la main
    main = ["", ""]
    for y in range(2):
        main[y] = deck[0]
        deck.pop(0)
    return main


cardsOnTable = ["", "", "", "", ""]
trash = []


def Flop():
    trash.append(deck[0])
    deck.pop(0)
    for y in range(3):
        cardsOnTable[y] = deck[0]
        deck.pop(0)
    print(
        f"les trois premières carte tirées sont : {cardsOnTable[0]}, {cardsOnTable[1]}, {cardsOnTable[2]}")
    print('\n')


def Turn():
    trash.append(deck[0])
    deck.pop(0)
    cardsOnTable[3] = deck[0]
    deck.pop(0)
    print(
        f"Les cartes présentes sur la Table sont : {cardsOnTable[0]}, {cardsOnTable[1]}, {cardsOnTable[2]}, {cardsOnTable[3]}")
    print('\n')


def River():
    trash.append(deck[0])
    deck.pop(0)
    cardsOnTable[4] = deck[0]
    deck.pop(0)
    print(f"Les cartes présentes sur la Table sont : {cardsOnTable}")
    print('\n')


def All():
    Flop()
    # time.sleep(1)
    Turn()
    # time.sleep(1)
    River()
    # time.sleep(1)


def round2():
    Turn()

    River()

    # * COMBINAISONS :

    # * LA PAIRE : Si vous possédez deux cartes identiques.
    # * ATTENTION: Si deux joueurs finissent une manche avec chacun une paire c’est celui qui aura la carte la plus forte qui remporte le pot.
    # * Exemple: entre une paire de 6 et une paire de roi, c’est celui qui a la paire de roi qui gagne.
    # * LA DOUBLE PAIRE: Si vous possédez deux paires de cartes.
    # * LE BRELAN: Vous possédez un brelan, si vous avez trois cartes identiques.
    # * LA QUINTE OU SUITE: Vous possédez une suite, si cinq cartes de couleurs différentes se suivent.
    # * LA COULEUR: Vous possédez une couleur si vous avez avec votre main et les cinq cartes de la table, cinq cartes de la même couleur. C’est-à-dire 5 carreaux, cinq cœurs, cinq piques ou cinq trèfles.
    # * LE FULL: Vous possédez 3 cartes identiques ainsi qu’une paire.
    # * LE CARRE: Vous possédez 4 cartes identiques.
    # * QUINTE FLUSH: Vous avez cette combinaison à partir du moment où vous avez cinq cartes qui se suivent(LA SUITE) qui sont de même couleur(LA COULEUR).
    # * QUINTE FLUSH ROYALE: Cette combinaison est la plus forte que vous puissiez avoir. Pour avoir une quinte flush royal il faut les cinq plus grosses cartes du jeu qui se suivent c’est-à-dire: l’as, le roi, la dame, le valet et le 10, et que c’est cinq cartes soient d’une seule et même couleur.
