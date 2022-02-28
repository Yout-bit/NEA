import socket
import sys
import pygame
from pygame.font import match_font
from pygame.key import *
from pygame.locals import *

from grid import Grid
from grid import Cliant_Grid
from InputBoxes import InputBox


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



def shadow_text(size, text, loc, disp):
    x, y = loc
    disp.blit(Text(size).render(text, True, Colours["SHADOW"]), (x + disp, y + disp))
    disp.blit(Text(size).render(text, True, Colours["BLACK"]), loc)
    
def draw_menu(response):
    shadow_text(112, "NEW GAME", (40, 40), 3)
    readys = response[3:3 + int(response[1])]
    for i in range(int(response[1])):
        if readys[i] == "0": 
            shadow_text(112, "P" + str(i+1) + " press space", (40, 120 + i*85), 3)
        else:
            shadow_text(112, "P" + str(i+1) + " is ready", (40, 120 + i*85), 3)

def Text(size):
    #return pygame.font.Font('Helvetica.ttf', size)
    return pygame.font.SysFont('didot.ttf', size)

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

def conn(host, port):
    ClientSocket = socket.socket()
    try:
        ClientSocket.connect((host, port))
        return ClientSocket
    except socket.error as e:
        return True

mapnum = -1

def set_up_map(map_choice, disp):
    level = Cliant_Grid(map_choice, 80, disp)
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

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.blit(pygame.transform.scale(pygame.image.load("Menu1.png"), (880, 720)), (0,0))

pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

ClientSocket = True
input_boxes = [InputBox(55, 200, 140, 32), InputBox(395, 200, 140, 32)]
text = ""

#Connection menu
while ClientSocket == True:
    pygame.display.update()
    DISPLAYSURF.blit(background, (0,0))
    shadow_text(112, "Enter host and port", (40, 40), 3)
    shadow_text(70, "Host:", (55, 150), 2)
    shadow_text(70, "Port:", (395, 150), 2)

    for box in input_boxes:
        box.update()
        box.draw(DISPLAYSURF)
    shadow_text(60, text, (50,300), 2)
             
    FramePerSec.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for box in input_boxes:
            box.handle_event(event)
    if input_boxes[0].output != "" and input_boxes[1].output != "":
        ClientSocket = conn(input_boxes[0].output, int(input_boxes[1].output))
        text = "Server not found"
        input_boxes[0].output = input_boxes[1].output = ""
        

        
background.blit(pygame.transform.scale(pygame.image.load("Menu.png"), (880, 720)), (0,0))

Response = ClientSocket.recv(4096)
#Main loop
while True:
    pygame.display.update()

    #Communication with server
    ClientSocket.send(str.encode(get_inputs()))
    Response = ClientSocket.recv(4096).decode('utf-8')

    #In gameplay
    if Response[0] == "1" and len(Response) == (3 + int(Response[1]) * 12):
        if int(Response[2]) != mapnum:
            mapnum = int(Response[2])
            level = set_up_map(mapnum, DISPLAYSURF)
        level.draw()

        playerlocs = []
        for i in range(int(Response[1])):
            playerlocs.append([int(Response[3 + (12 * i):6 + (12 * i)]), int(Response[6 + (12 * i):9 + (12 * i)])])
            pygame.draw.circle(DISPLAYSURF, [0, 0, 0], (int(Response[9 + (12 * i):12 + (12 * i)]), int(Response[12 + (12 * i):15 + (12 * i)])), 16)

        draw_players(playerlocs)
            
    else:
        DISPLAYSURF.blit(background, (0,0))
        draw_menu(Response)
        

    FramePerSec.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

ClientSocket.close()
