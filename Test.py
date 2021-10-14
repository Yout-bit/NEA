import sys
import pygame
from pygame import transform
from pygame.font import match_font
from pygame.key import *
from pygame.locals import *
import math
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1020,1020))
image = pygame.Surface((255,255))
c = 0
x=0
cool = 0
n = 4
while True:
    pygame.display.update()
    c+=1
    for i in range(255):
        for j in range(255):
            if x % n == 0:
               image.set_at((i,j),  (math.sin(i^j^c)*math.sin(j^i^c) % 255, math.cos(j^i^c)*math.cos(i^j^c) % 255, math.tan(i^j^c) * math.tan(j^i^c) % 255))
            elif x % n == 1:
                image.set_at((i,j),  (i^c % 255, j^c % 255, ((i*j)^c) % 255))
            elif x % n == 2:
                image.set_at((i,j),  ((i^(j^c)) % 255, (j^(i^c)) % 255, (c^(i^j)) % 255))
            elif x % n == 3:
                image.set_at((i,j),  (i,j,c % 255))
    DISPLAYSURF.blit(pygame.transform.scale(image, (1020,1020)),(0,0))

    if cool != 0:
        cool -= 1
    if pygame.key.get_pressed()[pygame.K_SPACE] and cool == 0:
        cool = 20
        x += 1

    FramePerSec.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()