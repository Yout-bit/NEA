import socket
import os
from _thread import *
import sys
import pygame
from pygame.font import match_font
from pygame.key import *
from pygame.locals import *
import math
import random

from player import Player
from collisions import Collisions
from projectile import Projectile 


SCREEN_WIDTH = 880
SCREEN_HEIGHT = 720

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
    DISPLAYSURF = 1
    MAP = map()
    TILE_WIDTH = math.sqrt((SCREEN_HEIGHT * SCREEN_WIDTH) /  len(MAP)) 
    level = Collisions(MAP, TILE_WIDTH, DISPLAYSURF)
    for player in  players:
        player

    P1 = Player(TILE_WIDTH, 5, TILE_WIDTH, TILE_WIDTH, level, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q], "1")
    P2 = Player(TILE_WIDTH, 5, (9) * TILE_WIDTH, (7) * TILE_WIDTH, level, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE], "2")
    S1 = Projectile(15, P1, level, (0, 0, 0))
    S2 = Projectile(15, P2, level, (0, 255, 0))
    P1text = "P1 press q"
    P2text = "P2 press space"
    return P1, P2, S1, S2, level, P1text, P2text

def check_hit(player, projectile):
    hitbox = player.get_hitbox()
    if hitbox != None and not player.dead:
        if hitbox.collidepoint(projectile.center):
            projectile.destroy()
            player.destroy()
            return True
        elif player.rect.collidepoint(projectile.center):
            projectile.destroy()
        else:
            return False

def create_player(players, number):
    if number == 0:
        players.append(Player(80, 5, 80, 80, level, number))
    elif number == 1:
        players.append(Player(80, 5, 720, 560, level, number))
    elif number == 2:
        players.append(Player(80, 5, 80, 560, level, number))
    else:
        players.append(Player(80, 5, 720, 80, level, number))
    return players

def threefigs(number):
    number = str(int(number))
    while len(number) < 3:
        number = "0" + number 
    return number


#P1, P2, S1, S2, level, P1text, P2text = setup()
DISPLAYSURF = 1
mapnum = random.randint(0,7)
level = Collisions(mapnum)
COUNTDOWN = 60 * 5 

P1ready = P2ready = False
P1Wines = []
P1Score = P2Score = 0

#Data to send to cliants
#[Game State(Menu/Game - 0/1), NumOfPlayers, Map, P1pos, S1pos rept for all players]
output = "121080080200120720560999999"

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)
players = []
shots = []

def threaded_client(connection, number):
    global output
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        reply = data.decode('utf-8')
        for i in range(len(players)):
            if players[i].name == number:
                players[i].update(reply)
                shots[i].update()
        if not data:
            break
        connection.sendall(str.encode(output))
    connection.close()

def threaded_main():
    global output
    while True:
        x = "1" + str(len(players)) + str(mapnum)
        for i in range(len(players)):
            for j in range(len(shots)):
                if i != j:
                    check_hit(players[i], shots[j])
            for j in (players[i].get_pos() + shots[i].get_pos()):
                x += threefigs(j)
        output = x



start_new_thread(threaded_main, ())


#Handelling new connections
ThreadCount = 0
while ThreadCount != 4:

    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, str(ThreadCount)))
    players = create_player(players, ThreadCount)
    shots.append(Projectile(15, players[ThreadCount], level, (0, 0, 0)))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))




