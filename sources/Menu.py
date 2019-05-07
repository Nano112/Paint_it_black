from sources.Button import Button


class Menu:
    def __init__(self, DISPLAY, textures, height, buttons=[], outputs=[]):
        self.DISPLAY = DISPLAY
        self.textures = textures
        self.buttons = buttons
        self.outputs = outputs
        self.height = height

    def draw_menu(self):
        self.draw_buttons()
        self.draw_outputs()

    def draw_buttons(self):
        for b in self.buttons:
            b.draw_button(self.DISPLAY, self.textures)

    def draw_outputs(self):
        for o in self.outputs:
            o.draw_output(self.DISPLAY, self.textures)

    def get_clicked(self,pos_x,pos_y):
        for b in self.buttons:
            if b.is_clicked(pos_x,pos_y):
                b.execute()
