from .Players import Player
from .Game import Whole_Game

g = Whole_Game
call = 0


class Table:
    def __init__(self, money):
        self.money = money

    def Ante(self):  # * Petite blinde / Grosse blinde
        if g.CurrentPlayer().pocket > 10:
            print(
                f"{g.CurrentPlayer()}, vous êtes de petite blinde, vous mettez donc 10$ sur la table.")
            g.CurrentPlayer().pocket -= 10
            self.money += 10
        else:
            print(f"{g.CurrentPlayer(Player)}, comme vous n'avez pas assez d'argent pour la petite blinde, vous n'avez pas d'autre choix que de faire un tapis")
            self.All_In(g.CurrentPlayer(Player))
        if g.NextPlayer().pocket > 10:
            print(
                f"{g.NextPlayer()}, vous êtes de grosse blinde, vous mettez donc 20$ sur la table."
            # ?                                                                                                     Faut vraiment trouver ce problème là
            g.NextPlayer().pocket -= 10
            self.money += 10
        else:
            print(f"{g.NextPlayer()}, comme vous n'avez pas assez d'argent pour la petite blinde, vous n'avez pas d'autre choix que de faire un tapis")
            All_In(g.NextPlayer())

    def Bet(self, player):  # * Mise initiale
        player=g.CurrentPlayer(Player)
        mise=input(f"{player}, Combien voulez vous miser? : ")
        player.pocket -= mise
        self.money += mise
        print(f"{player}, vous avez misé {mise}$")

    def Call(self, player):  # * Suivre
        player=g.CurrentPlayer(Player)
        print(f"Vous suivez la mise précédente qui est de {call}$.")

    def Raise(self, player):  # * Relancer
        player=g.CurrentPlayer(Player)

    def Check(self, player):  # * Check
        player=g.CurrentPlayer(Player)

    def All_In(self, player):  # * Tapis
        player=g.CurrentPlayer(Player)

    def Fold(self, player):  # * Se coucher
        player=g.CurrentPlayer(Player)
