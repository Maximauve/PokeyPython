from .Players import Player
from .Shuffle import Hand

class Whole_Game:
    def __init__(self):
        self.players = []
        self.name = ''

    def Count(self):
        return len(self.players)

    def initGame(self): 
        available = False
        players = []
        while available == False:
            nb_players = input("Combien de joueurs ? (entre 2 et 4) : ")
            nb_players = int(nb_players)
            if nb_players < 2 or nb_players > 4:
                print("Nombre de joueurs invalide\nRéessayez !")
            else:
                available = True
        if nb_players >= 2:
            players = players + [Player(
                input("Nom du joueur 1: "), Hand())]
            players = players + [Player(
                input("Nom du joueur 2: "), Hand())]
        if nb_players >= 3:
            players = players + [Player(
                input("Nom du joueur 3: "), Hand())]
        if nb_players == 4:
            players = players + [Player(
                input("Nom du joueur 4: "), Hand())]
        self.players = players
        name = input("Nom de la partie ? : ")
        self.name = name




    #td Réussir cette fontion qui nous hante o_o
    # def NextPlayers(self):
    #     i = 1
    #     while i <= nb_player:
    #         variable = i % nb
    #         i += 1