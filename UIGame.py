"""
Autor : Tudosa eduard-Bogdan
Game: Game of Mancala
Observatii: A se consulta readme-ul inainte de inceperea jocului
"""

import os
import random
import time

import pygame
import ControllerGame

from pygame import K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0, K_MINUS, K_EQUALS, K_ESCAPE

'''
Alegem modul de joc dorit.(calculator sau alt oponent)
'''


def choosePlayer():
    print("Alege tipul de oponent pe care il doresti(calculator sau player):")
    oponent = input()
    if (oponent[0].lower() != 'p') and (oponent[0].lower() != 'c'):
        print("Nu exista acest tip de oponent!")
        exit(0)
    else:
        return oponent


'''
Dam load la imaginile pentru:
- titlul jocului
- tabla de joc
- gaurile cu pietre cat si locul unde se aduna pietrele pentru a se calcula scorul jucatorului 
'''


def loadBoard():
    board_path = os.path.join("images", "board.jpg")
    return pygame.image.load(board_path)


def loadHoles():
    holeEmpty_path = os.path.join("images", "empty.jpg")
    hole1_path = os.path.join("images", "1stoneA.jpg")
    hole2_path = os.path.join("images", "2stoneA.jpg")
    hole3_path = os.path.join("images", "3stoneA.jpg")
    hole4_path = os.path.join("images", "4stoneA.jpg")
    hole5_path = os.path.join("images", "5stoneA.jpg")
    hole6_path = os.path.join("images", "6stoneA.jpg")

    return [pygame.image.load(holeEmpty_path).convert(),
            pygame.image.load(hole1_path).convert(),
            pygame.image.load(hole2_path).convert(),
            pygame.image.load(hole3_path).convert(),
            pygame.image.load(hole4_path).convert(),
            pygame.image.load(hole5_path).convert(),
            pygame.image.load(hole6_path).convert()]


def loadStore():
    storeEmpty_path = os.path.join("images", "storeEmpty.jpg")
    store1_path = os.path.join("images", "1boardA.jpg")
    store2_path = os.path.join("images", "2boardA.jpg")
    store3_path = os.path.join("images", "3boardA.jpg")
    store4_path = os.path.join("images", "4boardA.jpg")
    store5_path = os.path.join("images", "5boardA.jpg")
    store6_path = os.path.join("images", "7board.jpg")

    return [pygame.image.load(storeEmpty_path).convert(),
            pygame.image.load(store1_path).convert(),
            pygame.image.load(store2_path).convert(),
            pygame.image.load(store3_path).convert(),
            pygame.image.load(store4_path).convert(),
            pygame.image.load(store5_path).convert(),
            pygame.image.load(store6_path).convert()]


def loadTitle():
    mancala_path = os.path.join("images", "mancala.jpg")
    return pygame.image.load(mancala_path).convert()


'''
Creeam UI-ul care isi va face update-uri in functie de schimbarile realizate de mutarile jucatorilor
'''


def storeImage(s, value):
    if value == 0:
        return s[0]
    elif value == 1:
        return s[1]
    elif value == 2:
        return s[2]
    elif value == 3:
        return s[3]
    elif value == 4:
        return s[4]
    elif value == 5:
        return s[5]
    elif value > 5:
        return s[6]


def holeImage(h, value):
    if value == 0:
        return h[0]
    elif value == 1:
        return h[1]
    elif value == 2:
        return h[2]
    elif value == 3:
        return h[3]
    elif value == 4:
        return h[4]
    elif value == 5:
        return h[5]
    elif value > 5:
        return h[6]


'''
Crearea textului afisat in josul paginii pentru a anunta cine este in tura, cat si a scorului celor 2 jucatori
'''


def scorePlayer(scores):
    font = pygame.font.Font('freesansbold.ttf', 40)

    player1Score = font.render(str(scores[0]), True, (37, 175, 82))
    player2Score = font.render(str(scores[1]), True, (37, 175, 82))

    return player1Score, player2Score


def namePlayer(name):
    font = pygame.font.Font('freesansbold.ttf', 40)
    return font.render(name, True, (37, 175, 82))


'''
Aceasta functie updateScreen este functia care face display la toate elementele necesare 
pentru a se realiza jocul, in urma unei mutari aceasta schimband interfata cu una noua
dupa update-urile necesare.
'''


def updateScreen(board, h, s, title, screen, game, currentPlayer):
    """
    :param board: tabla de joc adaugata
    :param h: vector cu imaginile gaurilor luate din folder-ul images
    :param s: vector cu imaginile store-urilor preluate din folder-ul images
    :param title: imaginea cu titlul Mancala
    :param screen: fereastra jocului
    :param game: parametru ce face referire la logica jocului
    :param currentPlayer: parametru ce precizeaza player-ul care este la tura
    :return:
    """

    bgcolor = (0, 0, 0)

    screen.fill(bgcolor)
    screen.blit(board, (230, 160))

    screen.blit(title, (350, 80))

    hole12 = holeImage(h, game.getSecondHoleValue(6))
    hole11 = holeImage(h, game.getSecondHoleValue(5))
    hole10 = holeImage(h, game.getSecondHoleValue(4))
    hole9 = holeImage(h, game.getSecondHoleValue(3))
    hole8 = holeImage(h, game.getSecondHoleValue(2))
    hole7 = holeImage(h, game.getSecondHoleValue(1))

    hole6 = holeImage(h, game.getFirstHoleValue(6))
    hole5 = holeImage(h, game.getFirstHoleValue(5))
    hole4 = holeImage(h, game.getFirstHoleValue(4))
    hole3 = holeImage(h, game.getFirstHoleValue(3))
    hole2 = holeImage(h, game.getFirstHoleValue(2))
    hole1 = holeImage(h, game.getFirstHoleValue(1))

    screen.blit(hole12, (310, 170))
    screen.blit(hole11, (367, 170))
    screen.blit(hole10, (424, 170))
    screen.blit(hole9, (528, 170))
    screen.blit(hole8, (585, 170))
    screen.blit(hole7, (642, 170))

    screen.blit(hole1, (310, 237))
    screen.blit(hole2, (367, 237))
    screen.blit(hole3, (424, 237))
    screen.blit(hole4, (528, 237))
    screen.blit(hole5, (585, 237))
    screen.blit(hole6, (642, 237))

    stores = game.storesScore()

    store1 = storeImage(s, stores[0])
    store2 = storeImage(s, stores[1])

    screen.blit(store2, (248, 170))
    screen.blit(store1, (704, 170))

    scores = scorePlayer(game.playerScores())

    screen.blit(scores[0], (834, 190))
    screen.blit(scores[1], (148, 190))

    name = namePlayer(currentPlayer)

    if currentPlayer[-1] != '!':
        screen.blit(name, (400, 350))
    else:
        screen.blit(name, (300, 350))

    pygame.display.flip()


