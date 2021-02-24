
# td     - Faire l'ordre de jeu (player 1: <action>, etc...)
# td     - Choix entre (Check, Relance, Suivre, Tapis, Se Couche)
# td     - Système de mise
# td     -
# td     -
# td     -


import asyncio
import os
import time
from package.Game import wholeGame as game
from package.Players import Player
from package import Shuffle
from package.Ending import endGame as end
from package.Money import table


nbPlayer = game.initGame()

for _ in range(nbPlayer):
    currentPlayer = game.currentPlayer()
    game.promptCards(currentPlayer)
    print("\n")
    currentPlayer = game.nextPlayer()


Shuffle.Flop()
# time.sleep(1)
Shuffle.Turn()
# time.sleep(1)
Shuffle.River()
# time.sleep(1)


# *     o---------------------------------o
# *     | FIN DE TOUR -- VERIF DES CARTES |
# *     o---------------------------------o

for _ in range(nbPlayer):

    print(currentPlayer.hand)

    # time.sleep(3)
    if end.royalFlush(currentPlayer):
        print(f"{currentPlayer.name}, Vous avez une Quinte Flush Royale !")

    elif end.straightFlush(currentPlayer):
        # a voir
        print(
            f"{currentPlayer.name}, Vous avez une Quinte Flush de {end.straightFlush(currentPlayer)[1]} !")

    elif end.Quads(currentPlayer):
        print(
            f"{currentPlayer.name}, Vous avez un carré de {end.Quads(currentPlayer)[1]} !")

    elif end.Full(currentPlayer):
        print(
            f"{currentPlayer.name}, Vous avez un full ! Brelan de {end.Full(currentPlayer)[1][0]} et Paire de {end.Full(currentPlayer)[1][1]} !")

    elif end.Flush(currentPlayer):
        print(
            f"{currentPlayer.name}, Vous avez une couleur de {end.Flush(currentPlayer)[2]} !")

    elif end.Straight(currentPlayer):
        print(
            f"{currentPlayer.name}, Vous avez une suite ! Commençant par un {end.Straight(currentPlayer)[1][0]} et finissant par un {end.Straight(currentPlayer)[1][4]} !")

    elif end.Trips(currentPlayer):
        print(
            f"{currentPlayer.name}, Vous avez un Brelan de {end.Trips(currentPlayer)[1]} !")

    elif end.twoPair(currentPlayer):
        print(
            f"{currentPlayer.name}, Vous avez une Double Paire de {end.twoPair(currentPlayer)[1][0]} et de {end.twoPair(currentPlayer)[1][1]} !")

    elif end.Pair(currentPlayer):
        print(
            f"{currentPlayer.name}, Vous avez une Paire de {end.Pair(currentPlayer)[1]} !")

    else:
    else:
    else:
    else:
    else:
    else:
    else:
    else:
    else:
        print(f"{currentPlayer.name}, malheurement vous n'avez pas de main...")

    currentPlayer = game.nextPlayer()
    print("\n\n")
