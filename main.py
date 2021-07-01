import sys
import pygame
from pygame.locals import *
import math
import random

from player import Player
from grid import Grid
from projectile import Projectile 




pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

def map():
    map_choice = random.randint(3,3)
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

MAP = map()




SCREEN_WIDTH = 1100
TILE_WIDTH = int(SCREEN_WIDTH / 11)
SCREEN_HEIGHT = int(TILE_WIDTH * 9)

level = Grid(MAP, TILE_WIDTH)


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
FONT = pygame.font.SysFont('didot.ttc', 140)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Game")

def rot_center(image, angle, xy):
    x, y = xy
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

def check_hit(player, projectile):
    if player.rect.left <= projectile.center.x <= player.rect.right and player.rect.top <= projectile.center.y <= player.rect.bottom:
        back, inner = player.get_hitbox(15)
        if (back - projectile.center).magnitude() + (inner - projectile.center).magnitude() == 15:
            projectile.destroy()
            return True
        else:
            projectile.destroy()
    return False


 
         
P1 = Player(TILE_WIDTH, 5, TILE_WIDTH, TILE_WIDTH, level, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q], "1", (174, 137, 218))
P2 = Player(TILE_WIDTH, 5, (9) * TILE_WIDTH, (7) * TILE_WIDTH, level, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE], "2", (124, 227, 228))
S1 = Projectile(15, P1, level, (0, 0, 0))
S2 = Projectile(15, P2, level, (0, 255, 0))


game_playing = True
loser = None
while game_playing:
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
        game_playing = False


    FramePerSec.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
       
            
#End screen
while True:
    pygame.display.update()

    DISPLAYSURF.fill(Colours["GREY"])
    if P1_winner:
        DISPLAYSURF.blit(FONT.render("Player 1 is the winner", True, Colours["GREEN"]), (50, 50) )
    else:
        DISPLAYSURF.blit(FONT.render("Player 2 is the winner", True, Colours["GREEN"]), (50, 50) )

    FramePerSec.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()