"""
Aici vom realiza interfata tablei de joc cat si functii necesare pentru logica jocului.
Clasa va comunica cu Controller-ul care va realiza in urma datelor oferite de BoardGame logica.
"""


class BoardGame:
    def __init__(self):
        self.firstBoardGameLine = [4, 4, 4, 4, 4, 4]
        self.secondBoardGameLine = [4, 4, 4, 4, 4, 4]
        self.firstStore = 0
        self.secondStore = 0
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
        return self.firstStore, self.secondStore

