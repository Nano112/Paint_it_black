import pygame

from sources import Grid


class Cell:
    def __init__(self, x_pos, y_pos, width, height, is_black):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.is_black = is_black
        self.state = False
        self.nearby_black_cells = 0
        self.is_shown = False

    def draw_cell(self, DISPLAY, textures, revealed):
        if self.state:
            DISPLAY.blit(pygame.transform.scale(textures[11], (self.width, self.height)),
                         (self.x_pos, self.y_pos))
        else:
            DISPLAY.blit(pygame.transform.scale(textures[10], (self.width, self.height)),
                         (self.x_pos, self.y_pos))
        if self.is_shown:
            DISPLAY.blit(pygame.transform.scale(textures[self.nearby_black_cells], (self.width, self.height)), (self.x_pos,self.y_pos))
        if revealed and self.is_black:
            DISPLAY.blit(pygame.transform.scale(textures[12], (self.width, self.height)),
                         (self.x_pos, self.y_pos))