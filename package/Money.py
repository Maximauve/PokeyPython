from .Players import Player
from .Game import wholeGame
from .Shuffle import *
from .Print import *

# td 	--> Pour les blindes : noter qu'ils ont déjà "misés" (la petite blinde a déjà misé 10€, et la grosse 20€)
# td 	--> Le pot, à donner au vainqueur
# td 	-->


class table:
    def __init__(self, money=0, currentBet=0):
        self.money = money
        self.currentBet = currentBet

    def Ante(self, game):  # * Petite blinde / Grosse blinde
        currentPlayer = game.currentPlayer()
        if currentPlayer.wallet > 10:
            print(
                f"{currentPlayer.name}, vous êtes de petite blinde, vous mettez donc 10€ sur la table.")
            currentPlayer.wallet -= 10
            self.currentBet = 10
            self.money += 10
        else:
            print(f"{currentPlayer.name}, comme vous n'avez pas assez d'argent pour la petite blinde, vous n'avez pas d'autre choix que de faire un tapis")
            self.allIn(currentPlayer)
        if game.getNextPlayer().wallet > 10:
            print(
                f"{game.getNextPlayer().name}, vous êtes de grosse blinde, vous mettez donc 20€ sur la table.")
            game.getNextPlayer().wallet -= 20
            self.currentBet = 20
            self.money += 20
        else:
            print(f"{game.getNextPlayer().name}, comme vous n'avez pas assez d'argent pour la petite blinde, vous n'avez pas d'autre choix que de faire un tapis")
            self.allIn(game.getNextPlayer())
        game.nextPlayer()
        game.nextPlayer()

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
            if bet > player.wallet:
                print(
                    "Vous n'avez pas assez d'argent pour miser cette somme!")
                bet = 0
                continue
        if bet == player.wallet:
            print("Vous faites Tapis.")
            self.allin(player)
            return
        player.wallet -= bet
        self.money += bet
        self.currentBet = bet
        print(f"{player.name}, vous avez misé {self.currentBet}€")

    def Call(self, player):  # * Suivre
        if self.currentBet >= player.wallet:
            print(
                f"Vous suivez avec le solde de votre compte qui est de {player.wallet}€.")
            self.allIn(player)
        else:
            player.wallet -= self.currentBet
            self.money += self.currentBet
            print(
                f"Vous suivez la mise précédente qui est de {self.currentBet}€.")

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
            if currentRaise > player.wallet:
                print(
                    "Vous n'avez pas assez d'argent pour miser cette somme!")
                currentRaise = 0
                continue
        player.wallet -= currentRaise
        self.money += currentRaise
        self.currentBet = currentRaise

    def Check(self, player):  # * Check
        print(f"Vous décidez de ne rien faire.")

    def allIn(self, player):  # * Tapis
        if player.wallet >= self.currentBet:
            self.currentBet = player.wallet
        self.money += player.wallet
        player.wallet -= player.wallet
        player.allIn = True

    def Fold(self, game, player):  # * Se coucher
        print(f"Vous vous couchez")
        player.status = False
        game.foldPlayer(player)

    def Choice(self, game):
        player = game.currentPlayer()
        nbPlayer = game.Count()
        rep = ""
        while player.status == False:
            game.nextPlayer()
            player = game.currentPlayer()
        for _ in range(nbPlayer):
            roundPlayer(player)
            if self.currentBet == 0:
                print("Il n'y a pas encore de mise . Vous pouvez choisir de miser(\"mise\"), de ne rien faire(\"check\"), de faire tapis (\"allin\"),de vous coucher (\"se coucher\") ou encore voir vos cartes (\"cartes\") ")
                print(f"Vous possédez {player.wallet}€ .")
                while rep != "mise" or rep != "check" or rep != "tapis" or rep != "se coucher":
                    rep = input("Que désirez vous faire ? : ")
                    if rep == "mise":
                        self.Bet(player)
                        break
                    elif rep == "check":
                        self.Check(player)
                        break
                    elif rep == "tapis":
                        self.allIn(player)
                        break
                    elif rep == "se coucher":
                        self.Fold(game, player)
                        break
                    elif rep == "cartes":
                        player.showCards()
                    else:
                        print(
                            "Mauvaise réponse! veuillez entrer \"mise\", \"check\", \"tapis\", \"se coucher\" ou \"cartes\" ")
            else:
                print(
                    f"La mise est actuellement de {self.currentBet} €. Vous pouvez choisir de suivre (\"suivre\"), de relancer (\"relance\"), de faire tapis (\"tapis\"), de vous coucher (\"se coucher\") ou de voir vos cartes (\"cartes\") ")
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
                        self.Fold(game, player)
                        break
                    elif rep == "suivre":
                        self.Call(player)
                        break
                    elif rep == "cartes":
                        player.showCards()
                    else:
                        print(
                            "Mauvaise réponse! veuillez entrer \"suivre\", \"relance\", \"tapis\", \"se coucher\" ou \"cartes\"")
            game.nextPlayer()
            player = game.currentPlayer()
        self.currentBet = 0

    def allInTotal(self, nbRound, game, end):
        nbPlayer = game.Count()
        currentPlayer = game.currentPlayer()
        for _ in range(nbPlayer):
            currentPlayer.showAllCards()
            game.nextPlayer()
            currentPlayer = game.currentPlayer()
        if nbRound == 1:
            All()
        elif nbRound == 2:
            round2()
        elif nbRound == 3:
            River()
        end.finalCheck(game)
        end.whoWon(game)
