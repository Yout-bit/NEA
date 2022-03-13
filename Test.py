import socket

from types import TracebackType
import pygame
#from pygame.key import *
#from pygame.locals import *

from grid import Client_Grid
from inputboxes import InputBox



pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 880
SCREEN_HEIGHT = 720
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Game")
while True:
    pygame.display.update()
    player_colours = [
        (100, 49, 158),
        (51, 49, 158),
        (49, 143, 158),
        (49, 158, 65)
    ]
    for i in range(4):
        player = pygame.Rect((80 + 80 * i, 80 + 80 * i), (80,80))
        pygame.draw.rect(DISPLAYSURF, (player_colours[i]), player)
        pygame.draw.rect(DISPLAYSURF, (255,0,0), pygame.Rect((80 + 80 * i, 80 + 80 * i), (80, 16)))

    FramePerSec.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
