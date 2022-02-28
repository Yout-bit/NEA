import math
import sys

class Collisions():
    def __init__(self, mapnum):
        self.mapnum = mapnum
        if mapnum == 0:
            self.map = self.initailise_map("##########-------##-###-#-##-----#-##-###-#-##-------##-#-###-##-#-----##-#-###-##-------##########")
        elif mapnum == 1:
            self.map = self.initailise_map("##########-------##-#-#-#-##---#-#-####-#-#-##---#---##-#-#-####-#-#---##-#-#-#-##-------##########")
        elif mapnum == 2:
            self.map = self.initailise_map("##########-------##-#####-##-------##-#-#-#-##---#---##-#-#-#-##-------##-#####-##-------##########")
        elif mapnum == 3:
            self.map = self.initailise_map("##########-------##-#-###-##-#---#-##-#-#---##-#-#-#-##---#-#-##-#---#-##-###-#-##-------##########")
        elif mapnum == 4:
            self.map = self.initailise_map("##########-------##-#-###-##-#-###-##-------##-##-##-##-------##-###-#-##-###-#-##-------##########")
        elif mapnum == 5:
            self.map = self.initailise_map("##########-------##-##-##-##-------##-#-#-#-##-#-#-#-##-#-#-#-##-------##-##-##-##-------##########")
        elif mapnum == 6:
            self.map = self.initailise_map("##########------###-####-###-#-----##---#-#-##-#---#-##-#-#---##-----#-###-####-###------##########")
        elif mapnum == 7:
            self.map = self.initailise_map("##########-------##-#####-##-------###-#-#-####-----####-#-#-###-------##-#####-##-------##########")    


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
    
    def get_grid_value(self, xy):
        x , y = xy       
        return self.map[math.floor(x / 80)][math.floor(y / 80)]
