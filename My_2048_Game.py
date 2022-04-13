import random


class My_2048_Game:
    def __init__(self):
        self.lose = False
        self.win = False
        self.score = 0
        self.board = [
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0
        ]

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
            freie_stellen = [i for i, x in enumerate(self.board) if x == 0]
            ausgewaehlte_stelle = random.choice(freie_stellen)
            einzusetzende_zahl = random.choice([2, 4])
            self.board[ausgewaehlte_stelle] = einzusetzende_zahl
        except IndexError:
            print("Spielfeld ist voll! Bitte neustarten über Q")

    def ausgabe_spielfeld(self):
        board_format = "\n{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n".format(
            self.board[0], self.board[1], self.board[2], self.board[3], self.board[4], self.board[5], self.board[6],
            self.board[7], self.board[8], self.board[9], self.board[10], self.board[11], self.board[12], self.board[13],
            self.board[14], self.board[15])
        print(board_format)

    def verschiebe(self, index):
        for i in self.board:
            if self.board[i+index] == 0:
                self.board[i+index] = self.board[i]
                self.board[i] = 0
            elif self.board[i+index] == self.board[i]:
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
        pass

    def score_ausgeben(self):
        print("Score: {} \n".format(self.score))

    def pruefe_verloren(self):
        ##
        pass

    def pruefe_gewonnen(self):
        ##
        pass


game = My_2048_Game()
game.starte_spiel()
