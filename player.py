from random import normalvariate
import pygame
from pygame.locals import *
import math
from pygame.math import Vector2 

centers = [Vector2(0,0), Vector2(0,0)]

class Player(pygame.sprite.Sprite):
    def __init__(self, size, move_speed, start_x, start_y, level, inp_moves, name, colour):
        super().__init__()
        self.dir = Vector2(0,0)
        self.wish_dir = Vector2()
        self.level = level
        self.move_speed = move_speed
        self.moves = inp_moves
        self.size = int(size)
        self.name = name
        self.colour = colour
        self.surf = pygame.Surface((size, size))
        self.rect = self.surf.get_rect()
        self.rect = Rect(start_x, start_y, size, size)
        self.fire = False
        self.bonk = 0


    #Checks whether the player can be moved by the input vector
    def detect_collision(self, vec):
        width_modifier = (self.size /2) -1 
        edge = Vector2(vec.x * (width_modifier) , vec.y * (width_modifier))   
        corner_1 = Vector2()
        corner_2 = Vector2() 
        if abs(vec.x) > 0:
            corner_1 = Vector2(self.rect.center) + edge + Vector2(0, width_modifier) + vec * self.move_speed
            corner_2 = Vector2(self.rect.center) + edge - Vector2(0, width_modifier) + vec * self.move_speed
        if abs(vec.y) > 0:
            corner_1 = Vector2(self.rect.center) + edge + Vector2(width_modifier, 0) + vec * self.move_speed
            corner_2 = Vector2(self.rect.center) + edge - Vector2(width_modifier, 0) + vec * self.move_speed

        return self.level.get_grid_value(corner_1.xy) == "#" or self.level.get_grid_value(corner_2.xy) == "#"

    #Checks if the center of the player lies within a players width of the center of the other player
    def detect_player(self):
        for i in centers:
            if (centers.index(i) != (int(self.name)-1)):
                i = Vector2(i)
                difference = Vector2((i.x - self.rect.centerx), (i.y - self.rect.centery))
                if (abs(difference.x) <= 100 and abs(difference.y == 0))  or (abs(difference.y) <=100 and abs(difference.x == 0)):
                    if not self.detect_collision(self.dir):
                        self.dir = difference.normalize() * -1

    #Assigns the wish diretion based on the input and checks if the player fires
    def input(self):
        pressed_keys = pygame.key.get_pressed()
        self.wish_dir = Vector2(1,0) if pressed_keys[self.moves[3]] else self.wish_dir
        self.wish_dir = Vector2(-1,0) if pressed_keys[self.moves[2]] else self.wish_dir

        self.wish_dir = Vector2(0,1) if pressed_keys[self.moves[1]] else self.wish_dir
        self.wish_dir = Vector2(0,-1) if pressed_keys[self.moves[0]] else self.wish_dir
        if self.wish_dir.magnitude() != 0:
            self.wish_dir.normalize_ip()

        self.fire = pressed_keys[self.moves[4]]      


    #Normalise the direction vector then checks the wish direction doesnt push the player into a wall and is not opposite to the current direction. Then tests for collision with other player
    def update(self):
        centers[int(self.name)-1] = self.rect.center
        self.input()
        if self.dir.magnitude() != 0:
            normal_dir = self.dir.normalize()
        else:
            normal_dir = Vector2(0,0)  
            
        if self.wish_dir.dot(normal_dir) != -1 and not self.detect_collision(self.wish_dir):
            self.dir = self.wish_dir
        
        self.detect_player()
        if not self.detect_collision(self.dir):
            self.rect.move_ip(self.dir * self.move_speed)
        else:
            pass


    def get_center(self):
        return Vector2(self.rect.center)


    def get_front(self):
        return (self.rect.center + self.dir * (self.size / 2))


    def get_hitbox(self, width):
        back_point =  (self.rect.center - self.dir * (self.size / 2)) 
        inner_back_point =  (self.rect.center - self.dir * ((self.size / 2) - width)) 
        return back_point, inner_back_point

    
    
    def draw(self,surface):
        pygame.draw.rect(surface, self.colour, self.rect)
        if self.dir != (0,0):
            backrect = self.rect.copy()
            backrect.width -= abs(self.dir.x * 90)
            backrect.height -= abs(self.dir.y *90)
            if self.dir in [(-1,0),(0,-1)]:
                backrect.top += 90 * abs(self.dir.y)
                backrect.left += 90 * abs(self.dir.x)
            pygame.draw.rect(surface, (255, 47, 51), backrect)
