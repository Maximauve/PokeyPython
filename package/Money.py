from .Players import Player
from .Game import wholeGame
from .Shuffle import *
from .Print import *


class table:
    def __init__(self, money=0, currentBet=0):
        self.money = money
        self.currentBet = currentBet

    def Ante(self, game):  # * Petite blinde / Grosse blinde
        currentPlayer = game.currentPlayer()
        print(currentPlayer.name)
        print(game.nextPlayer().name)
        if currentPlayer.wallet > 10:
            print(
                f"{currentPlayer.name}, vous êtes de petite blinde, vous mettez donc 10€ sur la table.")
            currentPlayer.wallet -= 10
            self.currentBet = 10
            self.money += 10
        else:
            print(f"{currentPlayer.name}, comme vous n'avez pas assez d'argent pour la petite blinde, vous n'avez pas d'autre choix que de faire un tapis")
            self.allIn(currentPlayer)
        if game.nextPlayer().wallet > 10:
            print(
                f"{game.nextPlayer().name}, vous êtes de grosse blinde, vous mettez donc 20€ sur la table.")
            game.nextPlayer().wallet -= 20
            self.currentBet = 20
            self.money = 20
        else:
            print(f"{game.nextPlayer()}, comme vous n'avez pas assez d'argent pour la petite blinde, vous n'avez pas d'autre choix que de faire un tapis")
            self.allIn(game.nextPlayer())

    def Bet(self, player):  # * Mise initiale
        bet = 0
        while bet <= self.currentBet:
            bet = input(f"{player.name}, Combien voulez vous miser ? :")
            try:
                bet = int(bet)
            except ValueError:
                print("Vous n'avez pas entré de nombre.\nRéessayez !")
                bet = 0
                continue
        player.wallet -= bet
        self.money += bet
        self.currentBet = bet
        print(f"{player.name}, vous avez misé {self.currentBet}€")

    def Call(self, player):  # * Suivre
        player.wallet -= self.currentBet
        self.money += self.currentBet
        print(f"Vous suivez la mise précédente qui est de {self.currentBet}€.")

    def Raise(self, player):  # * Relancer
        currentRaise = 0
        while currentRaise <= self.currentBet:
            currentRaise = input(
                f"{player.name}, Combien voulez vous relancer ? :")
            try:
                currentRaise = int(currentRaise)
            except ValueError:
                print("Vous n'avez pas entré de nombre.\nRéessayez !")
                currentRaise = 0
                continue
        player.wallet -= currentRaise
        self.money += currentRaise
        self.currentBet = currentRaise

    def Check(self, player):  # * Check
        print(f"Vous continuez à jouer")

    def allIn(self, player):  # * Tapis
        if player.wallet >= self.currentBet:
            self.currentBet = player.wallet
        self.money += player.wallet
        player.wallet -= player.wallet
        player.allIn = True

    def Fold(self, player):  # * Se coucher
        print(f"Vous vous couchez")
        player.status = False

    def Choice(self, game):
        player = game.currentPlayer()
        nbPlayer = game.Count()
        rep = ""
        while player.status == False:
            player = game.nextPlayer()
        for _ in range(nbPlayer):
            roundPlayer(player)
            if self.currentBet == 0:
                print("Il n'y a pas encore de mise . Vous pouvez choisir de miser(\"mise\"), de ne rien faire(\"check\"), de faire tapis (\"allin\") ou de vous coucher (\"se coucher\") ")
                print(f"Vous possédez {player.wallet}€ .")
                while rep != "mise" or rep != "check" or rep != "tapis" or rep != "se coucher":
                    rep = input("Que désirez vous faire ? : ")
                    if rep == "mise":
                        self.Bet(player)
                    elif rep == "check":
                        self.Check(player)
                    elif rep == "tapis":
                        self.allIn(player)
                    elif rep == "se coucher":
                        self.Fold(player)
                    else:
                        print(
                            "mauvaise réponse! veuillez entrer \"mise\", \"check\", \"tapis\" ou \"se coucher\" : ")

            else:
                print(
                    f"La mise est actuellement de {self.currentBet} €. Vous pouvez choisir de suivre (\"suivre\"), de relancer (\"relance\"), de faire tapis (\"tapis\") ou de vous coucher (\"se coucher\")")
                print(f"Vous possédez {player.wallet}€ .")
                while rep != "relance" or rep != "tapis" or rep != "se coucher" or rep != "suivre":
                    rep = input("Que désirez vous faire ? : ")
                    if rep == "relance":
                        self.Raise(player)
                        break
                    elif rep == "tapis":
                        self.allIn(player)
                        break
                    elif rep == "se coucher":
                        self.Fold(player)
                        break
                    elif rep == "suivre":
                        self.Call(player)
                        break
                    else:
                        print(
                            "mauvaise réponse! veuillez entrer \"suivre\", \"relance\", \"tapis\" ou \"se coucher\"")
            player = game.nextPlayer()

    def allInTotal(self, nbRound, game, end):
        nbPlayer = game.Count()
        currentPlayer = game.currentPlayer()
        for _ in range(nbPlayer):
            currentPlayer.showAllCards()
        if nbRound == 1:
            All()
        elif nbRound == 2:
            round2()
        elif nbRound == 3:
            River()
        end.finalCheck(game)
        end.whoWon(game)
