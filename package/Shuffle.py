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
    # print(hand)
    # print(f"Votre main est : {main}")
    # print('\n')


table = ["", "", "", "", ""]
trash = []


def Flop():
    trash.append(deck[0])
    deck.pop(0)
    for y in range(3):
        table[y] = deck[0]
        deck.pop(0)
    print(
        f"les tois premières carte tirées sont : {table[0]}, {table[1]}, {table[2]}")
    print('\n')


def Turn():
    trash.append(deck[0])
    deck.pop(0)
    table[3] = deck[0]
    deck.pop(0)
    print(
        f"Les cartes présentes sur la table sont : {table[0]}, {table[1]}, {table[2]}, {table[3]}")
    print('\n')


def River():
    trash.append(deck[0])
    deck.pop(0)
    table[4] = deck[0]
    deck.pop(0)
    print(f"Les cartes présentes sur la table sont : {table}")
    print('\n')


# td Mélanger le paquet dès le début --> donner les cartes dans l'ordre et bruler pour flop, turn et river

class EndGame:
    def __init__(self, cards):
        self.cards = table

    # def Paire(self):

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
