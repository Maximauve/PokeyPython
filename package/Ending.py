from .Shuffle import table
from .Game import Whole_Game
g = Whole_Game()


class EndGame:
    def __init__(self, tab=table):
        self.tab = tab

    def CheckCards(self, player):
        check = []
        for a in range(5):
            check.append(self.tab[a])
        for i in range(2):
            check.append(player.hand[i])
        # * Debug
        print(check)
        print('\n')
        return check

    def NumberCheck(self, deck):
        number = []
        for a in range(len(deck)):
            number.append(deck[a][0])
        return number

    def PowerCheck(self, deck):
        power = []
        for a in range(len(deck)):
            power.append(deck[a][1])
        return power

    def Paire(self, player):
        number = self.NumberCheck(self.CheckCards(player))
        for i in range(len(number)-1):
            for y in range(len(number)-1):
                if number[i] - number[y] == 0:
                    if i != y:
                        print(
                            f"Vous avez une paire de {number[i]} !")
                        if number[i] == 1:
                            return 13
                        else:
                            return number[i] - 1

    def DoublePaire(self, player):
        # number = self.NumberCheck(self.CheckCards(player))
        number = [2, 1, 7, 5, 7, 2, 5]
        dblnumber = number
        pair = []
        poped = 0
        for _ in range(2):
            print("range")
            for i in range(len(dblnumber)-poped):
                for y in range(len(dblnumber)-poped):
                    if number[i] - number[y] == 0:
                        if i != y:
                            if i > y:
                                dblnumber.pop(i)
                                dblnumber.pop(y)
                                poped = 2
                            else:
                                dblnumber.pop(y)
                                dblnumber.pop(i)
                                poped = 2
                            break
                if poped == 2:
                    break
        # print(dblnumber)
        if len(dblnumber) == 3:
            for i in range(3):
                for y in range(3):
                    if number[i] - number[y] == 0:
                        if i != y:
                            pair.append(dblnumber[i])
                            dblnumber.pop(i)
                            dblnumber.pop(y)
            print(dblnumber)
            if len(dblnumber) == 1:
                pair.sort()
                if pair[0] == 1:
                    pair.pop(1)
                else:
                    pair.pop(0)
                print(f"Vous avez une paire de {pair[0]} et de {pair[1]} !")
            else:
                print(f"Vous avez une paire de {pair[0]} et de {pair[1]} !")

            print(number)
            print(dblnumber)
            print(pair)
            if 1 in pair:
                return 25
            else:
                return (pair[1] + 11)
        else:
            return 0

    def Brelan(self, player):
        number = [1, 7, 5, 7, 1, 7, 2]
        numbertrié = number.sort()
        brelan = []
        # number = self.NumberCheck(self.CheckCards(player))
        for _ in range(2):
            for i in range(len(numbertrié)):
                for y in range(len(numbertrié)):
                    for x in range(len(numbertrié)):
                        if number[i] == number[y]:
                            if number[i] == number[x]:
                                if i != y != x:
                                    brelan.append(numbertrié[i])
                                    numbertrié.pop(x)
                                    numbertrié.pop(y)
                                    numbertrié.pop(i)
                                    print(numbertrié)
                                    break
                if len(numbertrié) == 4:
                    break
        print(".")
        if len(numbertrié) == 4:
            pass
        else:
            return 0

    # def Suite(self):

    # def Couleur(self):

    # def Full(self):

    # def Carre(self):

    # def QuinteFlush(self):

    # def QuinteFlushRoyale(self) int:
    # for a in len(number):

    # return 89

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
