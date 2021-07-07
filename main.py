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
    map_choice = random.randint(6,6)
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
    elif map_choice == 6:
        MAP = "###################----------------##-####-#-#######-##-#----#--#----#-##-#-#-###-#-##-#-##-#----#--#------##----#-#-###-#-#-##-##-#-#-###-#-#-##-##-#-#-------#-##-##-#-#-####-##-##-##-#-#----#-##-##-##-#----#-#-##-##-##-####-#-#-##-##-#-------#-#-##-##-#-#-###-#-#-##-##-#-#-###-#-#----##------#--#----#-##-#-##-#-###-#-#-##-#----#--#----#-##-#######-#-####-##----------------###################"
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

#Setting up the pygame window
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 900

#DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF|OPENGL)
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#gluPerspective(45, (SCREEN_WIDTH/SCREEN_HEIGHT), 0.1, 50.0)
#glTranslatef(0.0,0.0, -5)

TEXT = pygame.font.SysFont('didot.ttc', 140)
NUMBERS = pygame.font.SysFont('didot.ttc', 250)

pygame.display.set_caption("Game")

P1, P2, S1, S2, level = setup()
P1ready = P2ready = False
P1text = "Press q to ready"
P2text = "Press space to ready"
COUNTDOWN = FPS * 5 * 0


#Main loop
game = "start"
while True:
    if game == "start":
        pygame.display.update()
        DISPLAYSURF.fill(Colours["GREY"])

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
        pygame.display.update()

        DISPLAYSURF.fill(Colours["GREY"])

        P1.update()
        P2.update()
        S1.update()
        S2.update()

        P1.draw(DISPLAYSURF)
        P2.draw(DISPLAYSURF)
        level.draw(DISPLAYSURF)
        S1.draw(DISPLAYSURF)
        S2.draw(DISPLAYSURF)

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

    FramePerSec.tick(FPS)
    #Allows the window to be closed
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
