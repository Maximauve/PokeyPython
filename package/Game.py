from .Players import Player
from .Shuffle import Hand


class Whole_Game:
    def __init__(self):
        self.players = []
        self.currentplayer = 0

    def Count(self):
        return len(self.players)

    def initGame(self):
        nb_players = 1
        players = []
        while nb_players < 2 or nb_players > 4:
            nb_players = input("Combien de joueurs ? (entre 2 et 4) : ")
            try:
                nb_players = int(nb_players)
            except ValueError:
                print("Vous n'avez pas entré de nombre.\nRéessayez !")
                nb_players = 1
                continue
            if nb_players < 2 or nb_players > 4:
                print("Nombre de joueurs invalide\nRéessayez !")

        for a in range(nb_players):
            players += [Player(input(f"Nom du joueur {a+1}: "), Hand())]
        self.players = players
        return nb_players

    def CurrentPlayer(self):
        self.currentplayer = self.currentplayer % len(self.players)
        return self.players[self.currentplayer]

    def NextPlayer(self):
        self.currentplayer += 1
        self.currentplayer = self.currentplayer % len(self.players)
        return self.players[self.currentplayer]

    def Show_Cards(self, player):
        validAns = False
        while validAns == False:
            confirm = input(
                player.name + ", Voulez vous voir vos cartes? (yes/no)")
            if confirm == "yes" or confirm == "oui" or confirm == "ok" or confirm == "y" or confirm == "Y":
                player.info()
                validAns = True
            elif confirm == "no" or confirm == "non" or confirm == "n" or confirm == "N":
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


#! Deuxieme TOUR :

#! Check, le joueur peut cheker c’est-à-dire qu’il ne mise pas de somme supplémentaire dans le pot. Il peut cheker seulement si les joueurs d’avant n’ont pas misé eux non plus.
#! Miser, il décide de mettre dans le pot la somme qu’il souhaite.
#! Relancer, c’est-à-dire miser une somme plus importante si un joueur a déjà misé.
#! Suivre, si un joueur a déjà misé, vous égalisé cette mise dans le pot.
#! Se coucher. Il jette alors ses cartes et se retire définitivement de la partie
