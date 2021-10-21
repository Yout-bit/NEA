import sys
import pygame
from pygame.font import match_font
from pygame.key import *
from pygame.locals import *
import math
import random
#from OpenGL.GL import *
#from OpenGL.GLU import *


from player import Player
from grid import Grid
from projectile import Projectile 



from datetime import date

today = date.today()
if today.month == 10 and today.day > 25:
    Halloween = True
else:
    Halloween = False


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
    map_choice = random.randint(7,7)
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
        MAP = "##########------###-####-###-#-----##---#-#-##-#---#-##-#-#---##-----#-###-####-###------##########" 
    elif map_choice == 7:
        MAP = "##########-------##-#####-##-------###-#-#-####-----####-#-#-###-------##-#####-##-------##########"       
    return MAP

def setup():
    MAP = map()
    TILE_WIDTH = math.sqrt((SCREEN_HEIGHT * SCREEN_WIDTH) /  len(MAP)) 
    level = Grid(MAP, TILE_WIDTH, DISPLAYSURF)
    P1 = Player(TILE_WIDTH, 5
    , TILE_WIDTH, TILE_WIDTH, level, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q], "1", (174, 137, 218))
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


def draw_menu(P1text, P2text, winner, P1Score, P2Score, COUNTDOWN):
    DISPLAYSURF.blit(Text(112).render(P1text, True, Colours["SHADOW"]), (43, 123))
    DISPLAYSURF.blit(Text(112).render(P2text, True, Colours["SHADOW"]), (43, 203))
    DISPLAYSURF.blit(Text(112).render(winner, True, Colours["SHADOW"]), (43, 43))
    DISPLAYSURF.blit(Text(112).render(P1text, True, Colours["BLACK"]), (40, 120))
    DISPLAYSURF.blit(Text(112).render(P2text, True, Colours["BLACK"]), (40, 200))
    DISPLAYSURF.blit(Text(112).render(winner, True, Colours["BLACK"]), (40, 40))

    DISPLAYSURF.blit(Text(40).render("Scores:", True, Colours["SHADOW"]), (42, 414)) 
    DISPLAYSURF.blit(Text(40).render("Scores:", True, Colours["BLACK"]), (40, 412)) 
    DISPLAYSURF.blit(Text(40).render("P1", True, Colours["SHADOW"]), (47, 452))       
    DISPLAYSURF.blit(Text(40).render("P2", True, Colours["SHADOW"]), (88, 452))
    DISPLAYSURF.blit(Text(40).render("P1", True, (174, 137, 218)), (45, 450))        
    DISPLAYSURF.blit(Text(40).render("P2", True, (124, 227, 228)), (86, 450))
    for i in range(0,44,42):
        pygame.draw.rect(DISPLAYSURF, Colours["BLACK"], (40 + i, 484, 40, 128), 4)
        for j in range(0,5):
            try:
                if P1Wines[j] != (i == 42):
                    DISPLAYSURF.blit(Text(32).render("W", True, Colours["BLACK"]), (48 + i , 488 + j  * 24))
                else:
                    DISPLAYSURF.blit(Text(32).render("L", True, Colours["BLACK"]), (52 + i, 488 + j * 24))
            except IndexError:
                pass
    DISPLAYSURF.blit(Text(40).render(str(P1Score), True, Colours["BLACK"]), (50, 616))
    DISPLAYSURF.blit(Text(40).render(str(P2Score), True, Colours["BLACK"]), (95, 616))
    if COUNTDOWN != 5*60:
        for i in range(150, 0, -10):
            DISPLAYSURF.blit(Text(250).render(str(COUNTDOWN // FPS + 1), True, ((51*i)/50, (17*i)/15, (181*i)/150)), (SCREEN_WIDTH //2  - 50 + i/10, SCREEN_HEIGHT // 2 - 10 + i/10 ))

#Setting up the pygame window
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 880
SCREEN_HEIGHT = 720

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

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
if not  Halloween:
    background.fill(Colours["GREY"])
for i in range(1,random.randint(1,20)):
    pygame.draw.circle(background, (255, 0, 0, 200), (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)), random.randint(25, 100))
#background = pygame.image.load(r'Images/Background.png')

def Text(size):
    return pygame.font.SysFont('didot.ttc', size)


pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

#Main loop
game = "start"
while True:
    if game == "start":

        pygame.display.update()
        DISPLAYSURF.fill(Colours["GREY"])
        DISPLAYSURF.blit(background, (0,0))


        if pygame.key.get_pressed()[pygame.K_q]:
            P1ready = True
            P1text = "Player 1 is ready"
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            P2ready = True
            P2text = "Player 2 is ready"

        if P1ready and P2ready:
             COUNTDOWN -= 1
             for i in range(150, 0, -10):
                 DISPLAYSURF.blit(Text(250).render(str(COUNTDOWN // FPS + 1), True, ((51*i)/50, (17*i)/15, (181*i)/150)), (SCREEN_WIDTH //2  - 50 + i/10, SCREEN_HEIGHT // 2 - 10 + i/10 ))


        draw_menu(P1text, P2text, winner, P1Score, P2Score, COUNTDOWN)


        if COUNTDOWN == 0: 
            game = "playing"


    elif game == "playing":
        pygame.display.update()

        DISPLAYSURF.fill(Colours["GREY"])

        P1.update()
        P2.update()
        S1.update()
        S2.update()

        level.draw()
        S1.draw(DISPLAYSURF)
        S2.draw(DISPLAYSURF)
        P1.draw(DISPLAYSURF)
        P2.draw(DISPLAYSURF)



        P2_winner = check_hit(P1, S2)
        P1_winner = check_hit(P2, S1)
        if P1_winner or P2_winner:
            game = "end"


 
    elif game == "end":        
        pygame.display.update()

        DISPLAYSURF.fill(Colours["GREY"])
        if P1_winner:
            winner = "LAST WINNER = P1"
            P1Score += 1
            P1Wines.insert(0, True)
        else:
            winner ="LAST WINNER = P2"
            P2Score += 1
            P1Wines.insert(0, False)

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
