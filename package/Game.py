from .Players import Player
from .Shuffle import Hand

# td Faire NextPlayer (tro bi1)
# td  --> Faire en sorte qu'il ne change jamais, et qu'il se fasse par rapport à currentPlayer


class wholeGame:
    def __init__(self):
        self.players = []
        self.indexPlayer = 0

    def Count(self):
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
            players += [Player(input(f"Nom du joueur {a+1}: "), Hand())]
        self.players = players
        return nbPlayers

    def currentPlayer(self):
        self.indexPlayer = self.indexPlayer % len(self.players)
        return self.players[self.indexPlayer]

    def nextPlayer(self):
        if self.indexPlayer + 1 <= self.Count():
            self.indexPlayer += 1
        else:
            self.indexPlayer += 1
            self.indexPlayer -= self.Count()
        # self.indexPlayer += 1
        # self.indexPlayer = self.indexPlayer % len(self.players)
        return self.players[self.indexPlayer]

    def checkAllIn(self):
        player = self.currentPlayer()
        a = len(self.players)
        compt = 0
        for _ in range(self.Count()):
            if player.allIn == True:
                compt += 1
        if compt == a:
            return True
        return False

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

    def wakeUp(self):
        player = self.currentPlayer()
        for _ in range(self.Count()):
            player.status = True
            player = self.nextPlayer()
