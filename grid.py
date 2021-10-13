import pygame
import math
import random


class Grid():
    def __init__(self, map, tile_width):
        self.tile_width = tile_width
        self.map = self.initailise_map(map)

    def get_grid_value(self, xy):
        x , y = xy
        return self.map[math.floor(x / self.tile_width)][math.floor(y / self.tile_width)]

    def initailise_map(self, map):
        row = []
        fmap = []
        Counter = 0
        for charecter in map:
            Counter += 1
            row.append(charecter)
            if Counter == (900 / self.tile_width):
                fmap.append(row)
                row = []
                Counter = 0
        return fmap
    
    def draw(self, surface):
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                if self.map[row][column] == "#":
                    x = row * self.tile_width
                    y = column * self.tile_width
                    pygame.draw.rect(surface, (0, 0, 0), (x, y ,self.tile_width, self.tile_width))
