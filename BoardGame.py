"""
Aici vom realiza interfata tablei de joc cat si functii necesare pentru logica jocului.
Clasa va comunica cu Controller-ul care va realiza in urma datelor oferite de BoardGame logica.
"""


class BoardGame:
    def __init__(self):
        self.firstBoardGameLine = [4, 4, 4, 4, 4, 4, 0]
        self.secondBoardGameLine = [4, 4, 4, 4, 4, 4, 0]
        self.lastStone = 0

    def getBoardGame(self):
        return self.firstBoardGameLine, self.secondBoardGameLine

    def getFirstHoleValue(self, hole):
        return self.firstBoardGameLine[hole - 1]

    def getSecondHoleValue(self, hole):
        return self.secondBoardGameLine[hole - 1]

    def getLastStone(self):
        return self.lastStone

    def storesScore(self):
        return self.firstBoardGameLine[6], self.secondBoardGameLine[6]

    def stoneLeft(self, name):
        totalStone = 0
        if name == 'Player':
            for holePosition in range(6):
                totalStone = totalStone + self.firstBoardGameLine[holePosition]
        else:
            for holePosition in range(6):
                totalStone = totalStone + self.secondBoardGameLine[holePosition]
        return totalStone > 0

    '''
    Functia makeMove realizeaza o mutare a unui jucator si modifica tabla de joc in urma acestei mutari
    '''

    def makeMove(self, hole, name):
        lastPosition = 0
        stones = 0
        if hole < 7:
            stones = self.firstBoardGameLine[hole - 1]
            self.firstBoardGameLine[hole - 1] = 0
            hole = hole - 1
        else:
            stones = self.secondBoardGameLine[hole - 7]
            self.secondBoardGameLine[hole - 7] = 0

        while stones != 0:
            if name == 'Player':
                for holePosition in range(13):
                    if holePosition > hole:
                        if stones != 0:
                            if holePosition < 7:
                                self.firstBoardGameLine[holePosition] = self.firstBoardGameLine[holePosition] + 1
                                stones = stones - 1
                                lastPosition = holePosition
                            else:
                                self.secondBoardGameLine[holePosition - 7] = self.secondBoardGameLine[
                                                                                 holePosition - 7] + 1
                                stones = stones - 1
                                lastPosition = holePosition

                for holePosition in range(13):
                    if stones != 0:
                        if holePosition < 7:
                            self.firstBoardGameLine[holePosition] = self.firstBoardGameLine[holePosition] + 1
                            stones = stones - 1
                            lastPosition = holePosition
                        else:
                            self.secondBoardGameLine[holePosition - 7] = self.secondBoardGameLine[holePosition - 7] + 1
                            stones = stones - 1
                            lastPosition = holePosition

            else:
                for holePosition in range(14):
                    if holePosition > hole:
                        if stones != 0:
                            if holePosition != 6:
                                if holePosition < 6:
                                    self.firstBoardGameLine[holePosition] = self.firstBoardGameLine[holePosition] + 1
                                    stones = stones - 1
                                    lastPosition = holePosition
                                else:
                                    self.secondBoardGameLine[holePosition - 7] = self.secondBoardGameLine[
                                                                                     holePosition - 7] + 1
                                    stones = stones - 1
                                    lastPosition = holePosition

                for holePosition in range(14):
                    if stones != 0:
                        if holePosition != 6:
                            if holePosition < 7:
                                self.firstBoardGameLine[holePosition] = self.firstBoardGameLine[holePosition] + 1
                                stones = stones - 1
                                lastPosition = holePosition
                            else:
                                self.secondBoardGameLine[holePosition - 7] = self.secondBoardGameLine[
                                                                                 holePosition - 7] + 1
                                stones = stones - 1
                                lastPosition = holePosition

        if lastPosition == 6 or lastPosition == 13:
            self.lastStone = -1
        else:
            self.lastStone = lastPosition

    '''
    Mutarea speciala a unei singure pietre intr-o casuta goala
    '''

    def lastStoneMove(self, player):
        board = self.firstBoardGameLine + self.secondBoardGameLine
        if self.lastStone != -1:
            if board[self.lastStone] - 1 == 0:
                if player == "Player":

                    if self.lastStone == 0:
                        if board[12] != 0:
                            board[self.lastStone] = 0
                            board[6] = board[6] + 1 + board[12]
                            board[12] = 0

                    if self.lastStone == 1:
                        if board[11] != 0:
                            board[self.lastStone] = 0
                            board[6] = board[6] + 1 + board[11]
                            board[11] = 0

                    if self.lastStone == 2:
                        if board[10] != 0:
                            board[self.lastStone] = 0
                            board[6] = board[6] + 1 + board[10]
                            board[10] = 0

                    if self.lastStone == 3:
                        if board[9] != 0:
                            board[self.lastStone] = 0
                            board[6] = board[6] + 1 + board[9]
                            board[9] = 0

                    if self.lastStone == 4:
                        if board[8] != 0:
                            board[self.lastStone] = 0
                            board[6] = board[6] + 1 + board[8]
                            board[8] = 0

                    if self.lastStone == 5:
                        if board[7] != 0:
                            board[self.lastStone] = 0
                            board[6] = board[6] + 1 + board[7]
                            board[7] = 0

                else:
                    if self.lastStone == 12:
                        if board[0] != 0:
                            board[self.lastStone] = 0
                            board[13] = board[13] + 1 + board[0]
                            board[0] = 0

                    if self.lastStone == 11:
                        if board[1] != 0:
                            board[self.lastStone] = 0
                            board[13] = board[13] + 1 + board[1]
                            board[1] = 0

                    if self.lastStone == 10:
                        if board[2] != 0:
                            board[self.lastStone] = 0
                            board[13] = board[13] + 1 + board[2]
                            board[2] = 0

                    if self.lastStone == 9:
                        if board[3] != 0:
                            board[self.lastStone] = 0
                            board[13] = board[13] + 1 + board[3]
                            board[3] = 0

                    if self.lastStone == 8:
                        if board[4] != 0:
                            board[self.lastStone] = 0
                            board[13] = board[13] + 1 + board[4]
                            board[4] = 0

                    if self.lastStone == 7:
                        if board[5] != 0:
                            board[self.lastStone] = 0
                            board[13] = board[13] + 1 + board[5]
                            board[5] = 0

        for index in range(14):
            if index < 7:
                self.firstBoardGameLine[index] = board[index]
            else:
                self.secondBoardGameLine[index - 7] = board[index]

    '''
    Dupa terminarea jocului, jucatorul curent muta toate pietrele din acest rand in store-ul lui
    '''

    def rowToStore(self, player):
        if player == "Player":
            for index in range(6):
                self.firstBoardGameLine[6] = self.firstBoardGameLine[6] + self.firstBoardGameLine[index]
        else:
            for index in range(6):
                self.secondBoardGameLine[6] = self.secondBoardGameLine[6] + self.secondBoardGameLine[index]
