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
