import asyncio
import os
from package.Game import Whole_Game
from package.Players import Player
from package import Shuffle
from package.Ending import EndGame

game = Whole_Game()
end = EndGame()

for _ in range(game.initGame()):
    Current_P = game.CurrentPlayer()
    game.Show_Cards(Current_P)
    print("\n")
    game.CurrentPlayer().info
    Current_P = game.NextPlayer()

# Shuffle.Flop()
# Shuffle.Turn()
# Shuffle.River()

# end.Paire(Current_P)
end.DoublePaire(Current_P)
#end.Brelan(Current_P)

# td     - Faire l'ordre de jeu (player 1: <action>, etc...)
# td     - Choix entre (Check, Relance, Suivre, Tapis, Se Couche)
# td     - Système de mise
# td     - Définir les combos de cartes (paire, brelan, etc...)
# td     -
# td     -
