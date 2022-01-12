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

    '''
    Functie care calculeaza scorul celor 2 jucatori
    '''

    def playerScores(self):
        player1 = 0
        player2 = 0

        if self.player.getName() == 'Player':
            player1 = self.player.getScore()
            player2 = self.other.getScore()
        else:
            player2 = self.player.getScore()
            player1 = self.other.getScore()

        return player1, player2

    '''
    Functie care specifica tura jucatorului
    '''

    def playerTurn(self):
        return self.player.getName()

    '''
    Functie care mentine desfasurarea jocului
    (pana cand nu mai raman pietre pe una din cele 2 linii)
    '''

    def continueGame(self):
        return self.board.stoneLeft(self.other.getName())

    '''
    Functie care realizeaza logica din spatele selectiei unei gauri de catre jucatorul curent
    '''

    def selectHole(self, hole):
        self.board.makeMove(hole, self.player.getName())
        self.board.lastStoneMove(self.player.getName())

        score = 0
        store = self.board.storesScore()

        if self.player.getName() == 'Player':
            score = store[0]
        else:
            score = store[1]

        self.player.setScore(score)

        if self.board.lastStone < 14:
            temp = self.player
            self.player = self.other
            self.other = temp

    '''
    Functia care realizeaza logica jocului dupa terminarea acestuia
    '''

    def endGame(self):
        self.board.rowToStore(self.other.getName())

        score = 0
        store = self.board.storesScore()

        if self.other.getName() == 'Player':
            score = store[0]
        else:
            score = store[1]

        self.other.setScore(score)

    '''
    Functia care precizeaza rezultatul jocului
    '''

    def winner(self):
        if self.player.getScore() == self.other.getScore():
            return "tie"
        elif self.player.getScore() > self.other.getScore():
            return self.player.getName()
        else:
            return self.other.getName()
