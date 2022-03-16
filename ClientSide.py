from math import floor
import pygame
import socket

from grid import Client_Grid
from inputboxes import InputBox


Colours = {
    "RED"   : (255, 0, 0),
    "BLACK" : (0, 0, 0),
    "SHADOW": (103, 120, 131)
    }

Player_Colours = [
    (100, 49, 158),
    (51, 49, 158),
    (49, 143, 158),
    (49, 158, 65)
    ]

#Displays text at the given location with some drop shadow to make it easier to read against backgrounds of differnt colour 
def shadow_text(size, text, loc, disp):
    x, y = loc
    DISPLAYSURF.blit(Text(size).render(text, True, Colours["SHADOW"]), (x + disp, y + disp))
    DISPLAYSURF.blit(Text(size).render(text, True, Colours["BLACK"]), loc)
    
#Displays the main text, players and scores
def draw_menu(response):
    shadow_text(112, "NEW GAME", (40, 40), 3)
    shadow_text(60, "SCORES", (700,60), 3)
    for i in range(int(response[1])):
        if response[3 + 2 *i] == "0": 
            shadow_text(112, "P" + str(i+1) + " press space", (40, 120 + i*85), 3)
        else:
            shadow_text(112, "P" + str(i+1) + " is ready", (40, 120 + i*85), 3)
        shadow_text(122, response[4 + 2 * i], (800, 120 + i*85), 3)

def Text(size):
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

#Tries to connect, else returns true
def conn(host, port):
    ClientSocket = socket.socket()
    try:
        ClientSocket.connect((host, port))
        return ClientSocket
    except socket.error as e:
        return True

mapnum = -1

#Creates a Client_Grid object
def set_up_map(map_choice, disp):
    level = Client_Grid(map_choice, 80, disp)
    return level

#Draws a rect at every players postion, colour dependant on what number player they are
def draw_players(locs):
    for i in range(len(locs)):
        player = pygame.Rect((locs[i][0], locs[i][1]), (80,80))
        pygame.draw.rect(DISPLAYSURF, (Player_Colours[i]), player)
        #Calculates and draws the hitbox based on the direction given 
        if locs[i][2] == "N":
            pygame.draw.rect(DISPLAYSURF, Colours["RED"], pygame.Rect((locs[i][0], (locs[i][1] + 64)), (80, 16)))
        elif locs[i][2] == "S":
            pygame.draw.rect(DISPLAYSURF, Colours["RED"], pygame.Rect((locs[i][0], locs[i][1]), (80, 16)))
        elif locs[i][2] == "E":
            pygame.draw.rect(DISPLAYSURF, Colours["RED"], pygame.Rect((locs[i][0], locs[i][1]), (16, 80)))
        else:
            pygame.draw.rect(DISPLAYSURF, Colours["RED"], pygame.Rect((locs[i][0] + 64, locs[i][1]), (16, 80)))
              
   
#Sets up the pygame window
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 880
SCREEN_HEIGHT = 720
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Game")

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.blit(pygame.transform.scale(pygame.image.load("Images\Conn Menu.png"), (880, 720)), (0,0))

ClientSocket = True
input_boxes = [InputBox(55, 200, 200, 32), InputBox(395, 200, 200, 32)]
text = ""

#Connection menu, loop ends when a connection is found
while ClientSocket == True:
    pygame.display.update()
    DISPLAYSURF.blit(background, (0,0))

    shadow_text(112, "Enter host and port", (40, 40), 3)
    shadow_text(70, "Host:", (55, 150), 2)
    shadow_text(70, "Port:", (395, 150), 2)

    for box in input_boxes:
        box.update(DISPLAYSURF)     
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
        

#Creates 2 background surfaces, each with a different frame of the button animation on
background.blit(pygame.transform.scale(pygame.image.load("Images\Game Menu.png"), (880, 720)), (0,0))        
background1 = background.copy()

pygame.draw.rect(background, Colours["BLACK"], pygame.Rect(83, 533, 65, 65))
pygame.draw.rect(background, Colours["BLACK"], pygame.Rect(8, 608, 65, 65))
pygame.draw.rect(background, Colours["BLACK"], pygame.Rect(83, 608, 65, 65))
pygame.draw.rect(background, Colours["BLACK"], pygame.Rect(158, 608, 65, 65))
pygame.draw.rect(background, Colours["BLACK"], pygame.Rect(233, 608, 212, 65))
background.blit(pygame.transform.scale(pygame.image.load("Images\Controls - WASD.png"), (216, 140)), (5, 530))
background.blit(pygame.transform.scale(pygame.image.load("Images\Controls - Space.png"), (216, 70)), (226, 601))

background1.blit(pygame.transform.scale(pygame.image.load("Images\Controls - WASD.png"), (216, 140)), (8, 533))
background1.blit(pygame.transform.scale(pygame.image.load("Images\Controls - Space.png"), (216, 70)), (229, 604))
tick = 0.0

Response = ClientSocket.recv(4096)
#Main loop
while True:
    pygame.display.update()

    #Communication with server
    ClientSocket.send(str.encode(get_inputs()))
    Response = ClientSocket.recv(4096).decode('utf-8')

    #If the map ever changes (also on start), creates an instance of the client_grid class with the new number
    if int(Response[2]) != mapnum:
        mapnum = int(Response[2])
        level = set_up_map(mapnum, DISPLAYSURF)

    #In gameplay, if the game state is gameplay
    if Response[0] == "1":

        #Draws the background, then projectiles, then players
        level.draw()

        playerlocs = []
        for i in range(int(Response[1])):
            playerlocs.append([int(Response[3 + (13 * i):6 + (13 * i)]), int(Response[6 + (13 * i):9 + (13 * i)]), Response[15 + (13 * i)]])
            pygame.draw.circle(DISPLAYSURF, Colours["BLACK"], (int(Response[9 + (13 * i):12 + (13 * i)]), int(Response[12 + (13 * i):15 + (13 * i)])), 16)

        draw_players(playerlocs)

    #Else, the game state is menu    
    else:
        #Every 100 frames changes the animtion
        tick += 1
        if tick % 200 > 100:
            DISPLAYSURF.blit(background, (0,0))
        else:
            DISPLAYSURF.blit(background1, (0,0))
        shadow_text(60, "Movement       Fire",(10,675),1)
        draw_menu(Response)
        

    FramePerSec.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

ClientSocket.close()
