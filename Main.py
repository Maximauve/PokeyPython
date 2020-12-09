import asyncio
import os
from package import Game
from package.Game import Whole_Game
from package.Players import Player


game = Whole_Game()
game.initGame()
game.players[0.info]



# td     - Faire l'ordre de jeu (player 1: <action>, etc...)
# td     - Choix entre (Check, Relance, Suivre, Tapis, Se Couche)
# td     - Système de mise
# td     - Définir les combos de cartes (paire, brelan, etc...)
# td     -
# td     -


# ? Premier TOUR :
# ?
# ? Se coucher. Il jette alors ses cartes et se retire définitivement de la partie.
# ? Suivre la grosse blinde, c’est-à-dire qu’il met dans le pot la même somme que celle déposée par la grosse blinde.
# ? Relancer. Il mise alors une somme supérieure à celle déposée par la grosse blinde.

#! Deuxieme TOUR :

#! Check, le joueur peut cheker c’est-à-dire qu’il ne mise pas de somme supplémentaire dans le pot. Il peut cheker seulement si les joueurs d’avant n’ont pas misé eux non plus.
#! Miser, il décide de mettre dans le pot la somme qu’il souhaite.
#! Relancer, c’est-à-dire miser une somme plus importante si un joueur a déjà misé.
#! Suivre, si un joueur a déjà misé, vous égalisé cette mise dans le pot.
#! Se coucher. Il jette alors ses cartes et se retire définitivement de la partie

# * COMBINAISONS :

# * LA PAIRE : Si vous possédez deux cartes identiques.
# * ATTENTION: Si deux joueurs finissent une manche avec chacun une paire c’est celui qui aura la carte la plus forte qui remporte le pot.
# * Exemple: entre une paire de 6 et une paire de roi, c’est celui qui a la paire de roi qui gagne.
# * LA DOUBLE PAIRE: Si vous possédez deux paires de cartes.
# * LE BRELAN: Vous possédez un brelan, si vous avez trois cartes identiques.
# * LA QUINTE OU SUITE: Vous possédez une suite, si cinq cartes de couleurs différentes se suivent.
# * LA COULEUR: Vous possédez une couleur si vous avez avec votre main et les cinq cartes de la table, cinq cartes de la même couleur. C’est-à-dire 5 carreaux, cinq cœurs, cinq piques ou cinq trèfles.
# * LE FULL: Vous possédez 3 cartes identiques ainsi qu’une paire.
# * LE CARRE: Vous possédez 4 cartes identiques.
# * QUINTE FLUSH: Vous avez cette combinaison à partir du moment où vous avez cinq cartes qui se suivent(LA SUITE) qui sont de même couleur(LA COULEUR).
# * QUINTE FLUSH ROYALE: Cette combinaison est la plus forte que vous puissiez avoir. Pour avoir une quinte flush royal il faut les cinq plus grosses cartes du jeu qui se suivent c’est-à-dire: l’as, le roi, la dame, le valet et le 10, et que c’est cinq cartes soient d’une seule et même couleur.
