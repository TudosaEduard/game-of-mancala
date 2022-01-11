"""
Aici vom stoca informatiile necesare pentru jucatorii nostri
cum ar fi tipul de jucator, scorul sau daca poate indeplini abilitatea: last stone position
"""


class PlayerGame:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lastStone = 0

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def getLastStone(self):
        return self.lastStone

    def setScore(self, score):
        self.score = score
