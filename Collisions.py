
class Collisions():
    def __init__(self, mapnum):
        if mapnum == 0:
            self.map = initailise_map("##########-------##-###-#-##-----#-##-###-#-##-------##-#-###-##-#-----##-#-###-##-------##########")
        elif mapnum == 1:
            self.map = initailise_map("##########-------##-#-#-#-##---#-#-####-#-#-##---#---##-#-#-####-#-#---##-#-#-#-##-------##########")
        elif mapnum == 2:
            self.map = initailise_map("##########-------##-#####-##-------##-#-#-#-##---#---##-#-#-#-##-------##-#####-##-------##########")
        elif mapnum == 3:
            self.map = initailise_map("##########-------##-#-###-##-#---#-##-#-#---##-#-#-#-##---#-#-##-#---#-##-###-#-##-------##########")
        elif mapnum == 4:
            self.map = initailise_map("##########-------##-#-###-##-#-###-##-------##-##-##-##-------##-###-#-##-###-#-##-------##########")
        elif mapnum == 5:
            self.map = initailise_map("##########-------##-##-##-##-------##-#-#-#-##-#-#-#-##-#-#-#-##-------##-##-##-##-------##########")
        elif mapnum == 6:
            self.map = initailise_map("##########------###-####-###-#-----##---#-#-##-#---#-##-#-#---##-----#-###-####-###------##########")
        elif mapnum == 7:
            self.map = initailise_map("##########-------##-#####-##-------###-#-#-####-----####-#-#-###-------##-#####-##-------##########")     

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
    
    def get_grid_value(self, xy):
        x , y = xy
        return self.map[math.floor(x / self.tile_width)][math.floor(y / self.tile_width)]
