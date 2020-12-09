import os
import asyncio



def Count():
    available = False
    while available == False:
        nb_players = input("Combien de joueurs ? (entre 2 et 4) : ")
        nb_players = int(nb_players)
        if nb_players < 2 or nb_players > 4:
            print("Nombre de joueurs invalide\nRéessayez !")
        else:
            available = True
    return nb_players



#td Réussir cette fontion qui nous hante o_o
def NextPlayers():
    i = 1
    while i <= nb_player:
        variable = i % nb
        i += 1
   

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def info(self):
        input(self.name + ", Appuyez sur ENTREE pour visualisez vos cartes")
        print("Vous possédez la main " + self.hand)
        input("Appuyez à nouveau sur ENTREE pour masquer vos cartes")
        os.system('cls' if os.name == 'nt' else 'clear')
