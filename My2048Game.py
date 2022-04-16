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
        try:
            #freie_stellen = [[0 for x in range(4)] for y in range(4)]
            #for row in freie_stellen:
            #    for element in freie_stellen:
            #freie_stellen = self.board.index(0)?

            freie_stellen = [i for i, x in enumerate(self.board) if x == 0]
            ausgewaehlte_stelle = random.choice(freie_stellen)
            einzusetzende_zahl = random.choice([2, 4])
            self.board[ausgewaehlte_stelle] = einzusetzende_zahl
        except IndexError:
            print("Spielfeld ist voll! Bitte neustarten über Q")

    def ausgabe_spielfeld(self):
        for row in self.board:
            for element in self.board:
                reihe = str(element) + " "
            print(reihe)

    def verschiebe(self, index):
        for i in self.board:
            if (self.board[i+index]) == 0:
                self.board[i+index] = self.board[i]
                self.board[i] = 0
            elif (self.board[i+index]) == (self.board[i]):
                self.aktualisiere_score(self.board[i], self.board[i+index])
                self.board[i+index] = self.board[i+index] + self.board[i]
                self.board[i] = 0

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
        for i in self.board:
            if i == 2048:
                self.win = True


game = My2048Game()
game.starte_spiel()
