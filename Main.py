import asyncio
import os
import time
import sys
from package.Game import wholeGame
from package.Players import Player
from package import Shuffle
from package.Ending import endGame
from package.Money import table
from package import Print

table = table()
end = endGame()
game = wholeGame()

# * Initialisation de la partie
nbPlayer = game.initGame()
currentPlayer = game.currentPlayer()
for a in range(nbPlayer):
    game.promptCards(currentPlayer)
    print("\n")
    game.nextPlayer()
    currentPlayer = game.currentPlayer()

Print.startGame()

# * Boucle principale du jeu
n = 1
while nbPlayer > 0:

    for a in [1, 2]:
        print(a)

    tab = game.sleepingPlayers()
    print(tab)
    print(len(tab))
    for player in tab:
        print(f"{player.name} va être réveillé")
        game.wakeUp(player)

    Print.nbRound(n)

    table.Ante(game)
    table.Choice(game)

    if game.checkAllIn():
        print("DEBUG --> checkAllIn n°1")
        table.allInTotal(1, game, end)
        continue

    Shuffle.Flop()
    table.Choice(game)

    if game.checkAllIn():
        print("DEBUG --> checkAllIn n°2")
        table.allInTotal(2, game, end)
        continue

    Shuffle.Turn()
    table.Choice(game)

    if game.checkAllIn():
        print("DEBUG --> checkAllIn n°3")
        table.allInTotal(3, game, end)
        continue

    Shuffle.River()
    table.Choice(game)

    Print.endOfRound()

    for _ in range(nbPlayer):
        currentPlayer.showAllCards()
        game.nextPlayer()
        currentPlayer = game.currentPlayer()
    end.finalCheck(game)
    end.whoWon(game)

    n += 1
