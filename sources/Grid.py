import random

from sources.Cell import Cell


class Grid:
    def __init__(self,DISPLAY, textures, x_min, y_min, x_max, y_max, nb_black_cells,nb_nearby_cells, nb_cells_horizontal, nb_cells_vertical):
        self.cell_width = (x_max - x_min ) // nb_cells_horizontal
        self.cell_height = (y_max - y_min) // nb_cells_vertical
        self.DISPLAY = DISPLAY
        self.textures = textures
        self.nb_black_cells = nb_black_cells
        self.nb_nearby_cells = nb_nearby_cells
        self.grid= [ [ None for y in range( nb_cells_vertical ) ] for x in range( nb_cells_horizontal ) ]
        self.nb_cells_horizontal = nb_cells_horizontal
        self.nb_cells_vertical = nb_cells_vertical
        self.x_min_position = x_min
        self.x_max_position = x_max
        self.y_min_position = y_min
        self.y_max_position = y_max
        self.revealed = False
        self.create_grid()
        self.error = nb_black_cells

    def draw_grid(self):
        for i in range(0, self.nb_cells_horizontal):
            for j in range(0, self.nb_cells_vertical):
                self.grid[i][j].draw_cell(self.DISPLAY, self.textures, self.revealed)

    def toggle(self, x_position, y_position):
        x_index, y_index = self.pos_to_index(x_position, y_position)
        if x_index == None or y_index == None:
            return
        #print(repr(x_index)+' ' + repr(y_index))
        self.grid[x_index][y_index].state = not self.grid[x_index][y_index].state
        if self.grid[x_index][y_index].state == self.grid[x_index][y_index].is_black:
            self.error -=1
        else:
            self.error +=1
        if(self.error == 0):
            print('Victoire')


    def index_to_pos(self, x_index, y_index):
        return x_index*self.cell_width+self.x_min_position,y_index*self.cell_height+self.y_min_position

    def pos_to_index(self, x_position, y_position):
        x_index = x_position - self.x_min_position
        y_index = y_position - self.y_min_position
        x_index = x_index // self.cell_width
        y_index = y_index // self.cell_height
        if  (x_index>=self.nb_cells_horizontal) or (x_index<0) or (y_index>=self.nb_cells_vertical) or (y_index<0):
            return
        return x_index,y_index

    def is_black(self,x_index ,y_index):
        if x_index<0 or x_index >= self.nb_cells_horizontal:
            return False
        if y_index < 0 or y_index >= self.nb_cells_vertical:
            return False
        return self.grid[x_index][y_index].is_black

    def is_shown(self,x_index ,y_index):
        if x_index<0 or x_index >= self.nb_cells_horizontal:
            return False
        if y_index < 0 or y_index >= self.nb_cells_vertical:
            return False
        return self.grid[x_index][y_index].is_shown

    def create_grid(self):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[0])):
                x_position, y_position = self.index_to_pos(i, j)
                self.grid[i][j] = Cell(x_position, y_position, self.cell_width, self.cell_height, False,i *len(self.grid[0])+j+1)
                print(i *len(self.grid[0])+j+1)

        for i in range(0, self.nb_black_cells):  # pose le nombre de bombes nécéssaire
            x, y = random_pos(self.nb_cells_horizontal, self.nb_cells_vertical)
            while (self.is_black(x, y) == True):
                x, y = random_pos(self.nb_cells_horizontal, self.nb_cells_vertical)
            self.grid[x][y].is_black = True

        for i in range(0, self.nb_nearby_cells):  # pose le nombre cases visibles
            x, y = random_pos(self.nb_cells_horizontal, self.nb_cells_vertical)
            while (self.is_shown(x, y) == True):
                x, y = random_pos(self.nb_cells_horizontal, self.nb_cells_vertical)
            self.grid[x][y].is_shown = True
            # pose la case visible seulement si la position n'est pas deja utilisé


        self.set_nearby_black_cell_count()

    def forme_logique(self):
        pass #A faire



    def nearby_black_cell_count(self, x_index, y_index):
        val = 0
        val += self.is_black(x_index - 1, y_index - 1)
        val += self.is_black(x_index    , y_index - 1)
        val += self.is_black(x_index + 1, y_index - 1)
        val += self.is_black(x_index - 1, y_index    )
        val += self.is_black(x_index    , y_index    )
        val += self.is_black(x_index + 1, y_index    )
        val += self.is_black(x_index - 1, y_index + 1)
        val += self.is_black(x_index    , y_index + 1)
        val += self.is_black(x_index + 1, y_index + 1)
        return val

    def set_nearby_black_cell_count(self):
        for x in range(0,self.nb_cells_horizontal):
            for y in range(0, self.nb_cells_vertical):
                self.grid[x][y].nearby_black_cells = self.nearby_black_cell_count(x,y)


def random_pos(x_max, y_max):
    return random.randrange(x_max), random.randrange(y_max)
    # fonction retournant un tuple de position