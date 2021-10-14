import pygame
import math
import random

from pygame import display
from pygame import image

B1 = pygame.image.load(r'Images/B1.png')
B2 = pygame.image.load(r'Images/B2.png')
B3 = pygame.image.load(r'Images/B3.png')

X = pygame.image.load(r'Images/X Block.png')
Y = pygame.image.load(r'Images/Y Block.png')
I = pygame.image.load(r'Images/I Block.png')
L = pygame.image.load(r'Images/L Block.png')

Background = []
for i in range(15):
    Row = []
    for j in range(15):
        rng = random.randint(1,3)
        if rng == 1:
            Row.append(B1)
        elif rng == 2:
            Row.append(B2)
        else:
            Row.append(B3)
    Background.append(Row)

class Grid():
    def __init__(self, map, tile_width, display):
        self.tile_width = tile_width
        self.display = display
        self.map = self.initailise_map(map)
        self.create_image_map()


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
        
    def create_image_map(self):
        self.image_map = []
        for row in range(len(self.map)):
            line = []
            for column in range(len(self.map[row])):
                if self.map[row][column] == "#":
                    line.append(Background[row][column])
                else:
                    if self.map[row-1][column] == "-" and self.map[row][column-1] == "-" and self.map[row][column+1] == "-" and self.map[row+1][column] == "-":
                        line.append(X)
                    elif self.map[row-1][column] == "#" and self.map[row][column-1] == "-" and self.map[row][column+1] == "-" and self.map[row+1][column] == "#":
                        line.append(I)    
                    elif self.map[row-1][column] == "-" and self.map[row][column-1] == "#" and self.map[row][column+1] == "#" and self.map[row+1][column] == "-":
                        line.append(pygame.transform.rotate(I, 90))
                    elif self.map[row-1][column] == "-" and self.map[row][column-1] == "#" and self.map[row][column+1] == "-" and self.map[row+1][column] == "#":
                        line.append(L)
                    elif self.map[row-1][column] == "#" and self.map[row][column-1] == "#" and self.map[row][column+1] == "-" and self.map[row+1][column] == "-":
                        line.append(pygame.transform.rotate(L, 90))
                    elif self.map[row-1][column] == "#" and self.map[row][column-1] == "-" and self.map[row][column+1] == "#" and self.map[row+1][column] == "-":
                        line.append(pygame.transform.rotate(L, 180))
                    elif self.map[row-1][column] == "-" and self.map[row][column-1] == "-" and self.map[row][column+1] == "#" and self.map[row+1][column] == "#":
                        line.append(pygame.transform.rotate(L, 270))
                    elif self.map[row+1][column] == "#":
                        line.append(Y)
                    elif self.map[row][column-1] == "#":
                        line.append(pygame.transform.rotate(Y, 90))
                    elif self.map[row-1][column] == "#":
                        line.append(pygame.transform.rotate(Y, 180))
                    else:
                        line.append(pygame.transform.rotate(Y, 270))
            self.image_map.append(line)
        
    
    def draw(self, surface):
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                x = row * self.tile_width
                y = column * self.tile_width
                self.display.blit(self.image_map[row][column], (x, y))
