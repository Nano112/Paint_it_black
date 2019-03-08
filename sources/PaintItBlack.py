
import pygame
from pygame.locals import *
import sys

from sources.Grid import Grid


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


display_width = 640
display_height = 840
pygame.init()

DISPLAY = pygame.display.set_mode((display_width, display_height), 0, 32)

WHITE = (255, 255, 255)

DISPLAY.fill(WHITE)
textures = load_images()

grid = Grid(DISPLAY, textures, 20, 220, display_width-20, display_height-20, 1, 16, 4, 4)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos_x, pos_y = pygame.mouse.get_pos()
            if event.button == 1:
                grid.toggle(pos_x,pos_y)
            if event.button == 3:
                grid.revealed = not grid.revealed

    grid.draw_grid()
    pygame.display.update()




