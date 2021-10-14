import pygame
import math
import random

from pygame import display
from pygame import image

X = pygame.Surface((80, 80))
pygame.Surface.fill(X, (153, 170, 181))
pygame.draw.rect(X, (33, 33, 33), (0, 20, 80, 40))
pygame.draw.rect(X, (33, 33, 33), (20, 0, 40, 80))
pygame.draw.rect(X, (55, 55, 55), (30, 0, 20, 80))
pygame.draw.rect(X, (55, 55, 55), (0, 30, 80, 20))
Y = pygame.Surface((80, 80))
pygame.Surface.fill(Y, (153, 170, 181))
pygame.draw.rect(Y, (33, 33, 33), (20, 0, 40, 80))
pygame.draw.rect(Y, (33, 33, 33), (0, 20, 40, 40))
pygame.draw.rect(Y, (55, 55, 55), (30, 0, 20, 80))
pygame.draw.rect(Y, (55, 55, 55), (0, 30, 40, 20))
I = pygame.Surface((80, 80))
pygame.Surface.fill(I, (153, 170, 181))
pygame.draw.rect(I, (33, 33, 33), (20, 0, 40, 80))
pygame.draw.rect(I, (55, 55, 55), (30, 0, 20, 80))
L = pygame.Surface((80, 80))
pygame.Surface.fill(L, (153, 170, 181))
pygame.draw.rect(L, (33, 33, 33), (20, 20, 40, 60))
pygame.draw.rect(L, (33, 33, 33), (0, 20, 60, 40))
pygame.draw.rect(L, (55, 55, 55), (30, 30, 20, 50))
pygame.draw.rect(L, (55, 55, 55), (0, 30, 50, 20))

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
            if Counter == (720 / self.tile_width):
                fmap.append(row)
                row = []
                Counter = 0
        return fmap

    def create_ground(self, row, column):
        G = pygame.Surface((80, 80))
        pygame.Surface.fill(G, (78, 52, 46))
        if column == 0:
            pygame.draw.rect(G, (62, 39, 35), (0,0,80,20))
        elif column == 8:
            pygame.draw.rect(G, (62, 39, 35), (0,60,80,20))

        if row == 0:
            pygame.draw.rect(G, (62, 39, 35), (0,0,20,80))
        elif row == 10:
            pygame.draw.rect(G, (62, 39, 35), (60,0,20,80))
        
        if column != 0:
            if self.map[row][column - 1] == "-":
                pygame.draw.rect(G, (93, 64, 55), (0,0,80,20))
        if column != 8:
            if self.map[row][column + 1] == "-":
                pygame.draw.rect(G, (93, 64, 55), (0,60,80,20))
        if row != 0:
            if self.map[row - 1][column] == "-":
                pygame.draw.rect(G, (93, 64, 55), (0,0,20,80))
        if row != 10:
            if self.map[row + 1][column] == "-":
                pygame.draw.rect(G, (93, 64, 55), (60,0,20,80))
    
        for i in range(1,random.randint(1,9)):
            pygame.draw.rect(G, (109, 76, 65), (random.randint(0,9)*10, random.randint(0,9)*10, 10, 10))
        for i in range(1,random.randint(1,9)):
            pygame.draw.rect(G, (121, 85, 72), (random.randint(0,9)*10, random.randint(0,9)*10, 10, 10))
        return G       
            

        
    def create_image_map(self):
        self.image_map = []
        for row in range(len(self.map)):
            line = []
            for column in range(len(self.map[row])):
                if self.map[row][column] == "#":
                    line.append(self.create_ground(row, column))
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
        
    
    def draw(self):
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                x = row * self.tile_width
                y = column * self.tile_width
                self.display.blit(self.image_map[row][column], (x, y))
