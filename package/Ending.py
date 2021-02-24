from .Shuffle import cardsOnTable
from .Game import wholeGame as g


#! Return des fonctions:
# * Value[0] --> Retourne le nombre de points rapportés par la valeure
# * Value[1] --> Retourne la valeure gagnée
# * Value[2] --> Complément (optionnel)


class endGame:
    def __init__(self, tab=cardsOnTable):
        self.tab = tab

    def checkCards(self, player):
        check = []
        for a in range(5):
            check.append(self.tab[a])
        for i in range(2):
            check.append(player.hand[i])
        return check

    def numberCheck(self, deck):
        numbers = []
        for a in range(len(deck)):
            numbers.append(deck[a][0])
        return numbers

    def powerCheck(self, deck):
        power = []
        for a in range(len(deck)):
            power.append(deck[a][1])
        return power

    def Pair(self, player, numbers=None):
        if numbers == None:
            numbers = self.numberCheck(self.checkCards(player))
        sortedNumbers = sorted(numbers, reverse=True)
        if sortedNumbers[5:] == [1, 1]:
            sortedNumbers[5:], sortedNumbers[:5] = sortedNumbers[:5], sortedNumbers[5:]
            return 13, 1, 0
        for i in range(len(sortedNumbers)):
            if i+1 >= len(sortedNumbers):
                break
            if sortedNumbers[i] == sortedNumbers[i+1]:
                return (sortedNumbers[i] - 1), sortedNumbers[i], i
        return None

    def twoPair(self, player):
        numbers = self.numberCheck(self.checkCards(player))
        numberToPop = sorted(numbers, reverse=True)
        if numberToPop[5:] == [1, 1]:
            numberToPop[5:], numberToPop[:5] = numberToPop[:5], numberToPop[5:]
        if self.Pair(player):
            for _ in range(2):
                numberToPop.pop(self.Pair(player)[2])
            res = self.Pair(player, numberToPop)
            if res:
                return self.Pair(player)[0] + 12, [self.Pair(player)[1], res[1]]
            return None

    def Trips(self, player):
        numbers = self.numberCheck(self.checkCards(player))
        sortedNumbers = sorted(numbers, reverse=True)
        if sortedNumbers[4:] == [1, 1, 1]:
            sortedNumbers[4:], sortedNumbers[:4] = sortedNumbers[:4], sortedNumbers[4:]
            return 38, 1, 0
        trips = 0
        for i in range(len(sortedNumbers)-2):
            if sortedNumbers[i] - sortedNumbers[i+1] == 0:
                if sortedNumbers[i+1] - sortedNumbers[i+2] == 0:
                    trips = sortedNumbers[i]
                    break
        if trips:
            return trips + 24, trips, i
        return None

    def Full(self, player):  # a faire apres
        numbers = self.numberCheck(self.checkCards(player))
        numberToPop = sorted(numbers, reverse=True)
        if numberToPop[4:] == [1, 1, 1]:
            numberToPop[4:], numberToPop[:4] = numberToPop[:4], numberToPop[4:]
        if self.Trips(player):
            for _ in range(3):
                numberToPop.pop(self.Trips(player)[2])
            if self.Pair(player, numberToPop):
                return self.Trips(player)[0] + 13, [self.Trips(player)[1], self.Pair(player, numberToPop)[1]]
            return None

    def Quads(self, player):
        numbers = self.numberCheck(self.checkCards(player))
        nbQuads = number
        nbQuads.sort()
        quads = []
        poped = False
        for i in range(len(nbQuads)):
            count = 0
            for y in range(len(nbQuads)):
                if nbQuads[i] == nbQuads[y] and i != y:
                    count += 1
                    if count == 3:
                        quads.append(nbQuads[i])
                        poped = True
                        break
            if poped == True:
                break
        if len(quads) == 1:
            res = quads[0]
            if quads[0] == 1:
                res = 14
            return (res + 50), quads[0]
        return None

    def Straight(self, player, numbers=None):
        if numbers == None:
            numbers = self.numberCheck(self.checkCards(player))
        sortedNumbers = sorted(numbers, reverse=True)
        trash = []
        straight = []
        for i in range(len(sortedNumbers)-1):
            if sortedNumbers[i+1] == sortedNumbers[i]:
                trash.append(i)
        trash = sorted(trash, reverse=True)
        for x in trash:
            sortedNumbers.pop(x)
        if sortedNumbers[-1] == 1:
            sortedNumbers.insert(0, 14)
        for i in range(len(sortedNumbers)-1):
            if sortedNumbers[i] - sortedNumbers[i+1] == 1:
                straight.append(sortedNumbers[i])
            else:
                straight = []
            if len(straight) == 4:
                straight.append(sortedNumbers[i+1])
                straight.sort()
                res = straight[4]
                return res + 59, straight
        return None

    def Flush(self, player):
        numbers = self.numberCheck(self.checkCards(player))
        power = self.powerCheck(self.checkCards(player))
        isColor = False
        for i in range(len(power)):
            sign = []
            signIndex = []
            nbInColor = []
            for y in range(len(power)):
                if power[i] == power[y] and i != y:
                    sign.append(power[y])
                    signIndex.append(y)
                    nbInColor.append(numbers[y])
                if len(sign) == 4:
                    nbInColor.append(numbers[i])
                    sign.append(power[i])
                    signIndex.append(i)
                    isColor = True
                    break
            if isColor:
                break
        nbInColor.sort()
        sign.sort()
        signIndex.sort()
        if len(sign) == 5:
            res = nbInColor[4]
            if nbInColor[0] == 1:
                res = 14
            return res + 72, nbInColor, sign[0]
        return None

    def straightFlush(self, player):
        Flushed = self.Flush(player)
        if Flushed:
            Straighted = self.Straight(player, Flushed[1])
            if Straighted:
                return Flushed[0] + 9, Straighted[1]
        return None

    def royalFlush(self, player):
        royale = self.QuinteFlush(player)
        if royale == 94:
            return 94, QuinteFlush[1]
        return None

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
