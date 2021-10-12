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
    "WHITE" : (255, 255, 255)  ,
    "SHADOW": (103, 120, 131)
    }

#Establishing functions
def map():
    map_choice = random.randint(0,6)
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
        MAP = "##########------###-####-###-#-----##---#-#-##-#---#-##-#-#---###-####-# ##------##-------# #########"        
    return MAP

def setup():
    MAP = map()
    TILE_WIDTH = math.sqrt((SCREEN_HEIGHT * SCREEN_WIDTH) /  len(MAP)) 
    level = Grid(MAP, TILE_WIDTH)
    P1 = Player(TILE_WIDTH, 5, TILE_WIDTH, TILE_WIDTH, level, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q], "1", (174, 137, 218))
    P2 = Player(TILE_WIDTH, 5, (9) * TILE_WIDTH, (7) * TILE_WIDTH, level, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE], "2", (124, 227, 228))
    S1 = Projectile(15, P1, level, (0, 0, 0))
    S2 = Projectile(15, P2, level, (0, 255, 0))
    P1text = "P1 press q"
    P2text = "P2 press space"
    return P1, P2, S1, S2, level, P1text, P2text
      

def check_hit(player, projectile):
    hitbox = player.get_hitbox()
    if hitbox != None:
        if hitbox.collidepoint(projectile.center):
            projectile.destroy()
            return True
        elif player.rect.collidepoint(projectile.center):
            projectile.destroy()
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


pygame.display.set_caption("Game")

P1, P2, S1, S2, level, P1text, P2text = setup()
COUNTDOWN = FPS * 5
P1ready = P2ready = False
P1Wines = []
P1Score = P2Score = 0
winner = "NEW GAME"

HEADINGS = pygame.font.SysFont('didot.ttc', 140)
SCORES =  pygame.font.SysFont('didot.ttc', 50)
TEXT =  pygame.font.SysFont('didot.ttc', 40)
NUMBERS = pygame.font.SysFont('didot.ttc', 250)


#Main loop
game = "start"
while True:
    if game == "start":
        pygame.display.update()
        DISPLAYSURF.fill(Colours["GREY"])

        if pygame.key.get_pressed()[pygame.K_q]:
            P1ready = True
            P1text = "Player 1 is ready"
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            P2ready = True
            P2text = "Player 2 is ready"

        if P1ready and P2ready:
             COUNTDOWN -= 1
             for i in range(150, 0, -10):
                 DISPLAYSURF.blit(NUMBERS.render(str(COUNTDOWN // FPS + 1), True, ((51*i)/50, (17*i)/15, (181*i)/150)), (SCREEN_WIDTH //2  - 10 + i/10, SCREEN_HEIGHT // 2 - 10 + i/10 ))

        if COUNTDOWN == 0: 
             game = "playing"


        DISPLAYSURF.blit(HEADINGS.render(P1text, True, Colours["SHADOW"]), (53, 173))
        DISPLAYSURF.blit(HEADINGS.render(P2text, True, Colours["SHADOW"]), (53, 273))
        DISPLAYSURF.blit(HEADINGS.render(winner, True, Colours["SHADOW"]), (53, 53))
        DISPLAYSURF.blit(HEADINGS.render(P1text, True, Colours["BLACK"]), (50, 175))
        DISPLAYSURF.blit(HEADINGS.render(P2text, True, Colours["BLACK"]), (50, 275))
        DISPLAYSURF.blit(HEADINGS.render(winner, True, Colours["BLACK"]), (50, 50))


        DISPLAYSURF.blit(SCORES.render("Scores:", True, Colours["BLACK"]), (50, 515)) 
        DISPLAYSURF.blit(SCORES.render("P1", True, Colours["BLACK"]), (55, 560))        
        DISPLAYSURF.blit(SCORES.render("P2", True, Colours["BLACK"]), (106, 560))
        for i in range(0,54,53):
            pygame.draw.rect(DISPLAYSURF, Colours["BLACK"], (50 + i, 605, 50, 160), 5)
            for j in range(0,5):
                try:
                    if P1Wines[j] != (i == 53):
                        DISPLAYSURF.blit(TEXT.render("W", True, Colours["BLACK"]), (60 + i, 610 + j  * 30))
                    else:
                         DISPLAYSURF.blit(TEXT.render("L", True, Colours["BLACK"]), (65 + i, 610 + j * 30))
                except:
                    pass
        DISPLAYSURF.blit(SCORES.render(str(P1Score), True, Colours["BLACK"]), (63, 770))
        DISPLAYSURF.blit(SCORES.render(str(P2Score), True, Colours["BLACK"]), (115, 770))

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
            winner = "LAST WINNER = P1"
            P1Score += 1
            P1Wines.append(True)
        else:
            winner ="LAST WINNER = P2"
            P2Score += 1
            P1Wines.append(False)

        P1, P2, S1, S2, level, P1text, P2text = setup()
        P1ready = P2ready = False
        COUNTDOWN = FPS * 3
        game = "start"

    FramePerSec.tick(FPS)
    #Allows the window to be closed
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
