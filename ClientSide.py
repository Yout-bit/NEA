import sys
import pygame
from pygame.key import *
from pygame.locals import *
import math
import random

#Client side needs only draw functions 
#Data input method: array
#[GAME STATE, No. of players, (P1topleft, P2topleft, P3topleft, P4topleft), (S1center, S2center, S3center, S4center), map, (pygame print outputs as functions)]
#if None no player 


#networking bizzle

#Setting up the pygame window
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 900

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Main loop
while True:
  
    pygame.display.update()
    
    DISPLAYSURF.fill(Colours["GREY"])
    
    if game_state == "start":
     #do the printy functions
     for i in inputs[6]:
        i
      
      #get inputs from server
      #give server client inputs
    
    elif game == "playing":
        P1.draw(DISPLAYSURF)
        P2.draw(DISPLAYSURF)
        level.draw(DISPLAYSURF)
        S1.draw(DISPLAYSURF)
        S2.draw(DISPLAYSURF)

        #get inputs from server
        #give server client inputs
        
    #End screen  
    elif game == "end":        
     #do the printy functions
     for i in inputs[6]:
        i
      
      #get inputs from server
      #give server client inputs

    FramePerSec.tick(FPS)
    #Allows the window to be closed
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
