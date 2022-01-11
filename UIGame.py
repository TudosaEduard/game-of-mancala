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

    return pygame.image.load(holeEmpty_path).convert(), \
           pygame.image.load(hole1_path).convert(), \
           pygame.image.load(hole2_path).convert(), \
           pygame.image.load(hole3_path).convert(), \
           pygame.image.load(hole4_path).convert(), \
           pygame.image.load(hole5_path).convert(), \
           pygame.image.load(hole6_path).convert()


def loadStore():
    storeEmpty_path = os.path.join("images", "storeEmpty.jpg")
    store1_path = os.path.join("images", "1boardA.jpg")
    store2_path = os.path.join("images", "2boardA.jpg")
    store3_path = os.path.join("images", "3boardA.jpg")
    store4_path = os.path.join("images", "4boardA.jpg")
    store5_path = os.path.join("images", "5boardA.jpg")
    store6_path = os.path.join("images", "7board.jpg")

    return pygame.image.load(storeEmpty_path).convert(), \
           pygame.image.load(store1_path).convert(), \
           pygame.image.load(store2_path).convert(), \
           pygame.image.load(store3_path).convert(), \
           pygame.image.load(store4_path).convert(), \
           pygame.image.load(store5_path).convert(), \
           pygame.image.load(store6_path).convert()


def loadTitle():
    mancala_path = os.path.join("images", "mancala.jpg")
    return pygame.image.load(mancala_path).convert()


'''
Pregatim mai multe iteme necesare pentru realizarea UI-ului
'''


def pygameScreen(player):
    pygame.init()

    widthScreen = 745
    heightScreen = 430
    screen = pygame.display.set_mode((widthScreen, heightScreen))
    pygame.display.set_caption('Game-of-Mancala')

    bgcolor = (0, 0, 0)

    board = loadBoard()
    he, h1, h2, h3, h4, h5, h6 = loadHoles()
    se, s1, s2, s3, s4, s5, s6 = loadStore()
    title = loadTitle()

pygameScreen(choosePlayer())
