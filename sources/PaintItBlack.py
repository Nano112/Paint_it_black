import pycosat as pycosat
import pygame
from pygame.locals import *
import sys
from pysat.formula import CNF

from sources.Button import Button
from sources.Menu import Menu
from sources.Grid import Grid
from sources.Output import Output
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


def updateDIMACS(verbose=True):
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


def init_grille(nb_bombes: int = 2, nb_grilles_affiche: int = 1, taille_bombes_verticals: int = 3,
                taille_bombes_horizontal: int = 3):
    return Grid(DISPLAY, textures, padding_side, padding_top + menu_height + padding_middle,
                display_width - padding_side, display_height - padding_bottom, nb_bombes, nb_grilles_affiche,
                taille_bombes_horizontal, taille_bombes_verticals)


def reveal_unreveal():
    grid.revealed = not grid.revealed


def get_nb_cells_horizontal():
    global grid
    return grid.nb_cells_horizontal


def get_nb_cells_vertical():
    global grid
    return grid.nb_cells_vertical


def set_nb_cells_horizontal(n):
    global grid
    grid.nb_cells_horizontal = n


def set_nb_cells_vertical(n):
    global grid
    grid.nb_cells_vertical = n


def increase_cells_horizontal():
    set_nb_cells_horizontal(get_nb_cells_horizontal() + 1)


def increase_cells_vertical():
    set_nb_cells_vertical(get_nb_cells_vertical() + 1)


def decrease_cells_horizontal():
    set_nb_cells_horizontal(get_nb_cells_horizontal() - 1)


def decrease_cells_vertical():
    set_nb_cells_vertical(get_nb_cells_vertical() - 1)


padding_top = 0
padding_middle = 0
padding_bottom = 0
padding_side = 0
width = 600
menu_height = 0
grille_height = 600
display_width = width + 2 * padding_side
display_height = menu_height + grille_height + padding_top + padding_middle + padding_bottom

pygame.init()
pygame.font.init()

DISPLAY = pygame.display.set_mode((display_width, display_height), 0, 32)
WHITE = (100, 100, 100)
DISPLAY.fill(WHITE)
textures = load_images()

nb_cases_noir = 20

nb_cases_afficher = 70

nb_cases_verticals = 10

nb_cases_horizontal = 10

grid = init_grille(nb_cases_noir, nb_cases_afficher, nb_cases_verticals, nb_cases_horizontal)


def regen_grid():
    global grid
    grid = init_grille(nb_cases_noir, nb_cases_afficher, nb_cases_verticals, nb_cases_horizontal)


buttons = []
outputs = []

standard_size = 30


def plus_moin(pos_x, pos_y, string, l1, l2):
    global buttons
    global outputs
    buttons.append(Button(pos_x, pos_y, 30, 30, 10, l1))  # moin large
    outputs.append(Output(pos_x + padding_side + 30, pos_y, 60 + padding_side, 30, 10, string))
    buttons.append(Button(pos_x + padding_side * 3 + 90, pos_y, 30, 30, 10, l2))  # plus large


buttons.append(Button(padding_side, padding_top, standard_size, standard_size, 10,
                      lambda: reveal_unreveal()))  # afficher la solution
buttons.append(Button(padding_side * 2 + standard_size, padding_top, standard_size, standard_size, 10,
                      lambda: regen_grid()))  # regenere la grille


def diminuer_cases_noires():
    global nb_cases_noir
    nb_cases_noir = nb_cases_noir - 1


def augmenter_cases_noires():
    global nb_cases_noir
    nb_cases_noir = nb_cases_noir + 1


def diminuer_case_a_afficher():
    global nb_cases_afficher
    nb_cases_afficher = nb_cases_afficher - 1


def augmenter_cases_a_afficher():
    global nb_cases_afficher
    nb_cases_afficher = nb_cases_afficher + 1


def diminuer_cases_horizontal():
    decrease_cells_horizontal()


def augmenter_cases_horizontal():
    increase_cells_horizontal()


def diminuer_cases_vertical():
    decrease_cells_vertical()


def augmenter_cases_horizontal():
    increase_cells_vertical()


plus_moin(200, padding_top, 'nb_noir', lambda: diminuer_cases_noires(),
          lambda: augmenter_cases_a_afficher())  # Nombres de cases noires
plus_moin(200, padding_top * 2 + standard_size, "nb_affiche", lambda: diminuer_case_a_afficher(),
          lambda: augmenter_cases_a_afficher())  # Nombres de case afficher
plus_moin(200, padding_top * 3 + standard_size * 2, "nb_horiz", lambda: diminuer_cases_horizontal(),
          lambda: augmenter_cases_horizontal())  # nombres de case horizontal
plus_moin(200, padding_top * 4 + standard_size * 3, "nb_vert", lambda: diminuer_cases_vertical(),
          lambda: augmenter_cases_horizontal())  # nombre de cases vertical

menu = Menu(DISPLAY, textures, menu_height, buttons, outputs)

updateDIMACS()
reveal_unreveal()
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
