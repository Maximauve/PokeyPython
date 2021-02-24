from .Players import Player
from .Shuffle import Hand


class wholeGame:
    def __init__(self):
        self.players = []
        self.currentPlayer = 0

    def count(self):
        return len(self.players)

    def initGame(self):
        nbPlayers = 1
        players = []
        while nbPlayers < 2 or nbPlayers > 4:
            nbPlayers = input("Combien de joueurs ? (entre 2 et 4) : ")
            try:
                nbPlayers = int(nbPlayers)
            except ValueError:
                print("Vous n'avez pas entré de nombre.\nRéessayez !")
                nbPlayers = 1
                continue
            if nbPlayers < 2 or nbPlayers > 4:
                print("Nombre de joueurs invalide\nRéessayez !")

        for a in range(nbPlayers):
            players += [Player(input(f"Nom du joueur {a+1}: "), hand())]
        self.players = players
        return nbPlayers

    def currentPlayer(self):
        self.currentplayer = self.currentplayer % len(self.players)
        return self.players[self.currentplayer]

    def nextPlayer(self):
        self.currentplayer += 1
        self.currentplayer = self.currentplayer % len(self.players)
        return self.players[self.currentplayer]

    def promptCards(self, player):
        validAns = False
        while validAns == False:
            confirm = input(
                player.name + ", Voulez vous voir vos cartes? (oui/non)")
            if confirm == "yes" or confirm == "oui" or confirm == "ok" or confirm == "y" or confirm == "Y":
                player.showCards()
                validAns = True
            elif confirm == "no" or confirm == "non" or confirm == "n" or confirm == "N":
                print("Vous n'avez pas voulu voir vos cartes.")
                validAns = True
            else:
                print(
                    "Erreur, vous n'avez pas saisi \"oui\" ou \"non\". Veuillez réessayer")


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
