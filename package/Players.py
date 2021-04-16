import os
import asyncio


class Player:
    def __init__(self, name, hand, wallet=1000, allIn=False, points=0, status=True, bet=0):
        self.name = name
        self.hand = hand
        self.wallet = wallet
        self.allIn = allIn
        self.points = points
        self.status = status
        self.bet = bet

    def showCards(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        input(self.name + ", Appuyez sur ENTREE pour visualisez vos cartes")
        print('\n')
        print(f"Vous possédez la main {self.hand}")
        print('\n')
        input("Appuyez à nouveau sur ENTREE pour masquer vos cartes")
        os.system('cls' if os.name == 'nt' else 'clear')

    def showAllCards(self):
        print('\n')
        print(f"{self.name} possède la main {self.hand}")
        print('\n')
