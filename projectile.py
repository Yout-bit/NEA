import re
import pygame
from pygame.math import Vector2 

class Projectile():
    def __init__(self, speed, player, level, colour):
        self.level = level
        self.player = player
        self.speed = speed
        self.colour = colour
        self.dir = Vector2(0, 0)
        self.next_move = Vector2()
        self.center = Vector2(0, 0)
        self.motion = False
        self.cooldown = 0

    #Removes the projectile, used if it hits a wall or the non hitbox area of a player
    def destroy(self):
        self.center = Vector2(0, 0)
        self.cooldown = 30
        self.motion = False

    def update(self):
        #If still on cooldown, counts the timer down and does not fire
        if self.cooldown > 0:
            self.cooldown -= 1
            return
        #When the fire button is first pressed and the projectile is not already in motion
        if self.player.fire and not self.motion:
            self.center = self.player.get_front()
            self.motion = True 
            #Checks the direction vector is not (0, 0)
            if self.player.dir.magnitude() != 0:
                self.dir = self.player.dir 
            else:
                self.motion = False
        #Movement - finds next posyion and checks it is not a wall, then either destroys iteslef or moves accordingly 
        if self.motion:
            self.next_move = self.center + (self.dir * self.speed)
            if self.level.get_grid_value(self.next_move) == "#":
                self.destroy()
            else:
                self.center = self.next_move




    def get_pos(self):
        return str(self.center.x) + str(self.center.y)
            



    #Draws itself onto the board
    def draw(self, surface):
        if self.motion:
            pygame.draw.circle(surface, self.colour, (int(self.center.x), int(self.center.y)), 16)

