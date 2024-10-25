import pygame as pg
from settings import * 

_ = False
mini_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
    [1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,],
    [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        # Scaling factor for drawing
        scale_factor = 2  # Half the screen
        size_x = int(WIDTH / len(self.mini_map[0]))  # Width of each grid block
        size_y = int(HEIGHT / len(self.mini_map) / scale_factor)  # Height of each grid block
        
        for pos in self.world_map:
            # Draw the walls (grid blocks)
            pg.draw.rect(
                self.game.screen, 'darkgray',
                (pos[0] * size_x, pos[1] * size_y, size_x, size_y), 2
            )
            # Draw red circles for each map block
            # pg.draw.circle(self.game.screen, 'red', (pos[0] * size_x, pos[1] * size_y), 10)
