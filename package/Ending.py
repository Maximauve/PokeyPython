from .Shuffle import table
from .Game import Whole_Game
g = Whole_Game()

# td Ne pas faire de print dans les fonctions de vérifications de cartes --> Ne retourner que la valeur
# td Les prints devront se faire par rapport à la valeure retournée (ex: si c'est un 5 qui est retourné, alors on sait que c'est une paire de 6)


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
        number = self.NumberCheck(self.CheckCards(player))
        dblnumber = number
        pair = []
        poped = False
        for nb in range(2):
            if nb == 1:
                poped = False
            for i in range(len(dblnumber)):
                for y in range(len(dblnumber)):
                    if dblnumber[i] - dblnumber[y] == 0:
                        if i != y:
                            if i > y:
                                pair.append(dblnumber[i])
                                dblnumber.pop(i)
                                dblnumber.pop(y)
                                poped = True
                            else:
                                pair.append(dblnumber[i])
                                dblnumber.pop(y)
                                dblnumber.pop(i)
                                poped = True
                            break
                if poped == True:
                    break
        if len(dblnumber) == 3:
            poped = False
            for i in range(len(dblnumber)):
                for y in range(len(dblnumber)):
                    if dblnumber[i] - dblnumber[y] == 0:
                        if i != y:
                            if i > y:
                                pair.append(dblnumber[i])
                                dblnumber.pop(i)
                                dblnumber.pop(y)
                                poped = True
                            else:
                                pair.append(dblnumber[i])
                                dblnumber.pop(y)
                                dblnumber.pop(i)
                                poped = True
                            break
                if poped == True:
                    break
            if len(pair) == 3:
                pair.sort()
                if pair[0] == 1:
                    pair[0], pair[1], pair[2] = pair[1], pair[2], pair[0]
                print(
                    f"Vous avez deux paires ! Une paire de {pair[1]} et de {pair[2]}")
                if pair[2] == 1:
                    pair[2] = 14
                return pair[2] + 11
            elif len(pair) == 2:
                pair.sort()
                if pair[0] == 1:
                    pair[0], pair[1] = pair[1], pair[0]
                print(
                    f"Vous avez deux paire ! Une paire de {pair[0]} et de {pair[1]}")
                if pair[1] == 1:
                    pair[1] = 14
                return pair[1] + 11
            else:
                return 0
        else:
            return 0

    def Brelan(self, player):
        number = self.NumberCheck(self.CheckCards(player))
        numbertrié = number
        brelan = []
        poped = False
        for nb in range(2):
            if nb == 1:
                poped = False
            for i in range(len(numbertrié)):
                for y in range(len(numbertrié)):
                    for x in range(len(numbertrié)):
                        if numbertrié[i] == numbertrié[y]:
                            if numbertrié[i] == numbertrié[x]:
                                if i != y and i != x and y != x:
                                    brelan.append(numbertrié[i])
                                    tab = [x, y, i]
                                    tab.sort()
                                    numbertrié.pop(tab[2])
                                    numbertrié.pop(tab[1])
                                    numbertrié.pop(tab[0])
                                    poped = True
                                    if nb == 1:
                                        continue
                                    break
                    if poped == True:
                        break
                if poped == True:
                    break
        brelan.sort()
        if len(brelan) > 1:
            if brelan[0] > brelan[1]:
                brelan[0], brelan[1] = brelan[1], brelan[0]
            if brelan[1] == 1:
                brelan[1] = 14
            return brelan[1] + 24
        elif len(brelan) > 0:
            if brelan[0] == 1:
                brelan[0] = 14
            return brelan[0] + 24
        else:
            return 0

    def Full(self, player):

        Brelan = self.Brelan(player)
        Paire = self.Paire(player)
        if Brelan != 0:
            if Paire != 0:
                print("Vous avez un Full !")
                return Brelan + 13
        else:
            return 0

    def Suite(self,player):
        number = self.NumberCheck(self.CheckCards(player))
        numbertrié = number
        numbertrié.sort()
        tab = []
        suite = []
        for i in range(len(numbertrié)-1):
            if numbertrié[i+1] == numbertrié[i]:
                tab.append(i)
        for x in tab:
            numbertrié.pop(x)
        if numbertrié[0] == 1:
            numbertrié.pop(0)
            numbertrié.append(14)
        for i in range(len(numbertrié)-1):
            compt = 0
            nbrange = 5
            if len(numbertrié)-i < 5:
                nbrange = len(numbertrié)-i
            for a in range(nbrange-1):
                if numbertrié[i+1+a] - numbertrié[i+a] == 1:
                    compt += 1
                else:
                    continue
            if compt == 4:
                suite.append(numbertrié[i])
        if len(suite) > 0:
            return suite[len(suite)-1] + 63
        else:
            return 0


    def Couleur(self, player):
        number = self.NumberCheck(self.CheckCards(player))
        power = self.PowerCheck(self.CheckCards(player))
        tabpower = power
        coul = False
        for i in range(len(power)):
            couleur = []
            couleury = []
            for y in range(len(power)):
                if tabpower[i] == tabpower[y] and i != y:
                    couleur.append(tabpower[y])
                    couleury.append(y)
                if len(couleur) == 4:
                    couleur.append(tabpower[i])
                    couleury.append(i)
                    coul = True
                    break
            if coul == True:
                break
        couleur.sort()
        couleury.sort()
        tabnb = []
        if len(couleur) == 5:
            for x in couleury:
                tabnb.append(number[x])
            tabnb.sort()
            if tabnb[0] == 1:
                tabnb[4] = 14
            return tabnb[4] + 72
        else:
            return 0

    def Carre(self,player):
        number = [1,1,1,4,3,9,1]
        nbcarre = number
        nbcarre.sort()
        carre = []
        poped = False
        for i in range(len(nbcarre)):
            compt = 0
            for y in range(len(nbcarre)):
                if nbcarre[i] == nbcarre[y] and i != y:
                    compt += 1
                    if compt == 3:
                        carre.append(nbcarre[i])
                        poped = True
                        break
            if poped == True:
                break
        if len(carre) == 1:
            if carre[0] == 1:
                carre[0] = 14
            return carre[0] + 50
        else:
            return 0

    #def QuinteFlush(self):

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
    # * Couleur : SI DEUX MAINS ONT DEUX COULEURS, celui avec la carte la plus haute l'emporte
    # * LE FULL: Vous possédez 3 cartes identiques ainsi qu’une paire.
    # * LE CARRE: Vous possédez 4 cartes identiques.
    # * QUINTE FLUSH: Vous avez cette combinaison à partir du moment où vous avez cinq cartes qui se suivent(LA SUITE) qui sont de même couleur(LA COULEUR).
    # * QUINTE FLUSH ROYALE: Cette combinaison est la plus forte que vous puissiez avoir. Pour avoir une quinte flush royal il faut les cinq plus grosses cartes du jeu qui se suivent c’est-à-dire: l’as, le roi, la dame, le valet et le 10, et que c’est cinq cartes soient d’une seule et même couleur.