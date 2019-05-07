import pycosat as pycosat
import pygame
from pygame.locals import *
import sys
from pysat.formula import CNF
from pysat.solvers import Lingeling

from sources.Grid import Grid
from sources.table_de_verite import *


def load_images():
    textures = []
    textures.append(pygame.image.load("data/0.png").convert_alpha())
    textures.append(pygame.image.load("data/1.png").convert_alpha())
    textures.append(pygame.image.load("data/2.png").convert_alpha())
    textures.append(pygame.image.load("data/3.png").convert_alpha())
    textures.append(pygame.image.load("data/4.png").convert_alpha())
    textures.append(pygame.image.load("data/5.png").convert_alpha())
    textures.append(pygame.image.load("data/6.png").convert_alpha())
    textures.append(pygame.image.load("data/7.png").convert_alpha())
    textures.append(pygame.image.load("data/8.png").convert_alpha())
    textures.append(pygame.image.load("data/9.png").convert_alpha())
    textures.append(pygame.image.load("data/white.jpg").convert())
    textures.append(pygame.image.load("data/black.jpg").convert())
    textures.append(pygame.image.load("data/isblack.png").convert_alpha())
    return textures

padding_top = 0
padding_middle = 0
padding_bottom = 0
padding_side = 0

width = 300
menu_height = 0
grille_height = 300



display_width = width + 2 * padding_side
display_height = menu_height + grille_height + padding_top + padding_middle + padding_bottom

pygame.init()

DISPLAY = pygame.display.set_mode((display_width, display_height), 0, 32)


WHITE = (255, 255, 255)

DISPLAY.fill(WHITE)
textures = load_images()

nb_bombes = 2
pourcentage_affiche = 1
taille_bombes_verticals = 3
taille_bombes_horizontal = 3

nb_grilles_affiche = taille_bombes_verticals * taille_bombes_horizontal
nb_grilles_affiche = (int) (nb_grilles_affiche * pourcentage_affiche)






grid = Grid(DISPLAY, textures, padding_side, padding_top + menu_height + padding_middle , display_width-padding_side, display_height-padding_bottom, nb_bombes, nb_grilles_affiche, taille_bombes_horizontal, taille_bombes_verticals)

grillState = grid.returnGridState()
grill = grid.returnGridNearby()
print(grillState)
print(grill)
liste_to_dimacs(grill, grillState)

grid.revealed = not grid.revealed

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:

            pos_x, pos_y = pygame.mouse.get_pos()
            if event.button == 1:
                grid.toggle(pos_x, pos_y)
            if event.button == 3:
                grid.toggleBombe( pos_x, pos_y)


            grillState = grid.returnGridState()
            grill = grid.returnGridNearby()
            print(grillState)
            print(grill)
            liste_to_dimacs(grill, grillState, False)

            formula = CNF(from_file='DIMACS.cnf').clauses
            print("dimacs: ", formula)
            print("SAT : ", pycosat.solve(formula))


    grid.draw_grid()
    pygame.display.update()




