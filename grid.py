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
        
<<<<<<< HEAD
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
=======
    def create_ground(self, x, y):
        G = pygame.Surface((80, 80))
        pygame.Surface.fill(G, (78, 52, 46))
        if y == 0:
            pygame.draw.rect(G, (62, 39, 35), (0,0,80,20))
        elif y == 8:
            pygame.draw.rect(G, (62, 39, 35), (0,60,80,20))

        if x == 0:
            pygame.draw.rect(G, (62, 39, 35), (0,0,20,80))
        elif x == 10:
            pygame.draw.rect(G, (62, 39, 35), (60,0,20,80))
        
        if y != 0:
            if self.map[x][y - 1] == "-":
                pygame.draw.rect(G, (93, 64, 55), (0,0,80,20))
        if y != 8:
            if self.map[x][y + 1] == "-":
                pygame.draw.rect(G, (93, 64, 55), (0,60,80,20))
        if x != 0:
            if self.map[x - 1][y] == "-":
                pygame.draw.rect(G, (93, 64, 55), (0,0,20,80))
        if x != 10:
            if self.map[x + 1][y] == "-":
                pygame.draw.rect(G, (93, 64, 55), (60,0,20,80))
>>>>>>> 816ab7e2a3a6a07a175e47b35362ca5441b8affc
    
        for i in range(1,randint(1,9)):
            draw.rect(G, (109, 76, 65), (randint(0,9)*10, randint(0,9)*10, 10, 10))
        for i in range(1,randint(1,9)):
            draw.rect(G, (121, 85, 72), (randint(0,9)*10, randint(0,9)*10, 10, 10))
        return G       
        
        
        
#New image map creation:
    def create_image_map(self):
        self.image_map = []
        for x in range(len(self.map)):
            line = []
            for y in range(len(self.map[x])):
                if self.map[x][y] == "#":
                    line.append(self.create_ground(x, y))
                else:
                    Blanck = Surface((80, 80))
                    Surface.fill(Blanck, (153, 170, 181))

                    #Surround = [N, E, S, W]
                    Surround = [self.map[x][y - 1], self.map[x + 1][y], self.map[x][y + 1], self.map[x - 1][y]]

                    for i in [[(33, 33, 33),0,0],[(55, 55, 55),10,20]]:
<<<<<<< HEAD
                        if x[0] == "-":
                            draw.rect(Blanck, i[0], (20+i[1], 0, 40 - i[2], 60 - i[2]))
                        if x[1] == "-":
                            draw.rect(Blanck, i[0], (20+i[1], 20+i[1], 60, 40 - i[2]))
                        if x[2] == "-":
                            draw.rect(Blanck, i[0], (20+i[1], 20+i[1], 40 - i[2], 60- i[1]))
                        if x[3] == "-":
                            draw.rect(Blanck, i[0], (0, 20+i[1], 60- i[1], 40 - i[2]))
=======
                        if Surround[0] == "-":
                            pygame.draw.rect(Blanck, i[0], (20+i[1], 0, 40 - i[2], 60 - i[2]))
                        if Surround[1] == "-":
                            pygame.draw.rect(Blanck, i[0], (20+i[1], 20+i[1], 60, 40 - i[2]))
                        if Surround[2] == "-":
                            pygame.draw.rect(Blanck, i[0], (20+i[1], 20+i[1], 40 - i[2], 60- i[1]))
                        if Surround[3] == "-":
                            pygame.draw.rect(Blanck, i[0], (0, 20+i[1], 60- i[1], 40 - i[2]))
>>>>>>> 816ab7e2a3a6a07a175e47b35362ca5441b8affc

                    draw.rect(Blanck, (55, 55, 55), (30, 30, 20, 20))
                    #DRAW STIGHT ONTO SURFACE RATHER THAN ADDING TO LIST?????!!!!!
                    line.append(Blanck)
            self.image_map.append(line)
<<<<<<< HEAD
        self.cheese = self.display.copy()
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                x = row * self.tile_width
                y = column * self.tile_width
                self.cheese.blit(self.image_map[row][column], (x, y))
    
    def draw(self):
        self.display.blit(self.cheese, (0,0))
=======
    
    def draw(self):
        for comumn in range(len(self.map)):
            for row in range(len(self.map[column])):
                x = column * self.tile_width
                y = row * self.tile_width
                self.display.blit(self.image_map[column][row], (x, y))
>>>>>>> 816ab7e2a3a6a07a175e47b35362ca5441b8affc
    
    
