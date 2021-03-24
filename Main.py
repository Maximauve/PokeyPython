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
for _ in range(nbPlayer):
    currentPlayer = game.currentPlayer()
    game.promptCards(currentPlayer)
    print("\n")
    currentPlayer = game.nextPlayer()

Print.startGame()

# * Boucle principale du jeu
n = 1
while nbPlayer > 0:
    game.wakeUp()

    Print.nbRound(n)

    table.Ante(game)
    table.Choice(game)

    if game.checkAllIn():
        table.allInTotal(1, game, end)
        continue

    Shuffle.Flop()
    table.Choice(game)

    if game.checkAllIn():
        table.allInTotal(2, game, end)
        continue

    Shuffle.Turn()
    table.Choice(game)

    if game.checkAllIn():
        table.allInTotal(3, game, end)
        continue

    Shuffle.River()
    table.Choice(game)

    Print.endOfRound()

    for _ in range(nbPlayer):
        currentPlayer.showAllCards()
    end.finalCheck(game)
    end.whoWon(game)

    n += 1
