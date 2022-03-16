from pygame import Surface, draw
from math import floor
from random import randint


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
            
 
class Server_Grid(Grid):
    def __init__(self, mapnum):
        super().__init__(mapnum)
        
    def get_grid_value(self, xy):
        x , y = xy       
        return self.map[floor(x / 80)][floor(y / 80)]        
        
        
class Client_Grid(Grid):
    def __init__(self, mapnum, tile_width, display):
        super().__init__(mapnum)
        self.tile_width = tile_width
        self.display = display
        self.create_image_map()
        
    def create_ground(self, row, column):
        G = Surface((80, 80))
        Surface.fill(G, (78, 52, 46))
        if column == 0:
            draw.rect(G, (62, 39, 35), (0,0,80,20))
        elif column == 8:
            draw.rect(G, (62, 39, 35), (0,60,80,20))

        if row == 0:
            draw.rect(G, (62, 39, 35), (0,0,20,80))
        elif row == 10:
            draw.rect(G, (62, 39, 35), (60,0,20,80))
        
        if column != 0:
            if self.map[row][column - 1] == "-":
                draw.rect(G, (93, 64, 55), (0,0,80,20))
        if column != 8:
            if self.map[row][column + 1] == "-":
                draw.rect(G, (93, 64, 55), (0,60,80,20))
        if row != 0:
            if self.map[row - 1][column] == "-":
                draw.rect(G, (93, 64, 55), (0,0,20,80))
        if row != 10:
            if self.map[row + 1][column] == "-":
                draw.rect(G, (93, 64, 55), (60,0,20,80))
    
        for i in range(1,randint(1,9)):
            draw.rect(G, (109, 76, 65), (randint(0,9)*10, randint(0,9)*10, 10, 10))
        for i in range(1,randint(1,9)):
            draw.rect(G, (121, 85, 72), (randint(0,9)*10, randint(0,9)*10, 10, 10))
        return G       
        
        
        
#Creates a surface that serves as the background for the game
    def create_image_map(self):
        self.image_map = []
        self.image_map = self.display.copy()
        for x in range(len(self.map)):
            line = []
            for y in range(len(self.map[x])):
                if self.map[x][y] == "#":
                    Blank = self.create_ground(x, y)
                else:
                    Blank = Surface((80, 80))
                    Surface.fill(Blank, (153, 170, 181))

                    #Surround = [N, E, S, W]
                    Surround = [self.map[x][y - 1], self.map[x + 1][y], self.map[x][y + 1], self.map[x - 1][y]]

                    for i in [[(33, 33, 33),0,0],[(55, 55, 55),10,20]]:
                        if Surround[0] == "-":
                            draw.rect(Blank, i[0], (20+i[1], 0, 40 - i[2], 60 - i[2]))
                        if Surround[1] == "-":
                            draw.rect(Blank, i[0], (20+i[1], 20+i[1], 60, 40 - i[2]))
                        if Surround[2] == "-":
                            draw.rect(Blank, i[0], (20+i[1], 20+i[1], 40 - i[2], 60- i[1]))
                        if Surround[3] == "-":
                            draw.rect(Blank, i[0], (0, 20+i[1], 60- i[1], 40 - i[2]))

                    draw.rect(Blank, (55, 55, 55), (30, 30, 20, 20))
                self.image_map.blit(Blank, (x * self.tile_width, y * self.tile_width))
    
    def draw(self):
        self.display.blit(self.image_map , (0,0))
    
    
