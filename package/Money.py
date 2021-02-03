from .Players import Player
from .Game import Whole_Game

g = Whole_Game()
call = 0
mise = 0


class Table:
    def __init__(self, money, mise):
        self.money = money
        self.mise = mise
        self.coucher = False

    def Ante(self):  # * Petite blinde / Grosse blinde
        if g.CurrentPlayer().pocket > 10:
            print(
                f"{g.CurrentPlayer()}, vous êtes de petite blinde, vous mettez donc 10$ sur la table.")
            g.CurrentPlayer().pocket -= 10
            self.mise = 10
            self.money += 10
        else:
            print(f"{g.CurrentPlayer()}, comme vous n'avez pas assez d'argent pour la petite blinde, vous n'avez pas d'autre choix que de faire un tapis")
            self.All_In(g.CurrentPlayer())
        if g.NextPlayer().pocket > 10:
            print(
                f"{g.NextPlayer()}, vous êtes de grosse blinde, vous mettez donc 20$ sur la table.")
            g.NextPlayer().pocket -= 20
            self.mise = 20
            self.money += 20
        else:
            print(f"{g.NextPlayer()}, comme vous n'avez pas assez d'argent pour la petite blinde, vous n'avez pas d'autre choix que de faire un tapis")
            self.All_In(g.NextPlayer())

    def Bet(self, player):  # * Mise initiale
        player = g.CurrentPlayer()
        bet = 0
        while bet <= self.mise:
            bet = input(f"{player}, Combien voulez vous miser ? :")
            try:
                bet = int(bet)
            except ValueError:
                print("Vous n'avez pas entré de nombre.\nRéessayez !")
                bet = 0
                continue
        player.pocket -= bet
        self.money += bet
        self.mise = bet
        print(f"{player}, vous avez misé {self.mise}$")

    def Call(self, player):  # * Suivre
        player = g.CurrentPlayer()
        call = self.mise
        player.pocket -= call
        self.money += call
        print(f"Vous suivez la mise précédente qui est de {call}$.")

    def Raise(self, player):  # * Relancer
        player = g.CurrentPlayer()
        relance = 0
        while relance <= self.mise:
            relance = input(f"{player}, Combien voulez vous relancer ? :")
            try:
                relance = int(relance)
            except ValueError:
                print("Vous n'avez pas entré de nombre.\nRéessayez !")
                relance = 0
                continue
        player.pocket -= relance
        self.money += relance
        self.mise = relance

    def Check(self, player):  # * Check
        player = g.CurrentPlayer()
        print(f"Vous continuez à jouer")

    def All_In(self, player):  # * Tapis
        player = g.CurrentPlayer()
        if player.pocket > self.mise:
            self.mise = player.pocket
        self.money += player.pocket
        player.pocket -= player.pocket

    def Fold(self, player):  # * Se coucher
        player = g.CurrentPlayer()
        print(f"Vous vous couchez")
        self.coucher.player = True
