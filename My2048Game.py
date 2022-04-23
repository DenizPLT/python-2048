import random


class My2048Game:
    def __init__(self):
        self.lose = False
        self.score = 0
        self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def starte_spiel(self):
        self.generiere_zahl()
        self.generiere_zahl()
        while (True):
            self.ausgabe_spielfeld()
            self.score_ausgeben()
            spielzug = input(
                "Wie Spielfeld verschieben? L, R, O, U? (Quit = Q)")
            tempBoard = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            for reihe in range(4):
                for spalte in range(4):
                    tempBoard[reihe][spalte] = self.board[reihe][spalte]
            if spielzug == 'Q' or spielzug == 'q':
                break
            elif spielzug == 'L' or spielzug == 'l':
                self.verschiebeLinks(0)
                self.verschiebeLinks(1)
                self.verschiebeLinks(2)
                self.verschiebeLinks(3)
            elif spielzug == 'R' or spielzug == 'r':
                self.verschiebeRechts(0)
                self.verschiebeRechts(1)
                self.verschiebeRechts(2)
                self.verschiebeRechts(3)
            elif spielzug == 'O' or spielzug == 'o':
                self.verschiebeHoch(0)
                self.verschiebeHoch(1)
                self.verschiebeHoch(2)
                self.verschiebeHoch(3)
            elif spielzug == 'U' or spielzug == 'u':
                self.verschiebeRunter(0)
                self.verschiebeRunter(1)
                self.verschiebeRunter(2)
                self.verschiebeRunter(3)
            else:
                print("Inkorrekte Eingabe! Versuche es erneut")
            if(self.vergleiche_board(self.board, tempBoard) == False):
                self.generiere_zahl()

    def generiere_zahl(self):
        reihe = random.randint(0, 3)
        spalte = random.randint(0, 3)
        while self.board[reihe][spalte] != 0:
            reihe = random.randint(0, 3)
            spalte = random.randint(0, 3)
        zahl = random.choice([2, 4])
        self.board[reihe][spalte] = zahl

    def ausgabe_spielfeld(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                abstand = "    "
                if (self.board[i][j] >9):
                    abstand = "   "
                if (self.board[i][j] >99):
                    abstand = "  "
                if (self.board[i][j] >999):
                    abstand = " "
                print(self.board[i][j], end=abstand)
            print("")

    def verschiebeHoch(self, spalte):
        for reihe in range(1, 4):
            sucheReihe = reihe - 1
            while(self.board[sucheReihe][spalte] == 0 and sucheReihe > 0): #sucht von oben nach unten nach nullen
                sucheReihe = sucheReihe - 1
            if (sucheReihe == 0 and self.board[sucheReihe][spalte] == 0): #verschiebt nullen
                self.board[0][spalte] = self.board[reihe][spalte]
                self.board[reihe][spalte] = 0
            elif(self.board[sucheReihe][spalte] == self.board[reihe][spalte]): #zwei gleiche zahlen gefunden
                self.zusammenfuegen(reihe, spalte, sucheReihe, spalte)
                self.board[reihe][spalte] = 0
            elif(reihe > sucheReihe + 1): # zahl gefunden aber übereinstimmen nicht
                self.board[sucheReihe+1][spalte] = self.board[reihe][spalte]
                self.board[reihe][spalte] = 0

    def verschiebeRunter(self, spalte):
        for reihe in range(2, -1, -1):
            sucheReihe = reihe + 1
            while(self.board[sucheReihe][spalte] == 0 and sucheReihe < 3):
                sucheReihe = sucheReihe + 1
            if (sucheReihe == 3 and self.board[sucheReihe][spalte] == 0):
                self.board[3][spalte] = self.board[reihe][spalte]
                self.board[reihe][spalte] = 0
            elif(self.board[sucheReihe][spalte] == self.board[reihe][spalte]):
                self.zusammenfuegen(reihe, spalte, sucheReihe, spalte)
                self.board[reihe][spalte] = 0
            elif(reihe < sucheReihe - 1): # zahl gefunden aber übereinstimmen nicht
                self.board[sucheReihe-1][spalte] = self.board[reihe][spalte]
                self.board[reihe][spalte] = 0

    def verschiebeLinks(self, reihe):
        for spalte in range(1, 4):
            sucheSpalte = spalte - 1
            while(self.board[reihe][sucheSpalte] == 0 and sucheSpalte > 0):
                sucheSpalte = sucheSpalte - 1
            if (sucheSpalte == 0 and self.board[reihe][sucheSpalte] == 0):
                self.board[reihe][0] = self.board[reihe][spalte]
                self.board[reihe][spalte] = 0
            elif(self.board[reihe][sucheSpalte] == self.board[reihe][spalte]):
                self.zusammenfuegen(reihe, spalte, reihe, sucheSpalte)
                self.board[reihe][spalte] = 0
            elif(spalte > sucheSpalte + 1): # zahl gefunden aber übereinstimmen nicht
                self.board[reihe][sucheSpalte+1] = self.board[reihe][spalte]
                self.board[reihe][spalte] = 0

    def verschiebeRechts(self, reihe):
        for spalte in range(2, -1, -1):
            sucheSpalte = spalte + 1
            while(self.board[reihe][sucheSpalte] == 0 and sucheSpalte < 3):
                sucheSpalte = sucheSpalte + 1
            if (sucheSpalte == 3 and self.board[reihe][sucheSpalte] == 0):
                self.board[reihe][3] = self.board[reihe][spalte]
                self.board[reihe][spalte] = 0
            elif(self.board[reihe][sucheSpalte] == self.board[reihe][spalte]):
                self.zusammenfuegen(reihe, spalte, reihe, sucheSpalte)
                self.board[reihe][spalte] = 0
            elif(spalte < sucheSpalte - 1): # zahl gefunden aber übereinstimmen nicht
                self.board[reihe][sucheSpalte-1] = self.board[reihe][spalte]
                self.board[reihe][spalte] = 0

    def zusammenfuegen(self, reihe1, spalte1, reihe2, spalte2):
        self.board[reihe2][spalte2] = 2*self.board[reihe2][spalte2]
        self.aktualisiere_score(self.board[reihe2][spalte2])

    def vergleiche_board(self, board1, board2):
        for reihe in range(4):
            for spalte in range(4):
                if (board1[reihe][spalte] != board2[reihe][spalte]):
                    return False
        return True

    def aktualisiere_score(self, zahl1):
        self.score = self.score + zahl1

    def score_ausgeben(self):
        print("Score: {} \n".format(self.score))

    def pruefe_verloren(self):
        ##
        pass



game = My2048Game()
game.starte_spiel()
