import asyncio
import os
from package.Game import Whole_Game
from package.Players import Player
from package import Shuffle
from package.Ending import EndGame

game = Whole_Game()
end = EndGame()

for nbp in range(game.initGame()):
    Current_P = game.CurrentPlayer()
    game.Show_Cards(Current_P)
    print("\n")
    game.CurrentPlayer().info
    Current_P = game.NextPlayer()
    nbp += 1

print(end.Suite(Current_P))

# Shuffle.Flop()
# Shuffle.Turn()
# Shuffle.River()


# for _ in range(nbp):

#     print(Current_P.hand)

#     if end.QuinteFlushRoyale(Current_P):
#         print(f"{Current_P.name}, " + end.QuinteFlushRoyale(Current_P)[2])

#     elif end.QuinteFlush(Current_P):
#         print(f"{Current_P.name}, " + end.QuinteFlush(Current_P)[2])

#     elif end.Carre(Current_P):
#         print(f"{Current_P.name}, " + end.Carre(Current_P)[2])

#     elif end.Full(Current_P):
#         print(f"{Current_P.name}, " + end.Full(Current_P)[2])

#     elif end.Couleur(Current_P):
#         print(f"{Current_P.name}, " + end.Couleur(Current_P)[2])

#     elif end.Suite(Current_P):
#         print(f"{Current_P.name}, " + end.Suite(Current_P)[2])

#     elif end.Brelan(Current_P):
#         print(f"{Current_P.name}, " + end.Brelan(Current_P)[2])

#     elif end.DoublePaire(Current_P):
#         print(f"{Current_P.name}, " + end.DoublePaire(Current_P)[2])

#     elif end.Paire(Current_P):
#         print(f"{Current_P.name}, " + end.Paire(Current_P)[2])
#     else:
#         print(f"{Current_P.name}, malheurement vous n'avez pas de main...")

#     Current_P = game.NextPlayer()

# td     - Faire l'ordre de jeu (player 1: <action>, etc...)
# td     - Choix entre (Check, Relance, Suivre, Tapis, Se Couche)
# td     - Système de mise
# td     - Définir les combos de cartes (paire, brelan, etc...)
# td     -
# td     -
