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

