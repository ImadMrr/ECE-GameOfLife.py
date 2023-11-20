import pygame
from pygame.locals import *
import game as Game
import graphs.graphAlive as Graph
import menu as Menu
import pageAccueil as PageAccueil

width, height = 1400, 800
rows, cols = 100, 100
speed = 5
start_game = False
rule_choice = 0

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jeu de la Vie - Imad Victor Paul Vinciane")

start_game = PageAccueil.pageAccueil(screen)
if start_game:
    info = Menu.menu(screen) #info[0] : rules_choice / info[1] = plate / info[2] = nbr_tour
    graphData = Game.game(width, height, rows, cols, speed, info[0], info[1], info[2])
    pygame.quit()
    Graph.graph_alive(graphData[0]) #grapheData[0] = alives / [1] = calculTime / [2] = dead
    Graph.graph_death(graphData[2]) #grapheData[0] = alives / [1] = calculTime / [2] = dead
    Graph.graph_calcul(graphData[1]) #grapheData[0] = alives / [1] = calculTime / [2] = dead