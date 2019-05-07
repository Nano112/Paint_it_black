class Button:

    def __init__(self, texture_id):



    def draw_cell(self, DISPLAY, textures):
    if self.state:
        DISPLAY.blit(pygame.transform.scale(textures[11], (self.width, self.height)),
                     (self.x_pos, self.y_pos))
    else:
        DISPLAY.blit(pygame.transform.scale(textures[10], (self.width, self.height)),
                     (self.x_pos, self.y_pos))
    if self.is_shown:
        DISPLAY.blit(pygame.transform.scale(textures[self.nearby_black_cells], (self.width, self.height)),
                     (self.x_pos, self.y_pos))
    if revealed and self.is_black:
        DISPLAY.blit(pygame.transform.scale(textures[12], (self.width, self.height)),
                     (self.x_pos, self.y_pos))