import os
import asyncio

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def info(self):
        input(self.name + ", Appuyez sur ENTREE pour visualisez vos cartes")
        print("Vous possédez la main " + self.hand)
        input("Appuyez à nouveau sur ENTREE pour masquer vos cartes")
        os.system('cls' if os.name == 'nt' else 'clear')
