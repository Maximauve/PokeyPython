class Game:
    def __init__(self):

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
   