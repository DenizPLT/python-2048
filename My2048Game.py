import random

class My2048Game:
    def __init__(self):
        self.lose = False
        self.win = False
        self.score = 0
        self.board = [[0 for x in range(4)] for y in range(4)]

    def starte_spiel(self):
        self.generiere_zahl()
        while self.lose == False and self.win == False:
            self.pruefe_verloren()
            self.pruefe_gewonnen()
            if self.lose == True or self.win == True:
                print("Spiel vorbei!")
                self.score_ausgeben
                break
            self.generiere_zahl()
            self.ausgabe_spielfeld()
            self.score_ausgeben()
            spielzug = input(
                "Wie Spielfeld verschieben? L, R, O, U? (Quit = Q)")
            if spielzug == 'Q' or spielzug == 'q':
                break
            elif spielzug == 'L' or spielzug == 'l':
                index = -1
                self.verschiebe(index)
            elif spielzug == 'R' or spielzug == 'r':
                index = 1
                self.verschiebe(index)
            elif spielzug == 'O' or spielzug == 'o':
                index = -4
                self.verschiebe(index)
            elif spielzug == 'U' or spielzug == 'u':
                index = 4
                self.verschiebe(index)
            else:
                print("Inkorrekte Eingabe! Versuche es erneut")

    def generiere_zahl(self):
            reihe = random.randint(0, 3)
            spalte = random.randint(0, 3)
            while (self.board[reihe][spalte] != 0):
                reihe = random.randint(0, 3)
                spalte = random.randint(0, 3)
            zahl = random.choice([2, 4])
            self.board[reihe][spalte] = zahl

    def ausgabe_spielfeld(self):
        for row in self.board:
            for element in row:
                reihe = str(element) + " "
            print(reihe)

    def verschiebe(self, index):
        #for i in self.board:
        #    if (self.board[i+index]) == 0:
        #        self.board[i+index] = self.board[i]
        #        self.board[i] = 0
        #    elif (self.board[i+index]) == (self.board[i]):
        #        self.aktualisiere_score(self.board[i], self.board[i+index])
        #        self.board[i+index] = self.board[i+index] + self.board[i]
        #        self.board[i] = 0
        pass

    def summiere_zahlen_spielzug(self):
        ##
        pass

    def verschiebe_bis_rand(self):
        ##
        pass

    def aktualisiere_score(self, zahl1, zahl2):
        summe_zahlen = sum(zahl1, zahl2)
        self.score = self.score + summe_zahlen

    def score_ausgeben(self):
        print("Score: {} \n".format(self.score))

    def pruefe_verloren(self):
        ##
        pass

    def pruefe_gewonnen(self):
        ##
        pass


game = My2048Game()
game.starte_spiel()
