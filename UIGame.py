"""
Autor : Tudosa eduard-Bogdan
Game: Game of Mancala
Observatii: A se consulta readme-ul inainte de inceperea jocului
"""

import os
import pygame

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


def scorePlayer(scores):
    font = pygame.font.Font('freesansbold.ttf', 40)

    player1Score = font.render(str(scores[0]), True, (37, 175, 82))
    player2Score = font.render(str(scores[1]), True, (37, 175, 82))

    return player1Score, player2Score


def updateScreen(board, h, s, title, screen):
    bgcolor = (0, 0, 0)

    screen.fill(bgcolor)
    screen.blit(board, (230, 160))

    screen.blit(title, (350, 80))

    hole12 = holeImage(h, 1)
    hole11 = holeImage(h, 1)
    hole10 = holeImage(h, 1)
    hole9 = holeImage(h, 1)
    hole8 = holeImage(h, 1)
    hole7 = holeImage(h, 1)
    hole6 = holeImage(h, 1)
    hole5 = holeImage(h, 1)
    hole4 = holeImage(h, 1)
    hole3 = holeImage(h, 1)
    hole2 = holeImage(h, 1)
    hole1 = holeImage(h, 1)

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

    store1 = storeImage(s, 0)
    store2 = storeImage(s, 1)

    screen.blit(store2, (248, 170))
    screen.blit(store1, (704, 170))

    scores = scorePlayer([1, 1])

    screen.blit(scores[0], (834, 190))
    screen.blit(scores[1], (148, 190))

    pygame.display.flip()


'''
Pregatim mai multe iteme necesare pentru realizarea UI-ului
'''


def pygameScreen(player):
    pygame.init()
    clock = pygame.time.Clock()
    widthScreen = 1000
    heightScreen = 500
    screen = pygame.display.set_mode((widthScreen, heightScreen))
    pygame.display.set_caption('Game-of-Mancala')
    running = 1
    # LEFT = 1
    # game = MancalaController.MancalaController()

    board = loadBoard()
    h = loadHoles()
    s = loadStore()
    title = loadTitle()

    while running:
        updateScreen(board, h, s, title, screen)


pygameScreen(choosePlayer())
