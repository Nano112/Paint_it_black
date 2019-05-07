import pygame


class Output:

    def __init__(self, x, y, largeur, hauteur, texture_id, string,police ='Comic Sans MS', taille = 10):
        self.font = pygame.font.SysFont(police, taille)
        self.string = string
        self.largeur = largeur
        self.hauteur = hauteur
        self.x = x
        self.y = y
        self.texture_id = texture_id


    def execute(self):
        self.function()

    def is_clicked(self, posX, posY):
        if (posX > self.x) and (posX < (self.x + self.largeur)):
            if (posY > self.y) and (posY < (self.y + self.hauteur)):
                return True
        return False




    def draw_text(self, DISPLAY, textures):
        textsurface = self.font.render(self.string, False, (0, 0, 0))
        DISPLAY.blit(pygame.transform.scale(textures[self.texture_id], (self.largeur, self.hauteur)), (self.x, self.y))
        DISPLAY.blit(pygame.transform.scale(textsurface, (self.largeur, self.hauteur)), (self.x, self.y))
