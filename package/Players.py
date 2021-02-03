import os
import asyncio


class Player:
    def __init__(self, name, hand, pocket=1000):
        self.name = name
        self.hand = hand
        self.pocket = pocket

    def info(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        input(self.name + ", Appuyez sur ENTREE pour visualisez vos cartes")
        print('\n')
        print(f"Vous possédez la main {self.hand}")
        print('\n')
        input("Appuyez à nouveau sur ENTREE pour masquer vos cartes")
        os.system('cls' if os.name == 'nt' else 'clear')
