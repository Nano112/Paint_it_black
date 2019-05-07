import pygame


class Button:

    def __init__(self, largeur, hauteur, x, y, texture_id, function= lambda : print("fauxBoutton")):
        self.function = function
        self.largeur = largeur
        self.hauteur = hauteur
        self.x = x
        self.y = y
        self.texture_id = texture_id


    def execute(self):
        self.function()

    def is_clicked(self,posX,posY):
        if posX > self.x & posX < self.x + self.largeur:
            if posY > self.y & posY < self.y + self.hauteur:
                return True
        return False




    def draw_button(self, DISPLAY, textures):
        DISPLAY.blit(pygame.transform.scale(textures[self.texture_id], (self.largeur, self.hauteur)), (self.x, self.y))
