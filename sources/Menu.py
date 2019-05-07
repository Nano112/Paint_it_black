from sources.Button import Button


class Menu:
    def __init__(self, DISPLAY, textures, height, buttons=[]):
        self.DISPLAY = DISPLAY
        self.textures = textures
        self.buttons = buttons
        self.height = height
        self.buttons.append(Button(30, 30, 10, 10, 12, lambda: print("CLICK !!!")))

    def draw_menu(self):
        self.draw_buttons()

    def draw_buttons(self):
        for b in self.buttons:
            b.draw_button(self.DISPLAY, self.textures)

    def get_clicked(self,pos_x,pos_y):
        for b in self.buttons:
            if b.is_clicked:
                b.execute()
