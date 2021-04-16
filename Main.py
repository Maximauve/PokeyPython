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
while nbPlayer > 1:

    tab = []
    for i, _ in enumerate(game.sleepingPlayers()):
        tab.append(game.sleepingPlayers()[i])
    for player in tab:
        game.wakeUp(player)
        for _ in range(nbPlayer):
            currentPlayer.allIn = False
            game.nextPlayer()
            currentPlayer = game.currentPlayer()

    Print.nbRound(n)

    table.Ante(game)
    table.Choice(game)

    if game.checkAllIn():
        table.allInTotal(1, game, end)
        end.finalCheck(game)
        end.whoWon(game, table.totalMoney())

    else:
        Shuffle.Flop()
        table.Choice(game)

        if game.checkAllIn():
            table.allInTotal(2, game, end)
            end.finalCheck(game)
            end.whoWon(game, table.totalMoney())

        else:
            Shuffle.Turn()
            table.Choice(game)

            if game.checkAllIn():
                table.allInTotal(3, game, end)
                end.finalCheck(game)
                end.whoWon(game, table.totalMoney())

            else:
                Shuffle.River()
                table.Choice(game)

                Print.endOfRound()

                for _ in range(nbPlayer):
                    currentPlayer.showAllCards()
                    game.nextPlayer()
                    currentPlayer = game.currentPlayer()
                end.finalCheck(game)
                end.whoWon(game, table.totalMoney())

    for a in range(nbPlayer):
        if currentPlayer.wallet == 0:
            nbPlayer -= 1
            print(
                f"{currentPlayer.name}, vous n'avez malheureusement plus d'argent, vous quittez donc la partie.")
            game.Kill(currentPlayer)
        game.nextPlayer()
        currentPlayer = game.currentPlayer()

    n += 1

print("Fin de Partie, merci d'avoir joué, à très bientôt! :D")
