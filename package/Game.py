from .Players import Player
from .Shuffle import Hand


class Whole_Game:
    def __init__(self):
        self.players = []
        self.currentplayer = 0

    def Count(self):
        return len(self.players)

    def initGame(self):
        available = False
        players = []
        while available == False:
            nb_players = input("Combien de joueurs ? (entre 2 et 4) : ")
            nb_players = int(nb_players)
            if nb_players < 2 or nb_players > 4:
                print("Nombre de joueurs invalide\nRéessayez !")
            else:
                available = True
        if nb_players >= 2:
            players = players + [Player(
                input("Nom du joueur 1: "), Hand())]
            players = players + [Player(
                input("Nom du joueur 2: "), Hand())]
        if nb_players >= 3:
            players = players + [Player(
                input("Nom du joueur 3: "), Hand())]
        if nb_players == 4:
            players = players + [Player(
                input("Nom du joueur 4: "), Hand())]
        self.players = players

    def CurrentPlayer(self):
        self.currentplayer = self.currentplayer % len(self.players)
        return self.players[self.currentplayer]

    def NextPlayer(self):
        self.currentplayer = self.currentplayer % len(self.players)
        self.currentplayer += 1
        return self.players[self.currentplayer]

    def Show_Cards(self, player):
        validAns = False
        while validAns == False:
            confirm = input(
                player.name + ", Voulez vous voir vos cartes? (yes/no)")
            if confirm == "yes" or confirm == "oui" or confirm == "ok":
                player.info()
                validAns = True
            elif confirm == "no" or confirm == "non":
                print("Vous n'avez pas voulu voir vos cartes.")
                validAns = True
            else:
                print(
                    "Erreur, vous n'avez pas saisi \"yes\" ou \"no\". Veuillez réessayer")

    def Round(self, nb):
        self.currentplayer = len(self.players)
        nbround = 0
        end = False
        while end == False:
            if nb == 1:
                #	Mise en forme de petite/grosse blinde
                print(self.players[self.CurrentPlayer()
                                   ].name + "A vous de jouer !")
                self.Show_Cards(self.CurrentPlayer())

            # elif nb == 2:

            # elif nb == 3:

            # elif nb == 4:

            self.currentplayer = self.currentplayer + 1
            nbround = nbround + 1


#! Tour 1:
#! Joueur 1 et 2 mettent petites et grosses blindes
#! Current player -> a vous
#! Voulez vous voir vos cartes? -> Show_Cards
#! commence au troisième joueur --> il suit ou relance ou se couche
#! joueur suivant --> check ou suivre ou relance ou se coucher
#! joueur de petite blinde --> suivre ou se coucher


# * après dernier joueur --> cartes tirées (fontion Flop)


# tour 2:
# same jusqu'à carte tirée --> qu'une seule cette fois ci (fonction Turn)
#

# currentplayer = len(self.players)
# currentplayer = currentplayer % len(self.players)
# return currentplayer
