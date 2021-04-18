import random
from .Print import *
import time

# * Définition du packet


def shuffleCards():
    signes = ("coeur", "carreau", "pique", "trefle")
    deck = []
    for signe in signes:
        for valeur in range(1, 14):
            deck.append((valeur, signe))

    random.shuffle(deck)

    return deck


def dealCards(deck, game):  # * Définition de la main
    currentPlayer = game.currentPlayer()

    for _ in range(game.Count()):
        currentPlayer.hand = ["", ""]
        game.nextPlayer()
        currentPlayer = game.currentPlayer()

    for a in range(2):
        for y in range(game.Count()):
            currentPlayer.hand[a] = deck[0]
            deck.pop(0)
            game.nextPlayer()
            currentPlayer = game.currentPlayer()


cardsOnTable = ["", "", "", "", ""]
trash = []


def Flop(deck):
    printFlop()
    trash.append(deck[0])
    deck.pop(0)
    for y in range(3):
        cardsOnTable[y] = deck[0]
        deck.pop(0)
    print(
        f"les trois premières carte tirées sont : {cardsOnTable[0]}, {cardsOnTable[1]}, {cardsOnTable[2]}")
    print('\n')


def Turn(deck):
    printTurn()
    trash.append(deck[0])
    deck.pop(0)
    cardsOnTable[3] = deck[0]
    deck.pop(0)
    print(
        f"Les cartes présentes sur la Table sont : {cardsOnTable[0]}, {cardsOnTable[1]}, {cardsOnTable[2]}, {cardsOnTable[3]}")
    print('\n')


def River(deck):
    printRiver()
    trash.append(deck[0])
    deck.pop(0)
    cardsOnTable[4] = deck[0]
    deck.pop(0)
    print(f"Les cartes présentes sur la Table sont : {cardsOnTable}")
    print('\n')


def All(deck):
    Flop(deck)
    time.sleep(1)
    Turn(deck)
    time.sleep(1)
    River(deck)
    time.sleep(1)


def round2(deck):
    Turn(deck)
    time.sleep(1)
    River(deck)
