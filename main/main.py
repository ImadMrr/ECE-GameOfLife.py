import pygame
from pygame.locals import *
import game as Game
import menu as Menu
import pageAccueil as PageAccueil

width, height = 1400, 800
#rows, cols = 100, 100
speed = 5
start_game = False
rule_choice = 0

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jeu de la Vie - Imad Victor Paul Vinciane")

start_game = PageAccueil.pageAccueil(screen)
if start_game:
    info = Menu.menu(screen) #info[0] : rules_choice / info[1] = plate / info[2] = nbr_tour / info[3] = rows / info[4] = cols / info[5] = mode
    if(int(info[3]<500)):
        graphData = Game.game(width, height, speed, info)
    else:
        graphData = Game.simulation(width, height, speed, info)
    #grapheData[0] = alives / [1] = calculTime / [2] = dead
    Menu.menu_graphs(screen,graphData)
    pygame.quit()