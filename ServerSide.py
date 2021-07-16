Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@Yout-bit 
Yout-bit
/
NEA
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
NEA/main.py /
@Yout-bit
Yout-bit fgh
Latest commit 207eebe 9 days ago
 History
 1 contributor
163 lines (131 sloc)  5.04 KB
  
import sys
import pygame
from pygame.key import *
from pygame.locals import *
import math
import random
#from OpenGL.GL import *
#from OpenGL.GLU import *


from player import Player
from grid import Grid
from projectile import Projectile 



#Establishing coolours
Colours = {
    "BLUEY" : (144, 137, 218),
    "GREY"  : (153, 170, 181),
    "DARK"  : (44, 47, 51),
    "BLUE"  : (0, 0, 255),
    "RED"   : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLACK" : (0, 0, 0),
    "WHITE" : (255, 255, 255)
    }

#Establishing functions
def map():
    map_choice = random.randint(0,5)
    if map_choice == 0:
        MAP = "##########-------##-###-#-##-----#-##-###-#-##-------##-#-###-##-#-----##-#-###-##-------##########"
    elif map_choice == 1:
        MAP = "##########-------##-#-#-#-##---#-#-####-#-#-##---#---##-#-#-####-#-#---##-#-#-#-##-------##########"
    elif map_choice == 2:
        MAP = "##########-------##-#####-##-------##-#-#-#-##---#---##-#-#-#-##-------##-#####-##-------##########"
    elif map_choice == 3:
        MAP = "##########-------##-#-###-##-#---#-##-#-#---##-#-#-#-##---#-#-##-#---#-##-###-#-##-------##########"
    elif map_choice == 4:
        MAP = "##########-------##-#-###-##-#-###-##-------##-##-##-##-------##-###-#-##-###-#-##-------##########"
    elif map_choice == 5:
        MAP = "##########-------##-##-##-##-------##-#-#-#-##-#-#-#-##-#-#-#-##-------##-##-##-##-------##########"
    return MAP

def setup():
    MAP = map()
    TILE_WIDTH = math.sqrt((SCREEN_HEIGHT * SCREEN_WIDTH) /  len(MAP)) 
    level = Grid(MAP, TILE_WIDTH)
    P1 = Player(TILE_WIDTH, 5, TILE_WIDTH, TILE_WIDTH, level, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q], "1", (174, 137, 218))
    P2 = Player(TILE_WIDTH, 5, (9) * TILE_WIDTH, (7) * TILE_WIDTH, level, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE], "2", (124, 227, 228))
    S1 = Projectile(15, P1, level, (0, 0, 0))
    S2 = Projectile(15, P2, level, (0, 255, 0))
    return P1, P2, S1, S2, level
      

def check_hit(player, projectile):
    hitbox = player.get_hitbox()
    if hitbox != None:
        if hitbox.collidepoint(projectile.center):
            projectile.destroy()
            return True
        else:
            return False


P1, P2, S1, S2, level = setup()
P1ready = P2ready = False
P1text = "Press q to ready"
P2text = "Press space to ready"
COUNTDOWN = FPS * 5 * 0


#Main loop
game = "start"
while True:
    if game == "start":

        DISPLAYSURF.blit(TEXT.render(P1text, True, Colours["BLACK"]), (50, 50))
        DISPLAYSURF.blit(TEXT.render(P2text, True, Colours["BLACK"]), (50, 150))
        if pygame.key.get_pressed()[pygame.K_q]:
            P1ready = True
            P1text = "Player 1 is ready"
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            P2ready = True
            P2text = "Player 2 is ready"

        if P1ready and P2ready:
            COUNTDOWN -= 1
            DISPLAYSURF.blit(NUMBERS.render(str(COUNTDOWN // FPS + 1), True, Colours["BLACK"]), (SCREEN_WIDTH //2 , SCREEN_HEIGHT // 2 ))
        if COUNTDOWN == 0: 
            game = "playing"

    elif game == "playing":
        P1.update()
        P2.update()
        S1.update()
        S2.update()

        P2_winner = check_hit(P1, S2)
        P1_winner = check_hit(P2, S1)
        if P1_winner or P2_winner:
            game = "end"



    #End screen  
    elif game == "end":        
        pygame.display.update()

        DISPLAYSURF.fill(Colours["GREY"])
        if P1_winner:
            DISPLAYSURF.blit(TEXT.render("Player 1 is the winner", True, Colours["GREEN"]), (50, 50) )
        else:
            DISPLAYSURF.blit(TEXT.render("Player 2 is the winner", True, Colours["GREEN"]), (50, 50) )
        DISPLAYSURF.blit(TEXT.render("Press p to play again", True, Colours["GREEN"]), (50, 150) )

        if pygame.key.get_pressed()[pygame.K_p]:
            P1, P2, S1, S2, level = setup()
            P1ready = P2ready = False
            P1text = "Press q to ready"
            P2text = "Press space to ready"
            COUNTDOWN = FPS * 5
            game = "start"
            COUNTDOWN = FPS * 3




