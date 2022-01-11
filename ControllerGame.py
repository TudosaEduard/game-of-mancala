"""
Aici vom realiza logica din spatele jocului cu ajutorul claselor Player si Board
"""

import PlayerGame
import BoardGame


class ControllerGame:
    def __init__(self):
        self.board = BoardGame.BoardGame()
        self.player = PlayerGame.PlayerGame("Player")
        self.other = PlayerGame.PlayerGame("Other")

    def getFirstHoleValue(self, hole):
        return self.board.getFirstHoleValue(hole)

    def getSecondHoleValue(self, hole):
        return self.board.getSecondHoleValue(hole)

    def storesScore(self):
        return self.board.storesScore()

