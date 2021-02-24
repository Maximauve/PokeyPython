from .Players import Player
from .Game import Whole_Game as g

call = 0
currentBet = 0


class table:
    def __init__(self, money, currentBet):
        self.money = money
        self.currentBet = currentBet
        self.coucher = False

    def Ante(self):  # * Petite blinde / Grosse blinde
        if g.currentPlayer().wallet > 10:
            print(
                f"{g.currentPlayer()}, vous êtes de petite blinde, vous mettez donc 10$ sur la table.")
            g.currentPlayer().wallet -= 10
            self.currentBet = 10
            self.money += 10
        else:
            print(f"{g.currentPlayer()}, comme vous n'avez pas assez d'argent pour la petite blinde, vous n'avez pas d'autre choix que de faire un tapis")
            self.allIn(g.currentPlayer())
        if g.nextPlayer().wallet > 10:
            print(
                f"{g.nextPlayer()}, vous êtes de grosse blinde, vous mettez donc 20$ sur la table.")
            g.nextPlayer().wallet -= 20
            self.currentBet = 20
            self.money += 20
        else:
            print(f"{g.nextPlayer()}, comme vous n'avez pas assez d'argent pour la petite blinde, vous n'avez pas d'autre choix que de faire un tapis")
            self.allIn(g.nextPlayer())

    def Bet(self, player):  # * Mise initiale
        player = g.currentPlayer()
        bet = 0
        while bet <= self.currentBet:
            bet = input(f"{player}, Combien voulez vous miser ? :")
            try:
                bet = int(bet)
            except ValueError:
                print("Vous n'avez pas entré de nombre.\nRéessayez !")
                bet = 0
                continue
        player.wallet -= bet
        self.money += bet
        self.currentBet = bet
        print(f"{player}, vous avez misé {self.currentBet}$")

    def Call(self, player):  # * Suivre
        player = g.currentPlayer()
        call = self.currentBet
        player.wallet -= call
        self.money += call
        print(f"Vous suivez la mise précédente qui est de {call}$.")

    def Raise(self, player):  # * Relancer
        player = g.currentPlayer()
        currentRaise = 0
        while currentRaise <= self.currentBet:
            currentRaise = input(f"{player}, Combien voulez vous relancer ? :")
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
        player = g.currentPlayer()
        print(f"Vous continuez à jouer")


#!                  All in
# td -       Une fois le All in en route, la "boucle de partie" s'arrête pour laisser place au All in
# td -       Les joueurs peuvent soit suivre le All in (s'ils n'ont pas l'argent mais qu'ils veulent quand même suivre, ça déclenche aussi un All in), relancer ou alors  se coucher
# td -       Le All in montre les cartes de tous les adversaires
# td -       Si un All in se fait avant le flop, le turn ou le river, alors ils sont mis après que les cartes se soient montrées
# td -
# td -
# td -


    def allIn(self, player):  # * Tapis
        player = g.currentPlayer()
        if player.wallet >= self.currentBet:
            self.currentBet = player.wallet
        self.money += player.wallet
        player.wallet -= player.wallet

    def Fold(self, player):  # * Se coucher
        player = g.currentPlayer()
        print(f"Vous vous couchez")
        self.coucher.player = True
