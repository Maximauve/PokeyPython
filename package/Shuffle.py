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


def Hand():  # * Définition de la main
    main = ["", ""]
    for y in range(2):
        main[y] = deck[0]
        deck.pop(0)
    return main


cardsOnTable = ["", "", "", "", ""]
trash = []


def Flop():
    printFlop()
    trash.append(deck[0])
    deck.pop(0)
    for y in range(3):
        cardsOnTable[y] = deck[0]
        deck.pop(0)
    print(
        f"les trois premières carte tirées sont : {cardsOnTable[0]}, {cardsOnTable[1]}, {cardsOnTable[2]}")
    print('\n')


def Turn():
    printTurn()
    trash.append(deck[0])
    deck.pop(0)
    cardsOnTable[3] = deck[0]
    deck.pop(0)
    print(
        f"Les cartes présentes sur la Table sont : {cardsOnTable[0]}, {cardsOnTable[1]}, {cardsOnTable[2]}, {cardsOnTable[3]}")
    print('\n')


def River():
    printRiver()
    trash.append(deck[0])
    deck.pop(0)
    cardsOnTable[4] = deck[0]
    deck.pop(0)
    print(f"Les cartes présentes sur la Table sont : {cardsOnTable}")
    print('\n')


def All():
    Flop()
    time.sleep(1)
    Turn()
    time.sleep(1)
    River()
    time.sleep(1)


def round2():
    Turn()
    time.sleep(1)
    River()
