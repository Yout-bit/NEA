import pygame
import math
import random
import sys

from pygame import display
from pygame import image


class Grid():
    def __init__(self, mapnum):
        self.select_map(mapnum)
        self.map = self.initailise_map(self.map)

        
    def initailise_map(self, map):
        row = []
        fmap = []
        Counter = 0
        for charecter in map:
            Counter += 1
            row.append(charecter)
            if Counter == (9):
                fmap.append(row)
                row = []
                Counter = 0
        return fmap 
    
    def select_map(self, mapnum):  
        if mapnum == 0:
            self.map = "##########-------##-###-#-##-----#-##-###-#-##-------##-#-###-##-#-----##-#-###-##-------##########"
        elif mapnum == 1:
            self.map = "##########-------##-#-#-#-##---#-#-####-#-#-##---#---##-#-#-####-#-#---##-#-#-#-##-------##########"
        elif mapnum == 2:
            self.map = "##########-------##-#####-##-------##-#-#-#-##---#---##-#-#-#-##-------##-#####-##-------##########"
        elif mapnum == 3:
            self.map = "##########-------##-#-###-##-#---#-##-#-#---##-#-#-#-##---#-#-##-#---#-##-###-#-##-------##########"
        elif mapnum == 4:
            self.map = "##########-------##-#-###-##-#-###-##-------##-##-##-##-------##-###-#-##-###-#-##-------##########"
        elif mapnum == 5:
            self.map = "##########-------##-##-##-##-------##-#-#-#-##-#-#-#-##-#-#-#-##-------##-##-##-##-------##########"
        elif mapnum == 6:
            self.map = "##########------###-####-###-#-----##---#-#-##-#---#-##-#-#---##-----#-###-####-###------##########"
        elif mapnum == 7:
            self.map = "##########-------##-#####-##-------###-#-#-####-----####-#-#-###-------##-#####-##-------##########"
            
            
class Collisions(Grid):
    def __init__(self, mapnum):
        Grid
    