'''
Pregatim mai multe iteme necesare pentru realizarea UI-ului
'''


def pygameScreen(player):
    """
    :param player: tipul adversarului citit din consola
    """
    pygame.init()
    widthScreen = 1000
    heightScreen = 500
    screen = pygame.display.set_mode((widthScreen, heightScreen))
    pygame.display.set_caption('Game-of-Mancala')
    running = 1
    game = ControllerGame.ControllerGame()

    board = loadBoard()
    h = loadHoles()
    s = loadStore()
    title = loadTitle()

    '''
    Aici rulam programul efectiv pana la terminarea partidei de Mancala 
    in functie de parametri alesi si de parcursul jocului
    '''

    currentPlayer = 'Player 1'
    while running:

        for event in pygame.event.get():
            if game.playerTurn() == 'Player':
                currentPlayer = 'Player 1'
            else:
                otherPlayer = player
                if otherPlayer[0].lower() == 'p':
                    currentPlayer = 'Player 2'
                else:
                    currentPlayer = 'Computer'

            if event.type == pygame.QUIT:
                running = 0

            if game.continueGame():
                updateScreen(board, h, s, title, screen, game, currentPlayer)
                if currentPlayer.lower() == "player 1":
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_1:
                            value = 1
                            game.selectHole(value)
                        if event.key == K_2:
                            value = 2
                            game.selectHole(value)
                        if event.key == K_3:
                            value = 3
                            game.selectHole(value)
                        if event.key == K_4:
                            value = 4
                            game.selectHole(value)
                        if event.key == K_5:
                            value = 5
                            game.selectHole(value)
                        if event.key == K_6:
                            value = 6
                            game.selectHole(value)
                        if event.key == K_7:
                            value = 12
                            game.selectHole(value)
                        if event.key == K_8:
                            value = 11
                            game.selectHole(value)
                        if event.key == K_9:
                            value = 10
                            game.selectHole(value)
                        if event.key == K_0:
                            value = 9
                            game.selectHole(value)
                        if event.key == K_MINUS:
                            value = 8
                            game.selectHole(value)
                        if event.key == K_EQUALS:
                            value = 7
                            game.selectHole(value)
                        if event.key == K_ESCAPE:
                            exit(0)

                    updateScreen(board, h, s, title, screen, game, currentPlayer)

                else:
                    if player[0].lower() == 'p':
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_1:
                                value = 1
                                game.selectHole(value)
                            if event.key == K_2:
                                value = 2
                                game.selectHole(value)
                            if event.key == K_3:
                                value = 3
                                game.selectHole(value)
                            if event.key == K_4:
                                value = 4
                                game.selectHole(value)
                            if event.key == K_5:
                                value = 5
                                game.selectHole(value)
                            if event.key == K_6:
                                value = 6
                                game.selectHole(value)
                            if event.key == K_7:
                                value = 12
                                game.selectHole(value)
                            if event.key == K_8:
                                value = 11
                                game.selectHole(value)
                            if event.key == K_9:
                                value = 10
                                game.selectHole(value)
                            if event.key == K_0:
                                value = 9
                                game.selectHole(value)
                            if event.key == K_MINUS:
                                value = 8
                                game.selectHole(value)
                            if event.key == K_EQUALS:
                                value = 7
                                game.selectHole(value)
                            if event.key == K_ESCAPE:
                                exit(0)

                        updateScreen(board, h, s, title, screen, game, currentPlayer)

                    else:

                        value = []
                        for index in range(6):
                            if game.board.getFirstHoleValue(index) != 0:
                                value.append(index)
                        for index in range(6):
                            if game.board.getSecondHoleValue(index) != 0:
                                value.append(index + 7)

                        time.sleep(3)
                        game.selectHole(random.choice(value))

                        updateScreen(board, h, s, title, screen, game, currentPlayer)

            else:
                game.endGame()
                winner = game.winner()
                if winner == "tie":
                    updateScreen(board, h, s, title, screen, game, "Is tie :)")
                elif winner == "Player":
                    updateScreen(board, h, s, title, screen, game, "Player 1 win the game!")
                elif player[0].lower() == 'p':
                    updateScreen(board, h, s, title, screen, game, "Player 2 win the game!")
                else:
                    updateScreen(board, h, s, title, screen, game, "Computer win the game!")


pygameScreen(choosePlayer())
