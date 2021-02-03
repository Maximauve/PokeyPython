from .Shuffle import table
from .Game import Whole_Game
g = Whole_Game()


#! Return des fonctions:
# * Value[0] --> Retourne le nombre de points rapportés par la valeure
# * Value[1] --> Retourne la valeure gagnée
# * Value[2] --> Retourne le message
#   Value[3] --> Complément (optionnel)


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

    def Paire(self, player, number=None):
        if number == None:
            number = self.NumberCheck(self.CheckCards(player))
        numbersort = sorted(number, reverse=True)
        if numbersort[5:] == [1, 1]:
            numbersort[5:], numbersort[:5] = numbersort[:5], numbersort[5:]
            return 13, 1
        for i in range(len(numbersort)):
            if i+1 >= len(numbersort):
                break
            if numbersort[i] == numbersort[i+1]:
                return (numbersort[i] - 1), numbersort[i], f"Vous avez une Paire de {numbersort[i]}", i
        return None

    def DoublePaire(self, player):
        number = self.NumberCheck(self.CheckCards(player))
        numberpop = sorted(number, reverse=True)
        if numberpop[5:] == [1, 1]:
            numberpop[5:], numberpop[:5] = numberpop[:5], numberpop[5:]
        if self.Paire(player):
            for _ in range(2):
                numberpop.pop(self.Paire(player)[3])
            res = self.Paire(player, numberpop)
            if res:
                return self.Paire(player)[0] + 12, [self.Paire(player)[1], res[1]], f"Doube Paire de {self.Paire(player)[1]} et de {res[1]}"
            return None

    def Brelan(self, player):
        number = self.NumberCheck(self.CheckCards(player))
        numbertrié = sorted(number, reverse=True)
        if numbertrié[4:] == [1, 1, 1]:
            numbertrié[4:], numbertrié[:4] = numbertrié[:4], numbertrié[4:]
        brelan = 0
        for i in range(len(numbertrié)-2):
            if numbertrié[i] - numbertrié[i+1] == 0:
                if numbertrié[i+1] - numbertrié[i+2] == 0:
                    brelan = numbertrié[i]
                    break
        if brelan:
            return brelan + 24, brelan, f"Vous avez un Brelan de {brelan} !", i

        return None

    def Full(self, player):

        number = self.NumberCheck(self.CheckCards(player))
        numberpop = sorted(number, reverse=True)
        if self.Brelan(player):
            for _ in range(3):
                numberpop.pop(self.Brelan(player)[3])
            if self.Paire(player, numberpop):
                return self.Brelan(player)[1] + 13, [self.Brelan(player)[1], self.Paire(player, numberpop)[1]], f"Vous avez un full! Brelan de {self.Brelan(player)[1]} et Paire de {self.Paire(player, numberpop)[1]}"
            return None

    def Suite(self, player, number=None):
        if number == None:
            number = self.NumberCheck(self.CheckCards(player))
        number = [8, 2, 10, 5, 11, 12, 13]
        numbertrié = sorted(number, reverse=True)
        tab = []
        suite = []
        compt = 0
        for i in range(len(numbertrié)-1):
            if numbertrié[i+1] == numbertrié[i]:
                tab.append(i)
        for x in tab:
            numbertrié.pop(x)
        if numbertrié[-1] == 1:
            numbertrié.insert(0, 14)
        for i in range(len(numbertrié)-1):
            if numbertrié[i] - numbertrié[i+1] == 1:
                suite.append(numbertrié[i])
                compt += 1
            else:
                suite = []
            if compt == 4:
                suite.append(numbertrié[i+1])
                suite.sort()
                res = suite[4]
                return res + 63, suite, f"Vous avez une suite! Commençant par un {suite[0]} et finissant par un {suite[4]}"
        return None

    def Couleur(self, player):
        number = self.NumberCheck(self.CheckCards(player))
        power = self.PowerCheck(self.CheckCards(player))
        coul = False
        for i in range(len(power)):
            couleur = []
            couleury = []
            nbcolor = []
            for y in range(len(power)):
                if power[i] == power[y] and i != y:
                    couleur.append(power[y])
                    couleury.append(y)
                    nbcolor.append(number[y])
                if len(couleur) == 4:
                    nbcolor.append(number[i])
                    couleur.append(power[i])
                    couleury.append(i)
                    coul = True
                    break
            if coul:
                break
        nbcolor.sort()
        couleur.sort()
        couleury.sort()
        tabnb = []
        if len(couleur) == 5:
            for x in couleury:
                tabnb.append(number[x])
            tabnb.sort()
            res = tabnb[4]
            if tabnb[0] == 1:
                res = 14
            return res + 72, nbcolor, "Vous avez une couleur!", couleur[0]
        return None

    def Carre(self, player):
        number = self.NumberCheck(self.CheckCards(player))
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
            res = carre[0]
            if carre[0] == 1:
                res = 14
            return (res + 50), carre[0], (f"Vous avez un carré de {carre[0]}")
        return None

    def QuinteFlush(self, player):
        Couleur = self.Couleur(player)
        if Couleur:
            Suite = self.Suite(player, Couleur[1])
            if Suite:
                return Couleur[0] + 9, Suite[1], f"Vous avez une Quinte Flush de {Couleur[3]}s!"
        return None

    def QuinteFlushRoyale(self, player):
        QuinteFlush = self.QuinteFlush(player)
        if QuinteFlush == 94:
            return 94, QuinteFlush[1], f"Vous avez une Quinte Flush Royale"
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
