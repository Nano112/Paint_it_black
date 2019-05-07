import pycosat as pycosat
import pygame
from pygame.locals import *
import sys
from pysat.formula import CNF

from sources.Button import Button
from sources.Menu import Menu
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


def updateDIMACS(verbose=False):
    grillState = grid.returnGridState()
    grill = grid.returnGridNearby()

    liste_to_dimacs(grill, grillState, False)
    formula = CNF(from_file='DIMACS.cnf').clauses
    solution = None
    try:
        solution = pycosat.solve(formula)

    except ValueError:
        print("Erreur solveur !!!")

    if verbose:
        print("Valeurs complété", grillState)
        print("Nombres de grilles Adjacente", grill)
        print("dimacs: ", formula)
        print("SAT : ", solution)



def init_grille(nb_bombes: int = 2, pourcentage_affiche: float = 1, taille_bombes_verticals: int = 3,
                taille_bombes_horizontal: int = 3):
    nb_grilles_affiche = taille_bombes_verticals * taille_bombes_horizontal
    nb_grilles_affiche = int(nb_grilles_affiche * pourcentage_affiche)
    return Grid(DISPLAY, textures, padding_side, padding_top + menu_height + padding_middle,
                display_width - padding_side, display_height - padding_bottom, nb_bombes, nb_grilles_affiche,
                taille_bombes_horizontal, taille_bombes_verticals)

def reveal_unreveal():
    grid.revealed = not grid.revealed



padding_top = 20
padding_middle = 0
padding_bottom = 20
padding_side = 20
width = 1000
menu_height = 200
grille_height = 500
display_width = width + 2 * padding_side
display_height = menu_height + grille_height + padding_top + padding_middle + padding_bottom

pygame.init()
pygame.font.init()

DISPLAY = pygame.display.set_mode((display_width, display_height), 0, 32)
WHITE = (100, 100, 100)
DISPLAY.fill(WHITE)
textures = load_images()

grid = init_grille(nb_bombes=4, taille_bombes_horizontal=10, taille_bombes_verticals=5)

def regen_grid():
    global grid
    grid = init_grille(nb_bombes=4, taille_bombes_horizontal=10, taille_bombes_verticals=5)


buttons = []
buttons.append(Button(padding_side, padding_top, 30, 30, 10, lambda: reveal_unreveal()))
buttons.append(Button(padding_side*2+30, padding_top, 30, 30, 10, lambda: regen_grid()))
buttons.append(Button(padding_side*3+30*2, padding_top, 30, 30, 10, lambda: print("3 !!!")))
buttons.append(Button(padding_side*4+30*3, padding_top, 30, 30, 10, lambda: print("4 !!!")))
menu = Menu(DISPLAY, textures, menu_height, buttons)



updateDIMACS()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:

            pos_x, pos_y = pygame.mouse.get_pos()
            if event.button == 1:
                grid.toggle(pos_x, pos_y)
                menu.get_clicked(pos_x, pos_y)
            if event.button == 3:
                grid.toggleBombe(pos_x, pos_y)

            updateDIMACS()
    menu.draw_menu()
    grid.draw_grid()
    pygame.display.update()

