from math import floor
from turtle import back
import pygame
import socket

from grid import Client_Grid
from inputboxes import InputBox

Colours = {
    "RED"   : (255, 0, 0),
    "BLACK" : (0, 0, 0),
    "SHADOW": (103, 120, 131)
    }

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 880
SCREEN_HEIGHT = 720
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) 

background.blit(pygame.transform.scale(pygame.image.load("Images\Game Menu.png"), (880, 720)), (0,0))        
background1 = background.copy()
#background1.blit(pygame.transform.scale(pygame.image.load("Images\Game Menu.png"), (880, 720)), (0,0))

pygame.draw.rect(background, Colours["BLACK"], pygame.Rect(83, 533, 65, 65))
pygame.draw.rect(background, Colours["BLACK"], pygame.Rect(8, 608, 65, 65))
pygame.draw.rect(background, Colours["BLACK"], pygame.Rect(83, 608, 65, 65))
pygame.draw.rect(background, Colours["BLACK"], pygame.Rect(158, 608, 65, 65))
pygame.draw.rect(background, Colours["BLACK"], pygame.Rect(233, 608, 212, 65))
background.blit(pygame.transform.scale(pygame.image.load("Images\Controls - WASD.png"), (216, 140)), (5, 530))
background.blit(pygame.transform.scale(pygame.image.load("Images\Controls - Space.png"), (216, 70)), (226, 601))

x = pygame.image.load("Images\Game Menu.png")
x = x.fill(Colours["BLACK"])
print (type(x))
pygame.draw.rect(background1, Colours["BLACK"], x)

background1.blit(pygame.transform.scale(pygame.image.load("Images\Controls - WASD.png"), (216, 140)), (8, 533))
background1.blit(pygame.transform.scale(pygame.image.load("Images\Controls - Space.png"), (216, 70)), (229, 604))

while True:
    pygame.display.update()
    DISPLAYSURF.blit(background1, (0,0))

    FramePerSec.tick(FPS)

