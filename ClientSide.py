import socket
import sys
import pygame
from pygame.font import match_font
from pygame.key import *
from pygame.locals import *
import math
import random

from player import Player
from grid import Grid
from projectile import Projectile 


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


def setup():
    MAP = map()
    TILE_WIDTH = math.sqrt((SCREEN_HEIGHT * SCREEN_WIDTH) /  len(MAP)) 
    level = Grid(MAP, TILE_WIDTH, DISPLAYSURF)
    P1 = Player(TILE_WIDTH, 5, TILE_WIDTH, TILE_WIDTH, level, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q], "1", (174, 137, 218))
    P2 = Player(TILE_WIDTH, 5, (9) * TILE_WIDTH, (7) * TILE_WIDTH, level, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE], "2", (124, 227, 228))
    S1 = Projectile(15, P1, level, (0, 0, 0))
    S2 = Projectile(15, P2, level, (0, 255, 0))
    P1text = "P1 press q"
    P2text = "P2 press space"
    return P1, P2, S1, S2, level, P1text, P2text


def shadow_text(size, text, loc, disp)
    x, y = loc
    DISPLAYSURF.blit(Text(size).render(text, True, Colours["SHADOW"]), (x + disp, y + disp))
    DISPLAYSURF.blit(Text(size).render(text, True, Colours["BLACK"]), loc)
    
def draw_menu(response):
    shadow_text(112, "NEW GAME", (40, 40), 3)
    for i in range(int(response[1])):
        readys = response[2:2 + int(response[1])]
        if readys[i] == "0": 
            shadow_text(112, "P" + str(i+1) + " press space", (40, 120 + i*85), 3)
        else:
            shadow_text(112, "P" + str(i+1) + " is ready", (40, 120 + i*85), 3)

def Text(size):
    return pygame.font.SysFont('didot.ttc', size)

def check_pressed(keys, inp):
    if keys[inp]:
        return "1"
    else:
        return "0"

#[Forward, Right, Back, Left, Fire]
def get_inputs():
    pressed_keys = pygame.key.get_pressed()
    x = "" 
    for key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE]:
        x += check_pressed(pressed_keys, key)
    return str(x)

mapnum = -1

def set_up_map(map_choice):
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
    level = Grid(MAP, 80, DISPLAYSURF)
    return level

def draw_players(locs):
    for i in range(len(locs)):
        player = pygame.Rect((locs[i][0], locs[i][1]), (80,80))
        pygame.draw.rect(DISPLAYSURF, (30 * (i+1), 50 * (i+1), 70 * (i+1)), player)
              
   

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 880
SCREEN_HEIGHT = 720
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Game")

#P1, P2, S1, S2, level, P1text, P2text = setup()
COUNTDOWN = FPS * 5 

#1ready = P2ready = False
#P1Wines = []
#P1Score = P2Score = 0
#winner = "NEW GAME"

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill(Colours["GREY"])
for i in range(1,random.randint(1,20)):
    pygame.draw.circle(background, (255, 0, 0, 200), (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)), random.randint(25, 100))


pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))



ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    pygame.display.update()
    DISPLAYSURF.fill(Colours["GREY"])
    #DISPLAYSURF.blit(background, (0,0))

    ClientSocket.send(str.encode(get_inputs()))
    Response = ClientSocket.recv(1024).decode('utf-8')
    if Response[0] == "1":
        if int(Response[2]) != mapnum:
            mapnum = int(Response[2])
            level = set_up_map(mapnum)
        level.draw()

        playerlocs = []
        for i in range(int(Response[1])):
            playerlocs.append([int(Response[3 + (12 * i):6 + (12 * i)]), int(Response[6 + (12 * i):9 + (12 * i)])])
            pygame.draw.circle(DISPLAYSURF, [0, 0, 0], (int(Response[9 + (12 * i):12 + (12 * i)]), int(Response[12 + (12 * i):15 + (12 * i)])), 16)

        draw_players(playerlocs)
    else:
        draw_menu(P1text, P2text, winner, P1Score, P2Score, COUNTDOWN):
        

        







    FramePerSec.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

ClientSocket.close()
